#!/usr/bin/env python3
"""
台本MDファイルからElevenLabs APIを使用してMP3音声を生成するCLIツール

使用方法:
    # 対話式選択
    python generate_audio.py

    # 直接指定
    python generate_audio.py "path/to/台本.md"

    # ドライラン（テキスト抽出のみ）
    python generate_audio.py --dry-run

    # スライドごとに音声生成（読み上げ用ファイル用）
    python generate_audio.py --per-slide
    python generate_audio.py --per-slide "path/to/【読み上げ用】〇〇.md"
    python generate_audio.py --per-slide --dry-run

    # 特定のスライドのみ再生成
    python generate_audio.py --per-slide --slide 1
    python generate_audio.py --per-slide --slide 1 --slide 3  # 複数指定可
    python generate_audio.py --per-slide --slide 1 "path/to/【読み上げ用】〇〇.md"
"""
import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# スクリプトのディレクトリをパスに追加
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from text_processor import (
    load_script,
    extract_narration,
    split_into_chunks,
    split_by_sections,
    extract_slides_from_reading_script,
    sanitize_filename,
)
from elevenlabs_client import ElevenLabsAudioGenerator, verify_api_key, ElevenLabsError


def find_script_files(base_dir: Path, pattern: str = "【台本】*.md") -> list[Path]:
    """
    作成済台本フォルダ内の指定パターンのファイルを検索

    Args:
        base_dir: 検索開始ディレクトリ
        pattern: 検索パターン（デフォルト: 【台本】*.md）

    Returns:
        ファイルのパスリスト
    """
    scripts_dir = base_dir / "作成済台本"
    if not scripts_dir.exists():
        return []

    # 指定パターンのMDファイルを検索
    script_files = list(scripts_dir.rglob(pattern))

    # パスでソート
    script_files.sort()

    return script_files


def find_reading_script_files(base_dir: Path) -> list[Path]:
    """
    作成済台本フォルダ内の【読み上げ用】ファイルを検索

    Args:
        base_dir: 検索開始ディレクトリ

    Returns:
        読み上げ用ファイルのパスリスト
    """
    return find_script_files(base_dir, pattern="【読み上げ用】*.md")


def display_file_list(files: list[Path], base_dir: Path, file_type: str = "台本") -> None:
    """
    ファイル一覧を表示

    Args:
        files: ファイルパスのリスト
        base_dir: 相対パス表示用の基準ディレクトリ
        file_type: ファイルタイプ名（表示用）
    """
    print(f"\n=== {file_type}ファイル一覧 ===\n")

    for i, file_path in enumerate(files, 1):
        relative_path = file_path.relative_to(base_dir / "作成済台本")
        # ファイル名を短縮表示
        display_name = str(relative_path)
        if len(display_name) > 70:
            display_name = display_name[:67] + "..."
        print(f"[{i}] {display_name}")

    print()


def select_file_interactive(files: list[Path], base_dir: Path, file_type: str = "台本") -> Path | None:
    """
    対話式でファイルを選択

    Args:
        files: ファイルパスのリスト
        base_dir: 相対パス表示用の基準ディレクトリ
        file_type: ファイルタイプ名（表示用）

    Returns:
        選択されたファイルパス、またはNone（キャンセル時）
    """
    display_file_list(files, base_dir, file_type)

    while True:
        try:
            user_input = input("番号を入力してください (q でキャンセル): ").strip()

            if user_input.lower() == 'q':
                return None

            selection = int(user_input)

            if 1 <= selection <= len(files):
                return files[selection - 1]
            else:
                print(f"1から{len(files)}の番号を入力してください。")

        except ValueError:
            print("数字を入力してください。")


def get_output_path(script_path: Path) -> Path:
    """
    出力ファイルパスを決定

    台本と同じフォルダに保存し、ファイル名は台本と同じ（拡張子をmp3に変更）

    Args:
        script_path: 台本ファイルのパス

    Returns:
        出力ファイルパス
    """
    # 台本ファイル名から【台本】プレフィックスを【音声】に変更
    stem = script_path.stem.replace("【台本】", "【音声】")
    return script_path.parent / f"{stem}.mp3"


def parse_arguments() -> argparse.Namespace:
    """コマンドライン引数をパース"""
    parser = argparse.ArgumentParser(
        description="台本MDファイルからMP3音声を生成",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  python generate_audio.py                    # 対話式選択
  python generate_audio.py "path/to/台本.md"  # 直接指定
  python generate_audio.py --dry-run          # テキスト抽出のみ
        """
    )

    parser.add_argument(
        "script_path",
        nargs="?",
        help="台本ファイルのパス（省略時は対話式選択）"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="テキスト抽出のみ実行（API呼び出しなし）"
    )

    parser.add_argument(
        "--max-chars",
        type=int,
        default=5000,
        help="チャンク分割の最大文字数（デフォルト: 5000）"
    )

    parser.add_argument(
        "--output", "-o",
        help="出力ファイルパス（省略時は台本と同じフォルダに保存）"
    )

    parser.add_argument(
        "--split",
        action="store_true",
        help="台本をセクションで2分割し、別々のMP3ファイルとして出力"
    )

    parser.add_argument(
        "--split-at",
        type=int,
        help="分割するセクション番号を指定（--splitと併用、このセクション以降が後半）"
    )

    parser.add_argument(
        "--per-slide",
        action="store_true",
        help="【読み上げ用】ファイルをスライドごとに分割して音声生成"
    )

    parser.add_argument(
        "--slide",
        type=int,
        action="append",
        help="特定のスライド番号のみ生成（--per-slideと併用、複数指定可）例: --slide 1 --slide 3"
    )

    return parser.parse_args()


def generate_split_audio(
    content: str,
    script_path: Path,
    args: argparse.Namespace,
    api_key: str,
    voice_id: str,
    model_id: str
) -> None:
    """
    台本をセクションで分割して、複数のMP3ファイルを生成

    Args:
        content: 台本の内容
        script_path: 台本ファイルのパス
        args: コマンドライン引数
        api_key: ElevenLabs APIキー
        voice_id: Voice ID
        model_id: モデルID
    """
    print("[2/5] 台本をセクションで分割中...")

    # セクションで分割
    parts = split_by_sections(content, split_point=args.split_at)

    if len(parts) < 2:
        print("警告: 分割できるセクションが見つかりませんでした。通常モードで実行してください。")
        sys.exit(1)

    print(f"  {len(parts)}つのパートに分割しました:")
    for part in parts:
        print(f"    パート{part['part']}: セクション {part['sections']} ({len(part['text'])}文字)")

    # ドライランの場合はここで終了
    if args.dry_run:
        print("\n=== ドライラン: 分割されたテキスト ===")
        for part in parts:
            print(f"\n--- パート{part['part']} (セクション {part['sections']}, {len(part['text'])}文字) ---")
            preview = part['text'][:300] + "..." if len(part['text']) > 300 else part['text']
            print(preview)
        return

    # API設定の確認
    if not api_key:
        print("エラー: ELEVENLABS_API_KEY が設定されていません。")
        sys.exit(1)

    if not voice_id:
        print("エラー: ELEVENLABS_VOICE_ID が設定されていません。")
        sys.exit(1)

    # APIキーの確認
    print("[3/5] APIキーを確認中...")
    if not verify_api_key(api_key):
        print("エラー: APIキーが無効です。設定を確認してください。")
        sys.exit(1)

    # 各パートの音声を生成
    generator = ElevenLabsAudioGenerator(api_key, voice_id, model_id)
    output_paths = []

    for part in parts:
        print(f"\n[4/5] パート{part['part']}の音声を生成中...")

        try:
            # チャンク分割（各パートも必要に応じて分割）
            chunks = split_into_chunks(part['text'], max_chars=args.max_chars)
            print(f"  {len(chunks)}個のチャンクに分割")

            audio_chunks = generator.generate_audio_chunks(chunks)

            # チャンクを結合
            if len(audio_chunks) > 1:
                print("  音声チャンクを結合中...")
                audio_data = generator.merge_audio_chunks(audio_chunks)
            else:
                audio_data = audio_chunks[0]

            # 出力パスを決定（パート番号を付与）
            stem = script_path.stem.replace("【台本】", "【音声】")
            output_path = script_path.parent / f"{stem}_part{part['part']}.mp3"
            output_paths.append(output_path)

            # ファイルを保存
            print(f"  保存中: {output_path.name}")
            generator.save_audio(audio_data, str(output_path))

        except ElevenLabsError as e:
            print(f"エラー: パート{part['part']}の音声生成に失敗しました: {e}")
            sys.exit(1)

    print(f"\n[5/5] 完了しました！")
    print(f"  生成されたファイル:")
    for path in output_paths:
        print(f"    - {path}")


def generate_per_slide_audio(
    content: str,
    script_path: Path,
    args: argparse.Namespace,
    api_key: str,
    voice_id: str,
    model_id: str
) -> None:
    """
    読み上げ用ファイルからスライドごとに個別のMP3ファイルを生成

    Args:
        content: 読み上げ用ファイルの内容
        script_path: 読み上げ用ファイルのパス
        args: コマンドライン引数
        api_key: ElevenLabs APIキー
        voice_id: Voice ID
        model_id: モデルID
    """
    print("[2/5] スライドごとにテキストを抽出中...")

    # スライドごとにテキストを抽出
    slides = extract_slides_from_reading_script(content)

    if not slides:
        print("エラー: スライドが見つかりませんでした。")
        print("  【読み上げ用】ファイルの形式を確認してください。")
        sys.exit(1)

    print(f"  {len(slides)}個のスライドを検出しました:")
    for slide in slides:
        preview = slide['text'][:30] + "..." if len(slide['text']) > 30 else slide['text']
        print(f"    スライド{slide['number']:02d}: {slide['title']} ({len(slide['text'])}文字)")

    # 特定スライドのみフィルタリング
    if args.slide:
        target_slides = [s for s in slides if s['number'] in args.slide]
        if not target_slides:
            print(f"エラー: 指定されたスライド番号 {args.slide} が見つかりません。")
            sys.exit(1)
        slides = target_slides
        print(f"\n  → スライド {args.slide} のみ生成します")

    # ドライランの場合はここで終了
    if args.dry_run:
        print("\n=== ドライラン: 抽出されたテキスト ===")
        for slide in slides:
            print(f"\n--- スライド{slide['number']:02d}: {slide['title']} ({len(slide['text'])}文字) ---")
            print(slide['text'])
        return

    # API設定の確認
    if not api_key:
        print("エラー: ELEVENLABS_API_KEY が設定されていません。")
        sys.exit(1)

    if not voice_id:
        print("エラー: ELEVENLABS_VOICE_ID が設定されていません。")
        sys.exit(1)

    # APIキーの確認
    print("[3/5] APIキーを確認中...")
    if not verify_api_key(api_key):
        print("エラー: APIキーが無効です。設定を確認してください。")
        sys.exit(1)

    # 各スライドの音声を生成
    generator = ElevenLabsAudioGenerator(api_key, voice_id, model_id)
    output_paths = []

    # 出力フォルダを作成
    # 【読み上げ用】YYYY-MM-DD_ジャンル_タイトル.md から
    # 【音声】YYYY-MM-DD_ジャンル_タイトル/ フォルダを作成
    base_stem = script_path.stem.replace("【読み上げ用】", "【音声】")
    output_dir = script_path.parent / base_stem
    output_dir.mkdir(exist_ok=True)

    print(f"[4/5] スライドごとに音声を生成中...")
    print(f"  出力先フォルダ: {output_dir.name}/")
    print(f"  設定: stability=1.0（一貫性重視）, style=0.5（テンション維持）")

    for i, slide in enumerate(slides, 1):
        print(f"\n  スライド{slide['number']:02d}/{len(slides)}: {slide['title']}...")

        try:
            # スライド単位で音声生成
            # stability=1.0で一貫性を最大化、style=0.5でテンションを維持
            audio_data = generator.generate_audio_with_retry(
                slide['text'],
                stability=1.0,
                similarity_boost=0.75,
                style=0.5
            )

            # 出力パスを決定
            # ファイル名に使えない文字を除去
            safe_title = sanitize_filename(slide['title'])
            output_filename = f"スライド{slide['number']:02d}_{safe_title}.mp3"
            output_path = output_dir / output_filename
            output_paths.append(output_path)

            # ファイルを保存
            generator.save_audio(audio_data, str(output_path))
            print(f"    保存: {output_path.name}")

        except ElevenLabsError as e:
            print(f"エラー: スライド{slide['number']}の音声生成に失敗しました: {e}")
            sys.exit(1)

    print(f"\n[5/5] 完了しました！")
    print(f"  生成されたファイル: {len(output_paths)}個")
    print(f"  保存先: {output_dir}")


def main():
    """メイン処理"""
    args = parse_arguments()

    # 環境変数を読み込み
    env_path = PROJECT_ROOT / ".env"
    if env_path.exists():
        load_dotenv(env_path)
    else:
        print("警告: .envファイルが見つかりません。")
        print(f"  {PROJECT_ROOT / '.env.example'} を参考に .env を作成してください。")

        if not args.dry_run:
            sys.exit(1)

    # API設定を取得
    api_key = os.getenv("ELEVENLABS_API_KEY", "")
    voice_id = os.getenv("ELEVENLABS_VOICE_ID", "")
    model_id = os.getenv("ELEVENLABS_MODEL_ID", "eleven_multilingual_v2")

    # --per-slide モードの場合は読み上げ用ファイルを検索
    if args.per_slide:
        file_type = "読み上げ用"
        file_pattern = "【読み上げ用】*.md"
    else:
        file_type = "台本"
        file_pattern = "【台本】*.md"

    # ファイルを決定
    if args.script_path:
        script_path = Path(args.script_path)
        if not script_path.is_absolute():
            script_path = PROJECT_ROOT / script_path
    else:
        # 対話式選択
        script_files = find_script_files(PROJECT_ROOT, pattern=file_pattern)

        if not script_files:
            print(f"エラー: {file_type}ファイルが見つかりませんでした。")
            print(f"  {PROJECT_ROOT / '作成済台本'} フォルダ内に{file_pattern}ファイルを配置してください。")
            sys.exit(1)

        script_path = select_file_interactive(script_files, PROJECT_ROOT, file_type)

        if script_path is None:
            print("キャンセルしました。")
            sys.exit(0)

    # ファイルの存在確認
    if not script_path.exists():
        print(f"エラー: ファイルが見つかりません: {script_path}")
        sys.exit(1)

    print(f"\n[1/5] {file_type}ファイルを読み込み中: {script_path.name}")

    # ファイルを読み込み
    try:
        content = load_script(str(script_path))
    except FileNotFoundError as e:
        print(f"エラー: {e}")
        sys.exit(1)

    # --per-slide モードの場合
    if args.per_slide:
        generate_per_slide_audio(content, script_path, args, api_key, voice_id, model_id)
        return

    # --split モードの場合
    if args.split:
        generate_split_audio(content, script_path, args, api_key, voice_id, model_id)
        return

    print("[2/5] ナレーションテキストを抽出中...")

    # ナレーション抽出
    narration = extract_narration(content)

    if not narration:
        print("エラー: ナレーションテキストを抽出できませんでした。")
        sys.exit(1)

    print(f"  抽出完了: {len(narration)}文字")

    # チャンク分割
    chunks = split_into_chunks(narration, max_chars=args.max_chars)
    print(f"[3/5] {len(chunks)}個のチャンクに分割しました")

    # ドライランの場合はここで終了
    if args.dry_run:
        print("\n=== ドライラン: 抽出されたテキスト ===\n")
        print(narration)
        print(f"\n=== 文字数: {len(narration)} / チャンク数: {len(chunks)} ===")
        return

    # API設定の確認
    if not api_key:
        print("エラー: ELEVENLABS_API_KEY が設定されていません。")
        print("  .env ファイルに API キーを設定してください。")
        sys.exit(1)

    if not voice_id:
        print("エラー: ELEVENLABS_VOICE_ID が設定されていません。")
        print("  .env ファイルに Voice ID を設定してください。")
        sys.exit(1)

    # APIキーの確認
    print("[4/5] 音声を生成中...")

    if not verify_api_key(api_key):
        print("エラー: APIキーが無効です。設定を確認してください。")
        sys.exit(1)

    # 音声生成
    try:
        generator = ElevenLabsAudioGenerator(api_key, voice_id, model_id)
        audio_chunks = generator.generate_audio_chunks(chunks)

        # チャンクを結合
        if len(audio_chunks) > 1:
            print("  音声チャンクを結合中...")
            audio_data = generator.merge_audio_chunks(audio_chunks)
        else:
            audio_data = audio_chunks[0]

    except ElevenLabsError as e:
        print(f"エラー: 音声生成に失敗しました: {e}")
        sys.exit(1)

    # 出力パスを決定
    if args.output:
        output_path = Path(args.output)
        if not output_path.is_absolute():
            output_path = PROJECT_ROOT / output_path
    else:
        output_path = get_output_path(script_path)

    # ファイルを保存
    print(f"[5/5] ファイルを保存中: {output_path.name}")
    generator.save_audio(audio_data, str(output_path))

    print(f"\n完了しました！")
    print(f"  保存先: {output_path}")


if __name__ == "__main__":
    main()
