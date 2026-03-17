"""
台本MDファイルからナレーションテキストを抽出するモジュール
"""
import re
from pathlib import Path


def load_script(file_path: str) -> str:
    """
    Markdownファイルを読み込む

    Args:
        file_path: 台本ファイルのパス

    Returns:
        ファイルの内容
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"ファイルが見つかりません: {file_path}")

    return path.read_text(encoding="utf-8")


def extract_narration(markdown_text: str) -> str:
    """
    台本からナレーション部分のみを抽出する

    処理内容:
    1. 【スタート】〜【終わり】の範囲を特定
    2. マーカー自体を除外（マーカー後のテキストは残す）
    3. ## 見出し行を除外
    4. （画面：○○）パターンを除外
    5. 表形式（| ... | ... |）を除外
    6. ※注意：ブロックを除外
    7. **強調**のMarkdown記法を除外（テキストは残す）
    8. 箇条書き記号を除外（テキストは残す）
    9. 空行の正規化

    Args:
        markdown_text: 台本のMarkdownテキスト

    Returns:
        抽出されたナレーションテキスト
    """
    # 【スタート】〜【終わり】の範囲を抽出（DOTALL で複数行にまたがるマッチ）
    match = re.search(r'【スタート】(.*?)【終わり】', markdown_text, re.DOTALL)

    if match:
        # 【スタート】の後のテキスト + 中間部分 + 【終わり】の前のテキスト
        text = match.group(0)
        # 【スタート】と【終わり】マーカーを除去
        text = text.replace('【スタート】', '')
        text = text.replace('【終わり】', '')
    else:
        # マーカーが見つからない場合は全文を対象とする
        print("警告: 【スタート】【終わり】マーカーが見つかりませんでした。全文を対象とします。")
        text = markdown_text

    # ## 見出し行からタイトル部分のみを抽出（例: "## 1. オープニング" → "オープニング"）
    # 番号付き見出し（## 1. タイトル, ### ステップ1：タイトル など）
    text = re.sub(r'^#{1,6}\s+\d+\.\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'^#{1,6}\s+ステップ\d+[：:]\s*', '', text, flags=re.MULTILINE)
    # 番号なし見出し（## タイトル）
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)

    # （画面：○○）パターンを除去
    text = re.sub(r'（画面：[^）]*）', '', text)

    # 表形式を除去（| で始まり | で終わる行）
    text = re.sub(r'^\|.*\|$', '', text, flags=re.MULTILINE)

    # ※注意：で始まるブロックを除去（次の空行または見出しまで）
    text = re.sub(r'※注意：.*?(?=\n\n|\n#|\Z)', '', text, flags=re.DOTALL)

    # **強調** または __強調__ を除去（テキストは残す）
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'__([^_]+)__', r'\1', text)

    # 箇条書き記号を除去（- または * で始まる行のマーカーのみ）
    text = re.sub(r'^[-*]\s+', '', text, flags=re.MULTILINE)

    # 番号付きリスト記号を除去（1. 2. など）
    text = re.sub(r'^\d+\.\s+', '', text, flags=re.MULTILINE)

    # テキストをクリーニング
    text = clean_text(text)

    return text


def clean_text(text: str) -> str:
    """
    テキストのクリーニング処理

    Args:
        text: クリーニング対象のテキスト

    Returns:
        クリーニング後のテキスト
    """
    # 連続する空行を1つにまとめる
    text = re.sub(r'\n{3,}', '\n\n', text)

    # 前後の空白をトリム
    text = text.strip()

    return text


def split_by_sections(markdown_text: str, split_point: int | None = None) -> list[dict]:
    """
    台本をセクション（## 見出し）で分割する

    Args:
        markdown_text: 台本のMarkdownテキスト
        split_point: 分割するセクション番号（この番号以降が後半になる）
                    Noneの場合は中間で自動分割

    Returns:
        分割されたパーツのリスト。各パーツは {'part': int, 'sections': str, 'text': str} の辞書
    """
    # 【スタート】〜【終わり】の範囲を抽出
    match = re.search(r'【スタート】(.*?)【終わり】', markdown_text, re.DOTALL)

    if match:
        text = match.group(0)
    else:
        text = markdown_text

    # セクション（## で始まる行）で分割
    # パターン: ## の前で分割（最初の部分を除く）
    sections = re.split(r'(?=\n## \d+\.)', text)

    # 空のセクションを除去
    sections = [s.strip() for s in sections if s.strip()]

    if not sections:
        return [{'part': 1, 'sections': 'all', 'text': text}]

    # 分割ポイントを決定
    if split_point is None:
        # 中間で分割（セクション数の半分）
        split_point = len(sections) // 2 + 1

    # 前半と後半に分割
    first_half = sections[:split_point]
    second_half = sections[split_point:]

    result = []

    if first_half:
        first_text = '\n\n'.join(first_half)
        # マーカーを除去してクリーニング
        first_text = first_text.replace('【スタート】', '').replace('【終わり】', '')
        first_text = clean_narration(first_text)
        result.append({
            'part': 1,
            'sections': f'1-{split_point}',
            'text': first_text
        })

    if second_half:
        second_text = '\n\n'.join(second_half)
        second_text = second_text.replace('【スタート】', '').replace('【終わり】', '')
        second_text = clean_narration(second_text)
        result.append({
            'part': 2,
            'sections': f'{split_point + 1}-{len(sections)}',
            'text': second_text
        })

    return result


def clean_narration(text: str) -> str:
    """
    ナレーションテキストをクリーニングする（extract_narrationと同様の処理）

    Args:
        text: クリーニング対象のテキスト

    Returns:
        クリーニング後のテキスト
    """
    # ## 見出し行からタイトル部分のみを抽出
    text = re.sub(r'^#{1,6}\s+\d+\.\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'^#{1,6}\s+ステップ\d+[：:]\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)

    # （画面：○○）パターンを除去
    text = re.sub(r'（画面：[^）]*）', '', text)

    # 表形式を除去
    text = re.sub(r'^\|.*\|$', '', text, flags=re.MULTILINE)

    # ※注意：で始まるブロックを除去
    text = re.sub(r'※注意：.*?(?=\n\n|\n#|\Z)', '', text, flags=re.DOTALL)

    # **強調** を除去（テキストは残す）
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'__([^_]+)__', r'\1', text)

    # 箇条書き記号を除去
    text = re.sub(r'^[-*]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\d+\.\s+', '', text, flags=re.MULTILINE)

    # テキストをクリーニング
    text = clean_text(text)

    return text


def extract_slides_from_reading_script(markdown_text: str) -> list[dict]:
    """
    読み上げ用ファイルからスライドごとにテキストを抽出

    処理内容:
    1. `---` で区切られたセクションを分割
    2. 各セクションから `## スライドN: タイトル` を解析してスライド番号とタイトルを取得
    3. 見出し行を除去し、本文のみを抽出
    4. 空のスライド（タイトルのみ等）はスキップ

    Args:
        markdown_text: 読み上げ用ファイルのMarkdownテキスト

    Returns:
        スライド情報のリスト。各要素は {'number': int, 'title': str, 'text': str} の辞書
    """
    # --- で区切られたセクションを分割
    sections = re.split(r'\n---\n', markdown_text)

    slides = []

    for section in sections:
        section = section.strip()
        if not section:
            continue

        # ## スライドN: タイトル のパターンを検索
        match = re.search(r'^##\s*スライド(\d+)[：:]\s*(.+)$', section, re.MULTILINE)

        if not match:
            # スライド見出しがない場合はスキップ（ヘッダー部分など）
            continue

        slide_number = int(match.group(1))
        slide_title = match.group(2).strip()

        # 見出し行を除去して本文のみを取得
        text = section

        # ## スライドN: タイトル の見出し行を除去
        text = re.sub(r'^##\s*スライド\d+[：:].+$', '', text, flags=re.MULTILINE)

        # 【事例N】などのサブ見出し行を除去
        text = re.sub(r'^【事例[^】]*】.+$', '', text, flags=re.MULTILINE)
        # 【スタート】【終わり】マーカーのみ除去（後続テキストは残す）
        text = re.sub(r'【(スタート|終わり)】', '', text)

        # ①②③などの番号付き見出しの行頭記号を除去（テキストは残す）
        text = re.sub(r'^[①②③④⑤⑥⑦⑧⑨⑩]\s*', '', text, flags=re.MULTILINE)

        # 番号付きリスト（1. 2. 3.）を除去（テキストは残す）
        text = re.sub(r'^\d+\.\s+', '', text, flags=re.MULTILINE)

        # テキストをクリーニング
        text = clean_text(text)

        # 空のスライドはスキップ
        if not text:
            continue

        slides.append({
            'number': slide_number,
            'title': slide_title,
            'text': text
        })

    return slides


def sanitize_filename(name: str) -> str:
    """
    ファイル名に使えない文字を除去・置換する

    Args:
        name: ファイル名にしたい文字列

    Returns:
        サニタイズ後の文字列
    """
    # ファイル名に使えない文字を除去・置換
    # Windows/Mac/Linux共通で使えない文字: / \ : * ? " < > |
    invalid_chars = r'[/\\:*?"<>|]'
    sanitized = re.sub(invalid_chars, '', name)

    # 先頭・末尾の空白を除去
    sanitized = sanitized.strip()

    # 空になった場合はデフォルト値
    if not sanitized:
        sanitized = 'untitled'

    return sanitized


def split_into_chunks(text: str, max_chars: int = 5000) -> list[str]:
    """
    テキストを指定文字数以下のチャンクに分割

    文末（。！？）で区切り、max_charsを超えないように分割する

    Args:
        text: 分割対象のテキスト
        max_chars: 1チャンクの最大文字数（デフォルト5000）

    Returns:
        チャンクのリスト
    """
    if len(text) <= max_chars:
        return [text]

    chunks = []
    current_chunk = ""

    # 文末で分割（。！？の後で分割）
    sentences = re.split(r'(?<=[。！？])', text)

    for sentence in sentences:
        if not sentence:
            continue

        # 現在のチャンクに追加しても上限を超えない場合
        if len(current_chunk) + len(sentence) <= max_chars:
            current_chunk += sentence
        else:
            # 現在のチャンクを保存し、新しいチャンクを開始
            if current_chunk:
                chunks.append(current_chunk.strip())

            # 1文が上限を超える場合は強制分割
            if len(sentence) > max_chars:
                # 段落（改行）で分割を試みる
                paragraphs = sentence.split('\n')
                for para in paragraphs:
                    if len(para) <= max_chars:
                        if current_chunk and len(current_chunk) + len(para) + 1 <= max_chars:
                            current_chunk += '\n' + para
                        else:
                            if current_chunk:
                                chunks.append(current_chunk.strip())
                            current_chunk = para
                    else:
                        # それでも長い場合は文字数で強制分割
                        if current_chunk:
                            chunks.append(current_chunk.strip())
                        for i in range(0, len(para), max_chars):
                            chunks.append(para[i:i+max_chars].strip())
                        current_chunk = ""
            else:
                current_chunk = sentence

    # 最後のチャンクを追加
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


if __name__ == "__main__":
    # テスト用
    import sys

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        content = load_script(file_path)
        narration = extract_narration(content)
        print("=== 抽出されたナレーション ===")
        print(narration)
        print(f"\n=== 文字数: {len(narration)} ===")

        chunks = split_into_chunks(narration)
        print(f"=== チャンク数: {len(chunks)} ===")
        for i, chunk in enumerate(chunks, 1):
            print(f"\n--- チャンク {i} ({len(chunk)}文字) ---")
            print(chunk[:200] + "..." if len(chunk) > 200 else chunk)
