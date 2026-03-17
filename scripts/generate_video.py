#!/usr/bin/env python3
"""
BAA台本からRemotion用プロジェクトJSON・アセット・コンポジションTSXを自動生成するCLIツール

使用方法:
    # 基本（文字数比例の推定字幕）
    python generate_video.py --slide-dir ~/Canva/スライド/ --component-name SeiseiAI "作成済台本/概念系/生成AIとは何か"

    # Whisper字幕同期付き（正確なタイミング）
    python generate_video.py --whisper-sync --slide-dir ~/Canva/スライド/ --component-name SeiseiAI "作成済台本/概念系/生成AIとは何か"

    # ドライラン（変更なしでプレビュー）
    python generate_video.py --dry-run --slide-dir ~/Canva/スライド/ --component-name SeiseiAI "作成済台本/概念系/生成AIとは何か"

    # 対話式選択
    python generate_video.py --slide-dir ~/Canva/スライド/ --component-name SeiseiAI
"""
import argparse
import json
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

# スクリプトのディレクトリをパスに追加
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from text_processor import extract_slides_from_reading_script, load_script, sanitize_filename

# === 定数 ===

FPS = 30
AUDIO_DELAY_FRAMES = 30  # 音声開始まで1秒の遅延
GAP_AFTER_FRAMES = 30    # スライド間ギャップ（1秒）
VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080

DEFAULT_REMOTION_DIR = PROJECT_ROOT / "remotion"

DEFAULT_STYLE = {
    "subtitle": {
        "fontFamily": "Noto Sans JP",
        "fontSize": 43,
        "fontWeight": "bold",
        "color": "#FFFFFF",
        "backgroundColor": "rgba(0, 0, 0, 0.7)",
        "padding": 16,
        "borderRadius": 8,
        "position": "bottom",
        "marginBottom": 10,
        "maxWidth": 1600,
    },
    "image": {
        "fit": "contain",
        "backgroundColor": "#092949",
    },
    "transition": {
        "type": "fade",
        "durationFrames": 15,
    },
    "audio": {
        "volume": 1,
        "fadeInFrames": 5,
        "fadeOutFrames": 5,
    },
}

# === ユーティリティ関数 ===


def find_topic_folders(base_dir: Path) -> list[Path]:
    """作成済台本フォルダ内のトピックフォルダを検索"""
    scripts_dir = base_dir / "作成済台本"
    if not scripts_dir.exists():
        return []

    folders = []
    for category_dir in sorted(scripts_dir.iterdir()):
        if not category_dir.is_dir():
            continue
        for topic_dir in sorted(category_dir.iterdir()):
            if not topic_dir.is_dir():
                continue
            # 読み上げ用ファイルと音声フォルダがあるトピックのみ
            has_reading = any(topic_dir.glob("【読み上げ用】*.md"))
            has_audio = any(topic_dir.glob("【音声】*"))
            if has_reading and has_audio:
                folders.append(topic_dir)
    return folders


def select_topic_interactive(folders: list[Path], base_dir: Path) -> Path | None:
    """対話式でトピックフォルダを選択"""
    print("\n=== 動画生成可能なトピック一覧 ===\n")
    scripts_dir = base_dir / "作成済台本"
    for i, folder in enumerate(folders, 1):
        relative = folder.relative_to(scripts_dir)
        print(f"[{i}] {relative}")
    print()

    while True:
        try:
            user_input = input("番号を入力してください (q でキャンセル): ").strip()
            if user_input.lower() == "q":
                return None
            selection = int(user_input)
            if 1 <= selection <= len(folders):
                return folders[selection - 1]
            print(f"1から{len(folders)}の番号を入力してください。")
        except ValueError:
            print("数字を入力してください。")


def get_audio_duration(mp3_path: Path) -> float:
    """MP3ファイルの長さ（秒）を取得。afinfoを優先、なければffprobeを使用"""
    # macOS の afinfo を試す
    try:
        result = subprocess.run(
            ["afinfo", str(mp3_path)],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 0:
            for line in result.stdout.splitlines():
                if "estimated duration:" in line:
                    return float(line.split(":")[-1].strip().split()[0])
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # ffprobe フォールバック
    try:
        result = subprocess.run(
            [
                "ffprobe",
                "-v", "error",
                "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1",
                str(mp3_path),
            ],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 0:
            return float(result.stdout.strip())
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    raise RuntimeError(f"音声の長さを取得できません: {mp3_path.name}\n  afinfo または ffprobe をインストールしてください。")


def split_subtitle_text(text: str, max_chars: int = 35) -> list[str]:
    """
    テキストを字幕用に分割（max_chars文字以内）

    分割優先順:
    1. 句読点（。？！）
    2. 読点・閉じ括弧（、」）で）
    3. 強制分割（max_chars文字で切る）
    """
    if len(text) <= max_chars:
        return [text]

    segments = []

    # まず句読点で分割
    parts = re.split(r"(?<=[。？！])", text)

    for part in parts:
        part = part.strip()
        if not part:
            continue

        if len(part) <= max_chars:
            segments.append(part)
        else:
            # さらに読点・閉じ括弧で分割
            sub_parts = re.split(r"(?<=[、」）\)])", part)
            current = ""
            for sub in sub_parts:
                if not sub:
                    continue
                if len(current) + len(sub) <= max_chars:
                    current += sub
                else:
                    if current:
                        segments.append(current.strip())
                    # それでもmax_charsを超える場合は強制分割
                    while len(sub) > max_chars:
                        segments.append(sub[:max_chars])
                        sub = sub[max_chars:]
                    current = sub
            if current.strip():
                segments.append(current.strip())

    return [s for s in segments if s]


def generate_estimated_subtitles(text: str, duration_sec: float) -> list[dict]:
    """
    テキストから字幕セグメントを文字数比例で生成

    Args:
        text: スライドの読み上げテキスト
        duration_sec: スライドの音声長さ（秒）

    Returns:
        SubtitleSegment のリスト [{text, startMs, endMs}, ...]
    """
    segments_text = split_subtitle_text(text)

    if not segments_text:
        return []

    total_chars = sum(len(s) for s in segments_text)
    if total_chars == 0:
        return []

    total_ms = duration_sec * 1000
    subtitles = []
    current_ms = 0.0

    for i, seg_text in enumerate(segments_text):
        # 文字数に比例した長さ
        ratio = len(seg_text) / total_chars
        seg_duration_ms = total_ms * ratio

        start_ms = round(current_ms)
        end_ms = round(current_ms + seg_duration_ms)

        # 最後のセグメントは端数を吸収
        if i == len(segments_text) - 1:
            end_ms = round(total_ms)

        subtitles.append({
            "text": seg_text,
            "startMs": start_ms,
            "endMs": end_ms,
        })

        current_ms += seg_duration_ms

    return subtitles


# === Whisper字幕同期 ===


def sync_subtitles_with_whisper(project_json_path: Path, model_name: str = "medium") -> bool:
    """
    Whisperを使ってproject.json内の字幕タイミングを正確に同期する。

    Args:
        project_json_path: project.jsonのパス
        model_name: Whisperモデル名（tiny/base/small/medium/large）

    Returns:
        True if successful, False if whisper is not available
    """
    try:
        import whisper
    except ImportError:
        print("  警告: openai-whisper がインストールされていません。")
        print("  推定値の字幕タイミングをそのまま使用します。")
        print("  インストール: pip install openai-whisper")
        return False

    with open(project_json_path, "r", encoding="utf-8") as f:
        project = json.load(f)

    base_dir = project_json_path.parent
    audio_path = project["meta"]["audioPath"]
    # audioPathは "public/{project}/音声/{audio_dir}" 形式
    # base_dirが "public/{project}" なので、音声フォルダ名だけ抽出
    audio_dir_relative = audio_path.split("/", 2)[-1] if "/" in audio_path else audio_path
    # base_dirからの相対パスで音声フォルダを特定
    audio_base = base_dir / audio_dir_relative.replace(
        f"public/{project_json_path.parent.name}/", ""
    )

    # audioPathがフルパスの場合のフォールバック
    if not audio_base.exists():
        # "public/XXX/音声/YYY" から "音声/YYY" を取り出す
        parts = audio_path.split("/")
        for i, part in enumerate(parts):
            if part == "音声":
                audio_base = base_dir / "/".join(parts[i:])
                break

    if not audio_base.exists():
        print(f"  エラー: 音声フォルダが見つかりません: {audio_base}")
        return False

    print(f"  音声フォルダ: {audio_base}")
    print(f"  Whisperモデル ({model_name}) を読み込み中...")
    model = whisper.load_model(model_name)

    updated_count = 0

    for slide in project["slides"]:
        audio_file = audio_base / slide["audio"]
        if not audio_file.exists():
            print(f"  スキップ（ファイルなし）: {slide['audio']}")
            continue

        slide_id = slide["id"]
        subtitles = slide["subtitles"]

        if not subtitles:
            continue

        print(f"  スライド{slide_id:02d}: {slide['audio']}")

        # Whisperで解析
        result = model.transcribe(
            str(audio_file),
            language="ja",
            word_timestamps=True,
        )

        segments = result["segments"]

        # ワードレベルタイムスタンプを抽出
        whisper_words = []
        for seg in segments:
            if "words" in seg:
                for w in seg["words"]:
                    whisper_words.append({
                        "text": w["word"].strip(),
                        "start": w["start"],
                        "end": w["end"],
                    })

        if not whisper_words:
            # ワードレベルがない場合はセグメントレベルで対応
            _sync_segment_level(subtitles, segments)
            updated_count += sum(1 for _ in subtitles)
            continue

        # ワードレベルタイムスタンプがある場合
        updated_count += _sync_word_level(subtitles, whisper_words)

    # 保存
    with open(project_json_path, "w", encoding="utf-8") as f:
        json.dump(project, f, ensure_ascii=False, indent=2)

    print(f"  Whisper同期完了: {updated_count}個の字幕タイミングを更新")
    return True


def _sync_segment_level(subtitles: list[dict], segments: list[dict]) -> None:
    """セグメントレベルのタイムスタンプで字幕を同期"""
    seg_idx = 0
    for sub in subtitles:
        if seg_idx >= len(segments):
            break

        start_ms = int(segments[seg_idx]["start"] * 1000)
        sub_text_clean = sub["text"].replace(" ", "").replace("\u3000", "")
        matched_end = segments[seg_idx]["end"]

        combined_text = segments[seg_idx]["text"].replace(" ", "").replace("\u3000", "")
        next_seg = seg_idx + 1
        while next_seg < len(segments):
            candidate = combined_text + segments[next_seg]["text"].replace(" ", "").replace("\u3000", "")
            if len(candidate) <= len(sub_text_clean) * 1.3:
                combined_text = candidate
                matched_end = segments[next_seg]["end"]
                next_seg += 1
            else:
                break

        end_ms = int(matched_end * 1000)
        sub["startMs"] = start_ms
        sub["endMs"] = end_ms
        seg_idx = next_seg


def _sync_word_level(subtitles: list[dict], whisper_words: list[dict]) -> int:
    """ワードレベルのタイムスタンプで字幕を同期"""
    PUNCT = "、。「」）？！ \u3000"
    updated_count = 0
    word_idx = 0

    for sub in subtitles:
        sub_text_clean = "".join(c for c in sub["text"] if c not in PUNCT)

        start_ms = (
            int(whisper_words[word_idx]["start"] * 1000)
            if word_idx < len(whisper_words)
            else sub["startMs"]
        )

        consumed_chars = 0
        target_chars = len(sub_text_clean)
        end_word_idx = word_idx

        while consumed_chars < target_chars and end_word_idx < len(whisper_words):
            w_text = "".join(
                c for c in whisper_words[end_word_idx]["text"] if c not in PUNCT
            )
            consumed_chars += len(w_text)
            end_word_idx += 1

        if end_word_idx > 0 and end_word_idx <= len(whisper_words):
            end_ms = int(whisper_words[end_word_idx - 1]["end"] * 1000)
        else:
            end_ms = sub["endMs"]

        word_idx = end_word_idx

        old_start = sub["startMs"]
        old_end = sub["endMs"]
        sub["startMs"] = start_ms
        sub["endMs"] = end_ms

        if old_start != start_ms or old_end != end_ms:
            updated_count += 1

    return updated_count


# === メイン処理関数 ===


def validate_and_discover(
    topic_folder: Path,
    slide_dir: Path,
) -> dict:
    """
    [1/7] 入力検証・アセット検出

    Returns:
        {
            "reading_script": Path,
            "audio_dir": Path,
            "audio_files": [Path, ...],
            "slide_files": [Path, ...],
            "slides_data": [dict, ...],
        }
    """
    print("[1/7] 入力検証・アセット検出...")

    # 読み上げ用ファイルを検索
    reading_scripts = list(topic_folder.glob("【読み上げ用】*.md"))
    if not reading_scripts:
        print(f"  エラー: 読み上げ用ファイルが見つかりません: {topic_folder}")
        sys.exit(1)
    reading_script = reading_scripts[0]
    print(f"  読み上げ用: {reading_script.name}")

    # 音声フォルダを検索
    audio_dirs = list(topic_folder.glob("【音声】*"))
    if not audio_dirs:
        print(f"  エラー: 音声フォルダが見つかりません: {topic_folder}")
        sys.exit(1)
    audio_dir = audio_dirs[0]

    # MP3ファイルを取得（ソート済み）
    audio_files = sorted(audio_dir.glob("*.mp3"))
    if not audio_files:
        print(f"  エラー: MP3ファイルが見つかりません: {audio_dir}")
        sys.exit(1)
    print(f"  音声: {len(audio_files)}個のMP3 ({audio_dir.name}/)")

    # スライドPNGを取得（数字順にソート）
    slide_dir = Path(slide_dir)
    if not slide_dir.exists():
        print(f"  エラー: スライドフォルダが見つかりません: {slide_dir}")
        sys.exit(1)

    slide_files = sorted(
        slide_dir.glob("*.png"),
        key=lambda p: _extract_number(p.stem),
    )
    if not slide_files:
        print(f"  エラー: PNGファイルが見つかりません: {slide_dir}")
        sys.exit(1)
    print(f"  スライド: {len(slide_files)}個のPNG ({slide_dir.name}/)")

    # 読み上げファイル解析
    content = load_script(str(reading_script))
    slides_data = extract_slides_from_reading_script(content)
    print(f"  読み上げセクション: {len(slides_data)}個")

    # 数の一致確認
    counts = {
        "MP3": len(audio_files),
        "PNG": len(slide_files),
        "読み上げセクション": len(slides_data),
    }
    unique_counts = set(counts.values())

    if len(unique_counts) > 1:
        print(f"\n  警告: アセット数が一致しません:")
        for name, count in counts.items():
            print(f"    {name}: {count}")
        # 最小値に合わせてトリム
        min_count = min(counts.values())
        audio_files = audio_files[:min_count]
        slide_files = slide_files[:min_count]
        slides_data = slides_data[:min_count]
        print(f"  → {min_count}スライドに調整しました")
    else:
        print(f"  ✓ アセット数一致: {len(audio_files)}スライド")

    return {
        "reading_script": reading_script,
        "audio_dir": audio_dir,
        "audio_files": audio_files,
        "slide_files": slide_files,
        "slides_data": slides_data,
    }


def _extract_number(stem: str) -> int:
    """ファイル名から数字を抽出してソート用に返す"""
    match = re.search(r"(\d+)", stem)
    return int(match.group(1)) if match else 0


def calculate_frame_timings(audio_durations: list[float]) -> list[dict]:
    """
    [3/7] 各スライドのフレームタイミングを計算

    Returns:
        [{durationSec, durationFrames, startFrame, gapAfterFrames}, ...]
    """
    timings = []
    current_frame = 0

    for i, dur_sec in enumerate(audio_durations):
        duration_frames = math.ceil(dur_sec * FPS)
        is_last = i == len(audio_durations) - 1
        gap = 0 if is_last else GAP_AFTER_FRAMES

        timings.append({
            "durationSec": round(dur_sec, 2),
            "durationFrames": duration_frames,
            "startFrame": current_frame,
            "gapAfterFrames": gap,
        })

        current_frame += duration_frames + gap + AUDIO_DELAY_FRAMES

    return timings


def build_project_json(
    title: str,
    description: str,
    project_name: str,
    audio_dir_name: str,
    slides_data: list[dict],
    audio_files: list[Path],
    timings: list[dict],
    subtitles_list: list[list[dict]],
) -> dict:
    """
    [5/7] Remotion ProjectData型に準拠したJSON構築

    Returns:
        ProjectData dict
    """
    slides = []
    for i, (slide_data, audio_file, timing, subtitles) in enumerate(
        zip(slides_data, audio_files, timings, subtitles_list)
    ):
        slides.append({
            "id": i + 1,
            "image": f"{i + 1}.png",
            "audio": audio_file.name,
            "subtitles": subtitles,
            "durationSec": timing["durationSec"],
            "durationFrames": timing["durationFrames"],
            "startFrame": timing["startFrame"],
            "gapAfterFrames": timing["gapAfterFrames"],
        })

    # totalFrames = 最後のスライドの startFrame + durationFrames + AUDIO_DELAY
    last = timings[-1]
    total_frames = last["startFrame"] + last["durationFrames"] + AUDIO_DELAY_FRAMES
    total_duration_sec = total_frames / FPS

    project_data = {
        "meta": {
            "title": title,
            "description": description,
            "fps": FPS,
            "width": VIDEO_WIDTH,
            "height": VIDEO_HEIGHT,
            "totalFrames": total_frames,
            "totalDurationSec": total_duration_sec,
            "assetsPath": f"public/{project_name}/資料",
            "audioPath": f"public/{project_name}/音声/{audio_dir_name}",
        },
        "style": DEFAULT_STYLE,
        "slides": slides,
    }

    return project_data


def setup_remotion_assets(
    remotion_dir: Path,
    project_name: str,
    audio_dir_name: str,
    slide_files: list[Path],
    audio_files: list[Path],
    project_json: dict,
    dry_run: bool = False,
) -> dict:
    """
    [6/7] アセットをRemotionプロジェクトにコピー

    Returns:
        {project_dir, slides_dest, audio_dest, json_path}
    """
    public_dir = remotion_dir / "public" / project_name
    slides_dest = public_dir / "資料"
    audio_dest = public_dir / "音声" / audio_dir_name
    json_path = public_dir / f"{project_name}_project.json"

    if dry_run:
        return {
            "project_dir": public_dir,
            "slides_dest": slides_dest,
            "audio_dest": audio_dest,
            "json_path": json_path,
        }

    # ディレクトリ作成
    slides_dest.mkdir(parents=True, exist_ok=True)
    audio_dest.mkdir(parents=True, exist_ok=True)

    # スライドPNGコピー（リネーム: 1.png, 2.png, ...）
    for i, src in enumerate(slide_files, 1):
        dst = slides_dest / f"{i}.png"
        shutil.copy2(src, dst)

    # 音声MP3コピー（ファイル名そのまま）
    for src in audio_files:
        dst = audio_dest / src.name
        shutil.copy2(src, dst)

    # JSONを保存
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(project_json, f, ensure_ascii=False, indent=2)

    return {
        "project_dir": public_dir,
        "slides_dest": slides_dest,
        "audio_dest": audio_dest,
        "json_path": json_path,
    }


def generate_composition_tsx(
    component_name: str,
    project_name: str,
) -> str:
    """
    [7/7] コンポジションTSXファイルの内容を生成

    Returns:
        TSXファイルの内容
    """
    json_import_path = f"../public/{project_name}/{project_name}_project.json"

    tsx_content = f'''import React from "react";
import {{ AbsoluteFill, Sequence }} from "remotion";
import {{ z }} from "zod";
import {{ Slide }} from "./AICopyright/Slide";
import {{ ProjectData }} from "./AICopyright/types";
import projectData from "{json_import_path}";

const AUDIO_DELAY_FRAMES = 30; // 音声開始まで1秒の遅延

export const {_to_camel_case(component_name)}Schema = z.object({{}});

export const {component_name}: React.FC<z.infer<typeof {_to_camel_case(component_name)}Schema>> = () => {{
  const data = projectData as ProjectData;

  return (
    <AbsoluteFill style={{{{ backgroundColor: data.style.image.backgroundColor }}}}>
      {{data.slides.map((slide) => (
        <Sequence
          key={{slide.id}}
          from={{slide.startFrame}}
          durationInFrames={{slide.durationFrames + slide.gapAfterFrames + AUDIO_DELAY_FRAMES}}
        >
          <Slide
            slide={{slide}}
            style={{data.style}}
            assetsPath={{data.meta.assetsPath}}
            audioPath={{data.meta.audioPath}}
          />
        </Sequence>
      ))}}
    </AbsoluteFill>
  );
}};

export {{ projectData as {_to_camel_case(component_name)}ProjectData }};
'''
    return tsx_content


def _to_camel_case(name: str) -> str:
    """PascalCase名をcamelCaseに変換（先頭小文字）"""
    if not name:
        return name
    return name[0].lower() + name[1:]


def generate_root_snippet(component_name: str) -> tuple[str, str]:
    """Root.tsxに追記するコードスニペットを生成"""
    schema_name = _to_camel_case(component_name) + "Schema"
    data_name = _to_camel_case(component_name) + "ProjectData"

    import_line = (
        f'import {{ {component_name}, {schema_name}, {data_name} }} '
        f'from "./{component_name}";'
    )

    composition_block = f"""
      {{/* {component_name} */}}
      <Composition
        id="{component_name}"
        component={{{component_name}}}
        durationInFrames={{{data_name}.meta.totalFrames}}
        fps={{{data_name}.meta.fps}}
        width={{{data_name}.meta.width}}
        height={{{data_name}.meta.height}}
        schema={{{schema_name}}}
        defaultProps={{{{}}}}
      />"""

    return import_line, composition_block


# === CLI ===


def parse_arguments() -> argparse.Namespace:
    """コマンドライン引数をパース"""
    parser = argparse.ArgumentParser(
        description="BAA台本からRemotion用動画プロジェクトを生成",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  python generate_video.py --slide-dir ~/Canva/スライド/ --component-name SeiseiAI "作成済台本/概念系/生成AIとは何か"
  python generate_video.py --dry-run --slide-dir ~/Canva/スライド/ --component-name SeiseiAI
        """,
    )

    parser.add_argument(
        "topic_folder",
        nargs="?",
        help="トピックフォルダパス（省略時は対話式選択）",
    )

    parser.add_argument(
        "--slide-dir",
        required=True,
        help="スライドPNG画像フォルダ（Canva等で手動作成したもの）",
    )

    parser.add_argument(
        "--component-name",
        required=True,
        help="TSXコンポーネント名（英字PascalCase、例: SeiseiAI）",
    )

    parser.add_argument(
        "--project-name",
        help="Remotionプロジェクト名（省略時はトピック名から自動生成）",
    )

    parser.add_argument(
        "--remotion-dir",
        default=str(DEFAULT_REMOTION_DIR),
        help=f"Remotionプロジェクトパス（デフォルト: {DEFAULT_REMOTION_DIR}）",
    )

    parser.add_argument(
        "--description",
        help="動画説明文（省略時はタイトルから生成）",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="変更なしでプレビュー",
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="既存プロジェクトを上書き",
    )

    parser.add_argument(
        "--whisper-sync",
        action="store_true",
        help="Whisperで字幕タイミングを正確に同期（openai-whisper要）",
    )

    parser.add_argument(
        "--whisper-model",
        default="medium",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisperモデルサイズ（デフォルト: medium）",
    )

    return parser.parse_args()


def main():
    """メイン処理"""
    args = parse_arguments()

    # コンポーネント名のバリデーション
    if not re.match(r"^[A-Z][A-Za-z0-9]+$", args.component_name):
        print("エラー: --component-name はPascalCase英字で指定してください（例: SeiseiAI）")
        sys.exit(1)

    remotion_dir = Path(args.remotion_dir)
    if not remotion_dir.exists():
        print(f"エラー: Remotionプロジェクトが見つかりません: {remotion_dir}")
        sys.exit(1)

    # トピックフォルダを決定
    if args.topic_folder:
        topic_folder = Path(args.topic_folder)
        if not topic_folder.is_absolute():
            topic_folder = PROJECT_ROOT / topic_folder
    else:
        folders = find_topic_folders(PROJECT_ROOT)
        if not folders:
            print("エラー: 動画生成可能なトピックが見つかりません。")
            print("  読み上げ用ファイルと音声フォルダが必要です。")
            sys.exit(1)
        topic_folder = select_topic_interactive(folders, PROJECT_ROOT)
        if topic_folder is None:
            print("キャンセルしました。")
            sys.exit(0)

    if not topic_folder.exists():
        print(f"エラー: フォルダが見つかりません: {topic_folder}")
        sys.exit(1)

    # プロジェクト名を決定
    title = topic_folder.name
    project_name = args.project_name or title
    description = args.description or f"{title} - Build AI Academy"

    print(f"\n{'='*60}")
    print(f"BAA → Remotion 動画プロジェクト生成")
    print(f"{'='*60}")
    print(f"  トピック: {title}")
    print(f"  プロジェクト名: {project_name}")
    print(f"  コンポーネント: {args.component_name}")
    if args.dry_run:
        print(f"  モード: ドライラン（変更なし）")
    print()

    # 既存プロジェクトの確認
    project_public = remotion_dir / "public" / project_name
    tsx_path = remotion_dir / "src" / f"{args.component_name}.tsx"
    if not args.force and not args.dry_run:
        if project_public.exists():
            print(f"エラー: プロジェクトが既に存在します: {project_public}")
            print("  --force オプションで上書きできます。")
            sys.exit(1)
        if tsx_path.exists():
            print(f"エラー: コンポーネントが既に存在します: {tsx_path}")
            print("  --force オプションで上書きできます。")
            sys.exit(1)

    # [1/7] 入力検証・アセット検出
    assets = validate_and_discover(topic_folder, Path(args.slide_dir))

    # [2/7] 読み上げ用ファイル解析（validate_and_discoverで完了済み）
    print("\n[2/7] 読み上げ用ファイル解析...完了（ステップ1で取得済み）")
    for slide in assets["slides_data"]:
        preview = slide["text"][:40].replace("\n", " ")
        print(f"  スライド{slide['number']:02d}: {slide['title']} ({len(slide['text'])}文字)")

    # [3/7] 音声タイミング取得
    print(f"\n[3/7] 音声タイミング取得...")
    audio_durations = []
    for mp3 in assets["audio_files"]:
        dur = get_audio_duration(mp3)
        audio_durations.append(dur)
        print(f"  {mp3.name}: {dur:.2f}秒")

    timings = calculate_frame_timings(audio_durations)
    total_duration = sum(d for d in audio_durations)
    print(f"  合計: {total_duration:.1f}秒 ({total_duration/60:.1f}分)")

    # [4/7] 字幕セグメント生成
    print(f"\n[4/7] 字幕セグメント生成...")
    subtitles_list = []
    for slide_data, dur in zip(assets["slides_data"], audio_durations):
        subs = generate_estimated_subtitles(slide_data["text"], dur)
        subtitles_list.append(subs)
        print(f"  スライド{slide_data['number']:02d}: {len(subs)}セグメント")

    # [5/7] プロジェクトJSON生成
    print(f"\n[5/7] プロジェクトJSON生成...")
    audio_dir_name = assets["audio_dir"].name
    project_json = build_project_json(
        title=title,
        description=description,
        project_name=project_name,
        audio_dir_name=audio_dir_name,
        slides_data=assets["slides_data"],
        audio_files=assets["audio_files"],
        timings=timings,
        subtitles_list=subtitles_list,
    )
    print(f"  totalFrames: {project_json['meta']['totalFrames']}")
    print(f"  totalDurationSec: {project_json['meta']['totalDurationSec']:.1f}")
    print(f"  スライド数: {len(project_json['slides'])}")

    # [6/7] アセットコピー
    print(f"\n[6/7] アセットコピー...")
    paths = setup_remotion_assets(
        remotion_dir=remotion_dir,
        project_name=project_name,
        audio_dir_name=audio_dir_name,
        slide_files=assets["slide_files"],
        audio_files=assets["audio_files"],
        project_json=project_json,
        dry_run=args.dry_run,
    )

    if args.dry_run:
        print(f"  [ドライラン] コピー先:")
        print(f"    スライド: {paths['slides_dest']}")
        print(f"    音声: {paths['audio_dest']}")
        print(f"    JSON: {paths['json_path']}")
    else:
        print(f"  スライドPNG: {len(assets['slide_files'])}ファイル → {paths['slides_dest']}")
        print(f"  音声MP3: {len(assets['audio_files'])}ファイル → {paths['audio_dest']}")
        print(f"  JSON: {paths['json_path']}")

    # [7/7] コンポジションTSX生成
    print(f"\n[7/7] コンポジションTSX生成...")
    tsx_content = generate_composition_tsx(args.component_name, project_name)

    if args.dry_run:
        print(f"  [ドライラン] TSX出力先: {tsx_path}")
        print(f"\n--- {args.component_name}.tsx プレビュー ---")
        print(tsx_content)
    else:
        tsx_path.parent.mkdir(parents=True, exist_ok=True)
        tsx_path.write_text(tsx_content, encoding="utf-8")
        print(f"  保存: {tsx_path}")

    # [8/8] Whisper字幕同期（オプション）
    if args.whisper_sync and not args.dry_run:
        print(f"\n[8/8] Whisper字幕同期...")
        sync_subtitles_with_whisper(paths["json_path"], model_name=args.whisper_model)
    elif args.whisper_sync and args.dry_run:
        print(f"\n[8/8] [ドライラン] Whisper字幕同期はスキップ")

    # Root.tsx 追記コード表示
    import_line, composition_block = generate_root_snippet(args.component_name)

    print(f"\n{'='*60}")
    print("完了！")
    print(f"{'='*60}")

    if args.dry_run:
        print("\n[ドライラン] 実際のファイル変更はありません。")
        print("\n--- JSON構造プレビュー（先頭2スライド） ---")
        preview = dict(project_json)
        preview["slides"] = project_json["slides"][:2]
        print(json.dumps(preview, ensure_ascii=False, indent=2))
    else:
        print(f"\n生成されたファイル:")
        print(f"  1. {paths['json_path']}")
        print(f"  2. {paths['slides_dest']}/ ({len(assets['slide_files'])} PNG)")
        print(f"  3. {paths['audio_dest']}/ ({len(assets['audio_files'])} MP3)")
        print(f"  4. {tsx_path}")

    print(f"\n--- Root.tsx に以下を手動で追記してください ---")
    print(f"\n// import文（他のimportの後に追加）:")
    print(import_line)
    print(f"\n// Composition（</> の直前に追加）:")
    print(composition_block)

    if not args.dry_run:
        print(f"\n--- 次のステップ ---")
        print(f"  1. Root.tsx に上記のコードを追記")
        print(f"  2. cd \"{remotion_dir}\"")
        print(f"  3. npm run dev  （プレビュー確認）")
        print(f"  4. npx remotion render {args.component_name}  （動画レンダリング）")


if __name__ == "__main__":
    main()
