# スライド詳細設計書（v2形式）

## 講座情報

```yaml
title: "NotebookLMで建材カタログを活用する方法"
target: "住宅会社の営業担当・設計担当"
duration: "10〜15分"
slide_count: 17
```

---

## スライド一覧

---

# スライド1: タイトル

```yaml
layout:
  type: "中央配置"
  logo_position: "左上"

copy:
  main_title: "NotebookLMで建材カタログを活用する方法"
  sub_title: "カタログをめくる日々からおさらば"
  badge_difficulty: "初心者向け"
  badge_date: "2025年12月版"

visual:
  logo: "Build AI Academy"
  main_image:
    description: "分厚いカタログの山と、スマートフォン/PCを操作する営業担当"
    style: "明るく前向きな雰囲気"

notes:
  - "カタログは3〜4冊積み重ねたイメージ"
  - "営業担当は笑顔でPCを操作している"
```

---

# スライド2: こんな経験ありませんか？

```yaml
layout:
  type: "中央イラスト＋周囲吹き出し"
  bubble_count: 3
  bubble_position: "around_center"

copy:
  heading: "こんな経験ありませんか？"
  bubbles:
    - "「この建材の仕様ってどうなってるんだっけ？」と聞かれて、数百ページのカタログをパラパラ…"
    - "見積もり作成時に「この単価どうだっけ？」と分厚いカタログを引っ張り出す"
    - "営業が設計に聞きに行って、設計もカタログを確認…二度手間が発生"
  bottom_message: "課題の本質は「必要な情報にすぐアクセスできない」こと"

visual:
  center_image:
    description: "困っている営業担当"
    details: "頭の上に「？」マーク、周囲に分厚いカタログが積まれている"
  bubbles:
    style: "吹き出し（白背景・グレー枠）"
  bottom_message:
    style: "強調枠（濃い背景色）"

notes:
  - "人物は汗マークや困り眉で「困っている感」を出す"
  - "カタログは実際の建材カタログをイメージ"
```

---

# スライド3: その悩み、NotebookLMで解決できます

```yaml
layout:
  type: "中央配置（強調メッセージ）"
  flow_direction: "horizontal"

copy:
  main_message: "AIにカタログを読み込ませれば、質問するだけで情報が見つかる"
  sub_message: "Googleが提供する無料AIツール「NotebookLM」を活用"
  bottom_keywords:
    - "専門知識不要"
    - "PDFをアップロードするだけ"
    - "無料で使える"

visual:
  flow:
    - element: "困った顔の人物"
    - arrow: true
    - element: "NotebookLMロゴ"
    - arrow: true
    - element: "笑顔の人物"
  bottom_message:
    style: "強調枠"
    separator: "・"

notes:
  - "メインメッセージは大きく太字"
  - "フローの矢印は右向き、グラデーションで変化を表現"
```

---

# スライド4: この動画でわかること

```yaml
layout:
  type: "チェックリスト形式"
  image_position: "right"

copy:
  heading: "この動画でわかること"
  checklist:
    - "NotebookLMの基本的な使い方"
    - "建材カタログの情報を瞬時に検索する方法"
    - "掛け率を設定して概算計算を自動化する方法"
    - "無料版と有料版の違い"
  bottom_message: "初めての方でも、動画を見ながら一緒に操作できます"

visual:
  checklist:
    icon: "checkmark"
    color: "green"
  side_image:
    description: "NotebookLM画面イメージ"
    type: "screenshot"
  bottom_message:
    style: "強調枠"

notes:
  - "チェックマークは緑色で統一"
  - "各項目は太字強調"
```

---

# スライド5: NotebookLMとは？

```yaml
layout:
  type: "左右分割"
  left: "テキスト説明"
  right: "画面キャプチャ"

copy:
  heading: "NotebookLMとは？"
  items:
    - label: "ツール名"
      text: "NotebookLM（ノートブックエルエム）"
    - label: "提供元"
      text: "Google"
    - label: "概要"
      text: "PDFなどの資料を読み込んで、その内容について質問できるAIツール"
    - label: "特徴"
      text: "アップロードした資料の中だけを参照して回答（ハルシネーションが少ない）"
  bottom_message: "「自分専用のAIアシスタント」を作るイメージ"

visual:
  left:
    logo: "NotebookLMロゴ"
  right:
    type: "screenshot"
    description: "NotebookLMの画面キャプチャ"

notes:
  - "ツール名は太字強調"
  - "画面キャプチャは最新版を使用"
```

---

# スライド6: NotebookLM基本情報

```yaml
layout:
  type: "カード形式"
  card_count: 5
  card_style: "アイコン付き横並び"

copy:
  heading: "NotebookLM基本情報"
  cards:
    - label: "料金"
      text: "無料（有料版は月額2,900円）"
    - label: "対応形式"
      text: "PDF、Googleドキュメント、テキスト、URLなど"
    - label: "ソース上限"
      text: "1ノートブックあたり最大50個"
    - label: "文字数上限"
      text: "1ソースあたり最大50万語"
    - label: "ファイルサイズ"
      text: "最大200MB"
  bottom_message: "300ページ超のカタログも読み込み可能"

visual:
  cards:
    - icon: "yen"
    - icon: "document"
    - icon: "chart"
    - icon: "text"
    - icon: "storage"

notes:
  - "アイコンはフラットデザイン"
  - "「無料」は太字強調"
```

---

# スライド7: 活用メリット（3つ）

```yaml
layout:
  type: "アイコン横並び"
  columns: 3
  center_element: true

copy:
  heading: "活用メリット（3つ）"
  items:
    - label: "①"
      title: "情報検索が瞬時に完了"
      text: "質問するだけでAIが回答"
    - label: "②"
      title: "概算計算が自動化"
      text: "掛け率を設定して自動計算"
    - label: "③"
      title: "営業・設計の工数削減"
      text: "二度手間がなくなる"
  bottom_message: "これから各メリットを詳しく紹介します"

visual:
  center_element:
    text: "NotebookLM × 建材カタログ"
    style: "中央配置・背景色付き"
  items:
    - icon: "search"
    - icon: "calculator"
    - icon: "clock"

notes:
  - "中央に「NotebookLM × 建材カタログ」を配置"
  - "周囲に3つのメリットを放射状に配置"
```

---

# スライド8: メリット① 情報検索が瞬時に完了

```yaml
layout:
  type: "左右2分割"
  left: "Before"
  right: "After"
  divider: "center_arrow"

copy:
  heading: "メリット① 情報検索が瞬時に完了"
  before:
    title: "Before"
    points:
      - "数百ページのカタログを手作業で検索"
      - "お客様を待たせてしまう…"
  after:
    title: "After"
    points:
      - "「この型番の単価は？」と質問するだけ"
      - "お客様をお待たせしない！"
  bottom_message: "何百ページあっても、AIが一瞬で該当箇所を見つけてくれる"

visual:
  before:
    image_description: "汗をかきながらカタログをめくる人"
    tone: "暗め・困っている表情"
  after:
    image_description: "笑顔でPCを操作する人"
    tone: "明るめ・満足している表情"
  bottom_message:
    style: "強調枠"

notes:
  - "Beforeは暗め、Afterは明るめの色調で対比"
  - "中央に矢印を配置"
```

---

# スライド9: メリット② 概算計算が自動化される

```yaml
layout:
  type: "フロー図中心"
  flow_direction: "horizontal"
  steps: 3

copy:
  heading: "メリット② 概算計算が自動化される"
  steps:
    - number: "1"
      text: "メーカーごとの掛け率を事前に設定"
      detail: "例：TOTO 60%、LIXIL 55%"
    - number: "2"
      text: "「TOTOで計算して」と質問"
      detail: ""
    - number: "3"
      text: "AIが掛け率を適用して概算を自動計算"
      detail: ""
  bottom_message: "電卓を叩く手間も削減！すぐに見積もり作成が可能"

visual:
  flow:
    - step: 1
      icon: "settings"
    - arrow: true
    - step: 2
      icon: "chat"
    - arrow: true
    - step: 3
      icon: "calculator"
  bottom_message:
    style: "強調枠"

notes:
  - "各ステップは番号付きで視覚的に区切る"
  - "矢印は右向き"
```

---

# スライド10: メリット③ 営業と設計の工数が大幅に削減

```yaml
layout:
  type: "左右2分割"
  left: "Before"
  right: "After"
  divider: "center_arrow"

copy:
  heading: "メリット③ 営業と設計の工数が大幅に削減"
  before:
    title: "Before"
    points:
      - "営業「この仕様わかります？」"
      - "設計「ちょっと待ってね…」（カタログ確認）"
      - "二度手間で両者の時間をロス"
  after:
    title: "After"
    points:
      - "営業が自分で検索して即回答"
      - "設計は本来の設計業務に集中"
      - "チーム全体の生産性が向上"
  bottom_message: "お互いが本来の業務に集中できる"

visual:
  before:
    image_description: "営業と設計が行き来するイラスト"
    tone: "慌ただしい雰囲気"
  after:
    image_description: "各自がPCで作業するイラスト"
    tone: "落ち着いた雰囲気"
  bottom_message:
    style: "強調枠"

notes:
  - "Beforeは2人が行き来している様子"
  - "Afterは各自が自席で集中している様子"
```

---

# スライド11: 汎用的に色々な場面で使える

```yaml
layout:
  type: "放射状配置"
  center: "NotebookLM"
  items_count: 5

copy:
  heading: "汎用的に色々な場面で使える"
  items:
    - title: "建材カタログ"
      text: "今回のメインテーマ"
    - title: "設備マニュアル"
      text: "機器の操作方法を検索"
    - title: "施工手順書"
      text: "施工手順を確認"
    - title: "社内業務マニュアル"
      text: "社内ルールを検索"
    - title: "仕様書"
      text: "詳細仕様を確認"
  bottom_message: "あらゆる文書をAIに読み込ませて、情報検索を効率化"

visual:
  center:
    element: "NotebookLMロゴ"
    style: "大きめ・中央配置"
  items:
    - icon: "book_red"
    - icon: "book_green"
    - icon: "book_blue"
    - icon: "book_orange"
    - icon: "notebook"
  bottom_message:
    style: "強調枠"

notes:
  - "中央にNotebookLMロゴ、周囲に5つの活用例を放射状に配置"
  - "各アイコンは色違いの本で区別"
```

---

# スライド12: 【実演】無料版での基本的な使い方

```yaml
layout:
  type: "左右分割"
  left: "手順リスト"
  right: "画面イメージ"

copy:
  heading: "【実演】無料版での基本的な使い方"
  steps:
    - "ブラウザでNotebookLMにアクセス"
    - "新しいノートブックを作成"
    - "左端の「ソース」ボタンをクリック"
    - "建材カタログのPDFをアップロード"
    - "「この型番の商品単価は？」と質問"
  note: "※実際の画面で実演します（容量が大きい場合は5分程度待つ）"

visual:
  right:
    type: "screenshot_placeholder"
    description: "NotebookLM操作画面"
  steps:
    style: "番号付きリスト"

notes:
  - "実演で補完されるため簡潔に"
  - "詳細な画面説明は不要"
```

---

# スライド13: 【実演】有料版での高度な使い方（カスタム機能）

```yaml
layout:
  type: "左右分割"
  left: "手順リスト"
  right: "画面イメージ"

copy:
  heading: "【実演】有料版での高度な使い方（カスタム機能）"
  steps:
    - "チャット欄右上の調節アイコン（3本線）をクリック"
    - "「カスタム」を選択"
    - "メーカーごとの掛け率を記載（例：TOTOは定価の60%で計算）"
    - "「TOTOで計算して」と質問"
    - "設定した掛け率を基に概算が出力される"
  note: "※有料版はGoogle One AIプレミアム（月額2,900円）に含まれています"

visual:
  right:
    type: "screenshot_placeholder"
    description: "カスタム設定画面"
  steps:
    style: "番号付きリスト"

notes:
  - "実演で補完されるため簡潔に"
  - "カスタム画面のUIをキャプチャ予定"
```

---

# スライド14: NotebookLMの制限事項

```yaml
layout:
  type: "カード形式"
  card_count: 5
  card_style: "アイコン付き縦並び"

copy:
  heading: "NotebookLMの制限事項"
  cards:
    - label: "ソース数"
      text: "1ノートブックあたり最大50個"
    - label: "文字数"
      text: "1ソースあたり最大50万語"
    - label: "ファイルサイズ"
      text: "最大200MB"
    - label: "チャット回数"
      text: "無料版は1日50回まで（有料版は500回）"
    - label: "カスタム指示"
      text: "有料版のみ（最大10,000文字まで設定可能）"
  bottom_message: "300ページ超のカタログも余裕で読み込めます"

visual:
  cards:
    - icon: "document"
    - icon: "text"
    - icon: "storage"
    - icon: "chat"
    - icon: "clock"
  header:
    icon: "info_circle"
    style: "情報アイコン（青）"

notes:
  - "制限事項だが「問題なく使える」という安心感を与える"
  - "下部メッセージでポジティブに締める"
```

---

# スライド15: 職種別おすすめの使い方

```yaml
layout:
  type: "カード横並び"
  columns: 3

copy:
  heading: "職種別おすすめの使い方"
  cards:
    - role: "営業担当"
      text: "商談中にお客様からの質問にその場で回答。見積もり時の単価確認も瞬時に"
    - role: "設計担当"
      text: "建材の仕様・寸法・納まりを即検索。複数メーカーの比較も簡単に"
    - role: "事務担当"
      text: "発注時の型番確認、見積もり作成時のデータ収集を効率化"
  bottom_message: "どの職種でも「カタログをめくる時間」を大幅削減"

visual:
  cards:
    - icon: "businessperson"
      color: "navy"
    - icon: "architect"
      color: "navy"
    - icon: "office_worker"
      color: "navy"
  bottom_message:
    style: "強調枠"

notes:
  - "各職種のイラストまたはアイコンを使用"
  - "職種名は太字強調"
```

---

# スライド16: まとめ

```yaml
layout:
  type: "カード横並び"
  columns: 4
  card_style: "フラット塗り"

copy:
  heading: "まとめ"
  cards:
    - label: "①"
      text: "情報検索が瞬時に完了（質問するだけでAIが回答）"
    - label: "②"
      text: "概算計算が自動化（掛け率を設定して自動計算）"
    - label: "③"
      text: "営業・設計の工数削減（二度手間がなくなる）"
    - label: "④"
      text: "汎用的に活用可能（マニュアル・仕様書・社内資料にも）"
  cta:
    prefix: "🚀"
    text: "ぜひ普段お使いのカタログをNotebookLMに取り込んで、情報検索の効率化を体験してみてください！"

visual:
  cards:
    - icon: "search"
    - icon: "calculator"
    - icon: "clock"
    - icon: "repeat"
  cta:
    style: "強調枠"

notes:
  - "各カードはフラット塗りアイコン"
  - "色はネイビー基調、アクセントはオレンジ"
```

---

# スライド17: エンディング

```yaml
layout:
  type: "中央配置"
  simple: true

copy:
  main_message: "ご視聴ありがとうございました"
  sub_message: "次回の講座でお会いしましょう"
  supplement: "NotebookLMの詳しい操作方法は別途解説動画をご用意しています"

visual:
  logo: "Build AI Academy"
  style: "シンプル・クリーン"

notes:
  - "シンプルに"
  - "ロゴは中央下部に配置"
```

---

## イラスト・図解の調達方法

| 種類 | 調達先 | 用途 |
|-----|--------|------|
| 人物イラスト | いらすとや、ソコスト | 課題提起、Before/After比較 |
| アイコン | Lucide、PowerPoint内蔵 | メリット説明、ポイント一覧 |
| 画面キャプチャ | NotebookLM実際の画面 | 実演スライド、ツール紹介 |
| ロゴ | NotebookLM公式サイト | タイトル、ツール紹介 |
| フロー図 | PowerPoint図形で作成 | 概算計算のフロー |

---

## チェックリスト

### 基本チェック
- [x] すべてのスライドにタイトルがある
- [x] すべてのスライドにVISUAL要素が指定されている
- [x] COPYの情報量が適切（5〜7行以内）
- [x] 重要キーワードに強調指定がある

### 3ブロック分離チェック（混入防止）
- [x] COPYに「レイアウト」「図解」「アイコン」「配置」等の指示語が含まれていない
- [x] COPYに「左/右に配置」「〜形式」等の配置指示が含まれていない
- [x] VISUALに「〜です」「〜ます」等の文章表現が含まれていない
- [x] LAYOUTに表示テキストやアイコン名が含まれていない

### 詳細化チェック
- [x] 導入部分が詳細化されている
- [x] 機能紹介が個別スライドに分割されている
- [x] 活用例がシーン別に分割されている
- [x] 実演部分は簡素になっている

### 住宅業界向けチェック
- [x] 住宅業界での活用イメージが含まれている
- [x] 職種別おすすめを含めている
- [x] Before/Afterで現場の変化がわかる

### まとめチェック
- [x] まとめスライドで要点が4つに集約されている
- [x] 行動を促すCTA（Call To Action）がある
