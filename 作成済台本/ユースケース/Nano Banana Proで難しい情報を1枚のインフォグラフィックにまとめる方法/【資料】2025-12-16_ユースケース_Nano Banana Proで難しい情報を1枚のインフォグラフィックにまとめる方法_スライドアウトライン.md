# スライド詳細設計書

## 講座情報

```yaml
title: "Nano Banana Proで難しい情報を1枚のインフォグラフィックにまとめる方法"
target: "住宅・建設会社の社員（営業、事務、現場監督など）"
duration: "約12分"
slide_count: 18
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
  main_title: "Nano Banana Proで難しい情報を1枚のインフォグラフィックにまとめる方法"
  sub_title: "難しい情報を1枚の絵でスッキリ伝える"
  badge_difficulty: "初心者向け"
  badge_date: "2025年12月版"

visual:
  logo: "Build AI Academy"
  main_image:
    description: "インフォグラフィックのサンプル画像と家族のイラスト"

notes:
  - "Nano Banana Proのロゴも配置"
```

---

# スライド2: こんな経験ありませんか？

```yaml
layout:
  type: "中央イラスト＋周囲吹き出し"
  bubble_count: 3

copy:
  heading: "こんな経験ありませんか？"
  bubbles:
    - "補助金の説明をしても、お客様の目がだんだん曇っていく..."
    - "省エネ基準の改正内容を共有したいけど、どこから手をつけていいかわからない"
    - "結局PDFをそのまま送って「読んでおいてください」で終わる"
  bottom_message: "複雑な情報を、わかりやすく伝える手段がない"

visual:
  center_image:
    description: "困っている営業担当のイラスト"
    details: "頭の上に「？」マーク、手元に分厚い資料"

notes:
  - "吹き出しは人物の周囲に配置"
```

---

# スライド3: この動画でわかること

```yaml
layout:
  type: "チェックリスト形式"
  image_position: "right"

copy:
  heading: "この動画でわかること"
  checklist:
    - "Geminiで情報をリサーチする方法"
    - "Nano Banana Proでインフォグラフィックを作る手順"
    - "きれいな図解を作るプロンプトのコツ"
    - "住宅業界での具体的な活用シーン"

visual:
  checklist:
    icon: "checkmark"
    color: "green"
  side_image:
    description: "インフォグラフィックの生成画面イメージ"

notes:
  - "チェックマークは緑色"
```

---

# スライド4: Before / After

```yaml
layout:
  type: "左右2分割"
  left: "Before"
  right: "After"

copy:
  heading: "AIで変わる情報伝達"
  before:
    title: "Before"
    points:
      - "文字びっしりの資料をそのまま渡す"
      - "口頭で長々と説明"
      - "お客様が理解できず、何度も同じ説明"
  after:
    title: "After"
    points:
      - "1枚の図解でパッと伝わる"
      - "調べる→まとめる→画像化が一気通貫"
      - "日本語もきれいに表示"
  bottom_message: "デザインスキル不要でプロ級の図解が作れる"

visual:
  before:
    image_description: "文字だらけのPDF資料、困惑するお客様"
  after:
    image_description: "カラフルなインフォグラフィック、笑顔のお客様"

notes:
  - "Beforeは暗め、Afterは明るめの色調"
```

---

# スライド5: Nano Banana Pro 基本情報

```yaml
layout:
  type: "カード形式"
  card_count: 5

copy:
  heading: "Nano Banana Pro 基本情報"
  cards:
    - label: "正式名称"
      text: "Gemini 3 Pro Image"
    - label: "提供元"
      text: "Google DeepMind"
    - label: "料金"
      text: "無料プランあり（回数制限）"
    - label: "特徴"
      text: "日本語テキストがきれいに出力"
    - label: "アクセス"
      text: "Gemini → 画像作成 → 思考モード"
  bottom_message: "2025年11月リリースの最新画像生成AI"

visual:
  cards:
    - icon: "tag"
    - icon: "google"
    - icon: "yen"
    - icon: "sparkle"
    - icon: "cursor"

notes:
  - "Geminiのロゴを右上に配置"
```

---

# スライド6: メリット① 一気通貫

```yaml
layout:
  type: "左右分割"
  left: "テキスト"
  right: "イラスト"

copy:
  heading: "① 調べる→まとめる→画像化が一気通貫"
  points:
    - "Geminiで補助金情報をリサーチ"
    - "そのままインフォグラフィックを作成"
    - "複数ツールを行き来する必要なし"
  bottom_message: "1つの画面で完結するから時短になる"

visual:
  right_image:
    description: "Gemini画面のフロー図（検索→整理→画像生成）"
  flow:
    - element: "検索アイコン"
    - arrow: true
    - element: "整理アイコン"
    - arrow: true
    - element: "画像アイコン"

notes:
  - "シンプルな3ステップのフローで表現"
```

---

# スライド7: メリット② 日本語がきれい

```yaml
layout:
  type: "左右分割"
  left: "比較"
  right: "サンプル画像"

copy:
  heading: "② 日本語がきれいに出力される"
  comparison:
    - label: "従来のAI"
      text: "文字が崩れる、意味不明な文字になる"
    - label: "Nano Banana Pro"
      text: "日本語テキストが正確に表示"
  bottom_message: "文字びっしりのインフォグラフィックも問題なし"

visual:
  right_image:
    description: "日本語がきれいに入ったインフォグラフィックのサンプル"
  comparison:
    before: "文字化けした画像例"
    after: "きれいな日本語の画像例"

notes:
  - "実際の生成サンプルを掲載"
```

---

# スライド8: メリット③ 説明の手間削減

```yaml
layout:
  type: "中央配置"

copy:
  heading: "③ 説明の手間が劇的に減る"
  main_message: "百聞は一見にしかず"
  points:
    - "1枚の絵で説明できれば、長々と話す必要なし"
    - "お客様への説明資料としてそのまま使える"
    - "社内共有用にも活用可能"

visual:
  center_image:
    description: "お客様にタブレットで図解を見せている営業担当"
    details: "お客様は笑顔でうなずいている"

notes:
  - "実際の活用シーンをイメージさせる"
```

---

# スライド9: 全体の流れ

```yaml
layout:
  type: "フロー図中心"
  flow_direction: "horizontal"
  steps: 5

copy:
  heading: "インフォグラフィック作成の流れ"
  steps:
    - number: "1"
      text: "リサーチ"
    - number: "2"
      text: "構成決め"
    - number: "3"
      text: "生成"
    - number: "4"
      text: "調整"
    - number: "5"
      text: "活用"

visual:
  flow:
    - step: 1
      icon: "search"
    - arrow: true
    - step: 2
      icon: "list"
    - arrow: true
    - step: 3
      icon: "magic"
    - arrow: true
    - step: 4
      icon: "edit"
    - arrow: true
    - step: 5
      icon: "share"

notes:
  - "各ステップにアイコンを配置"
```

---

# スライド10: 【実演】ステップ1 リサーチ

```yaml
layout:
  type: "左右分割"
  left: "手順"
  right: "画面イメージ"

copy:
  heading: "【実演】ステップ1：Geminiで情報をリサーチ"
  steps:
    - "Geminiを開く"
    - "「子育てエコホーム支援事業について、対象者、補助額、申請条件を教えて」と質問"
    - "最新情報を確認"
    - "ポイントを整理"
  note: "※実際の画面で実演します"

visual:
  right_image:
    type: "screenshot_placeholder"
    description: "Geminiでリサーチしている画面"

notes:
  - "実演で補完されるため簡潔に"
```

---

# スライド11: 【実演】ステップ2 構成決め

```yaml
layout:
  type: "左右分割"
  left: "チェックリスト"
  right: "サンプル"

copy:
  heading: "【実演】ステップ2：構成を決める"
  checklist:
    - label: "入れる情報"
      items:
        - "対象者"
        - "補助額"
        - "条件"
        - "申請の流れ"
    - label: "形式を選ぶ"
      items:
        - "フローチャート"
        - "リスト"
        - "チャート"

visual:
  right_image:
    description: "8種類のインフォグラフィック形式のサムネイル"

notes:
  - "形式の選び方を視覚的に示す"
```

---

# スライド12: 【実演】ステップ3 生成

```yaml
layout:
  type: "左右分割"
  left: "手順"
  right: "画面イメージ"

copy:
  heading: "【実演】ステップ3：Nano Banana Proで生成"
  steps:
    - "「画像を作成」を選択"
    - "「思考モード」を選択"
    - "プロンプトを入力"
    - "生成ボタンをクリック"
  note: "※実際の画面で実演します"

visual:
  right_image:
    type: "screenshot_placeholder"
    description: "Nano Banana Proの生成画面"

notes:
  - "思考モードの選択が重要ポイント"
```

---

# スライド13: プロンプトのコツ

```yaml
layout:
  type: "カード横並び"
  columns: 3

copy:
  heading: "きれいなインフォグラフィックを作るコツ"
  cards:
    - label: "コツ①"
      title: "5つの要素を含める"
      text: "被写体・構図・内容・背景・スタイル"
    - label: "コツ②"
      title: "日本語を直接指定"
      text: "「指定した文字以外は入れないで」と追記"
    - label: "コツ③"
      title: "アスペクト比を指定"
      text: "16:9の横長、正方形など用途に合わせて"

visual:
  cards:
    - icon: "layers"
    - icon: "text"
    - icon: "aspect_ratio"

notes:
  - "3つのコツを視覚的に強調"
```

---

# スライド14: プロンプト例

```yaml
layout:
  type: "コードブロック中心"

copy:
  heading: "実際のプロンプト例"
  code_block: |
    子育てエコホーム支援事業のインフォグラフィックを作成してください。

    【入れる情報】
    ・タイトル：子育てエコホーム支援事業 早わかりガイド
    ・対象者：子育て世帯、若者夫婦世帯
    ・補助額：新築 最大100万円、リフォーム 最大60万円
    ・条件：省エネ基準適合が必要
    ・申請の流れ：契約→着工→申請→交付

    【スタイル】
    ・16:9の横長レイアウト
    ・青と緑を基調とした爽やかな配色
    ・フラットデザインのアイコンを使用
    ・指定した日本語以外の文字は入れないでください
  bottom_message: "このプロンプトをコピーして使ってみてください"

visual:
  background: "コードブロック風の背景"
  highlight:
    - "【入れる情報】"
    - "【スタイル】"

notes:
  - "プロンプトは読みやすいフォントで表示"
  - "コピー可能であることを示す"
```

---

# スライド15: 【実演】ステップ4-5 調整と活用

```yaml
layout:
  type: "左右分割"
  left: "調整"
  right: "活用"

copy:
  heading: "【実演】ステップ4-5：調整と活用"
  adjust:
    title: "ステップ4：調整"
    points:
      - "「もう少し文字を大きく」"
      - "「色を変えて」"
      - "再生成で微調整"
  use:
    title: "ステップ5：活用"
    points:
      - "お客様への説明資料として印刷"
      - "社内共有用にチャットで送信"
      - "SNSやホームページに掲載"

visual:
  left_image:
    description: "調整指示を出している画面"
  right_image:
    description: "完成したインフォグラフィックを活用しているシーン"

notes:
  - "調整と活用を1枚にまとめて効率化"
```

---

# スライド16: 職種別おすすめの使い方

```yaml
layout:
  type: "カード横並び"
  columns: 3

copy:
  heading: "職種別おすすめの使い方"
  cards:
    - role: "営業担当"
      text: "補助金・ローンの説明資料、会社の強みを1枚で伝える"
    - role: "設計担当"
      text: "省エネ基準の図解、施工の流れをフローチャートに"
    - role: "事務担当"
      text: "社内マニュアルの図解化、手続きの流れを可視化"
  bottom_message: "どの職種でも「伝える」シーンで活躍"

visual:
  cards:
    - icon: "businessperson"
    - icon: "architect"
    - icon: "office_worker"

notes:
  - "各職種のイラストまたはアイコンを使用"
```

---

# スライド17: まとめ

```yaml
layout:
  type: "カード横並び"
  columns: 3

copy:
  heading: "まとめ"
  cards:
    - label: "①"
      text: "Geminiで調べてそのまま図解に（一気通貫）"
    - label: "②"
      text: "日本語がきれいに出力される"
    - label: "③"
      text: "5要素＋日本語直接指定がプロンプトのコツ"
  cta:
    prefix: "🚀"
    text: "「これ、図解にしたら伝わりやすいのに」と思ったら、Nano Banana Proを試してみてください！"

visual:
  cards:
    - icon: "workflow"
    - icon: "text_ja"
    - icon: "lightbulb"
  cta:
    style: "強調枠"

notes:
  - "3つのポイントに集約"
  - "色はネイビー基調、アクセントはオレンジ"
```

---

# スライド18: エンディング

```yaml
layout:
  type: "中央配置"
  simple: true

copy:
  main_message: "ご視聴ありがとうございました"
  sub_message: "次回の講座でお会いしましょう"
  supplement: "Build AI Academy"

visual:
  logo: "Build AI Academy"

notes:
  - "シンプルに"
```

---

## イラスト・図解の調達方法

| 種類 | 調達先 | 用途 |
|-----|--------|------|
| 人物イラスト | いらすとや / unDraw | 課題提起、活用シーン |
| アイコン | Material Icons / Feather Icons | カード、フロー図 |
| スクリーンショット | 実際のGemini画面をキャプチャ | 実演スライド |
| インフォグラフィックサンプル | Nano Banana Proで事前に生成 | Before/After、サンプル表示 |

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

### 構成チェック
- [x] 導入部分がコンパクト（課題→わかること→Before/After→基本情報）
- [x] 重複するスライドがない（同じ内容のスライドは統合済み）
- [x] 機能紹介が個別スライドに分割されている
- [x] 活用例がシーン別に分割されている
- [x] 実演部分は簡素になっている

### 住宅業界向けチェック
- [x] 住宅業界での活用イメージが含まれている
- [x] 職種別おすすめを含めている
- [x] Before/Afterで現場の変化がわかる

### まとめチェック
- [x] まとめスライドで要点が3つに集約されている
- [x] 行動を促すCTA（Call To Action）がある
