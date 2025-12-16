# スライド詳細設計書（v2形式）

## 講座情報

```yaml
title: "ChatGPTでExcelデータを自社フォーマットに自動変換する方法"
target: "住宅会社の事務担当・経理担当"
duration: "10〜15分"
slide_count: 19
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
  main_title: "ChatGPTでExcelデータを自社フォーマットに自動変換する方法"
  sub_title: "コピペ地獄からの解放"
  badge_difficulty: "初心者向け"
  badge_date: "2025年12月版"

visual:
  logo: "Build AI Academy"
  main_image:
    description: "バラバラなExcelファイルが整ったフォーマットに変換されるイメージ"
    style: "明るく効率化を感じさせる雰囲気"

notes:
  - "Excelアイコンを複数配置し、矢印で1つの整ったシートに変換されるイメージ"
  - "ChatGPTロゴも小さく配置"
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
    - "協力業者からの請求書、フォーマットがバラバラで毎回手作業でコピペ…"
    - "現場からの出来高報告書、微妙にフォーマットが違って転記に何十分も…"
    - "お客様からの要望リスト、形式がバラバラで管理台帳への転記が大変…"
  bottom_message: "課題の本質は「データの形式を揃える作業に人の手がかかりすぎている」こと"

visual:
  center_image:
    description: "困っている事務担当"
    details: "机の上にバラバラなExcelファイル（紙）が散乱、頭を抱えている"
  bubbles:
    style: "吹き出し（白背景・グレー枠）"
  bottom_message:
    style: "強調枠（濃い背景色）"

notes:
  - "事務担当は女性でも男性でもOK"
  - "Excelファイルは色違いで「バラバラ感」を表現"
```

---

# スライド3: その悩み、ChatGPTで解決できます

```yaml
layout:
  type: "中央配置（強調メッセージ）"
  flow_direction: "horizontal"

copy:
  main_message: "AIにルールを教えておけば、ファイルをアップロードするだけで自動変換"
  sub_message: "OpenAIが提供する「ChatGPT」のGPTs機能を活用"
  bottom_keywords:
    - "一度設定すればOK"
    - "ファイルをアップするだけ"
    - "転記ミスゼロ"

visual:
  flow:
    - element: "バラバラなExcelファイル"
    - arrow: true
    - element: "ChatGPTロゴ"
    - arrow: true
    - element: "整ったExcelファイル"
  bottom_message:
    style: "強調枠"
    separator: "・"

notes:
  - "メインメッセージは大きく太字"
  - "フローの矢印は右向き、変換のイメージを表現"
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
    - "ChatGPTでExcel変換を自動化する仕組みの作り方"
    - "GPTs機能の基本的な使い方"
    - "プロジェクト機能を使った代替方法（無料プランでも可）"
    - "有料版と無料版の違い"
  bottom_message: "初めての方でも、動画を見ながら一緒に操作できます"

visual:
  checklist:
    icon: "checkmark"
    color: "green"
  side_image:
    description: "ChatGPT画面イメージ"
    type: "screenshot"
  bottom_message:
    style: "強調枠"

notes:
  - "チェックマークは緑色で統一"
  - "各項目は太字強調"
```

---

# スライド5: ChatGPTとは？

```yaml
layout:
  type: "左右分割"
  left: "テキスト説明"
  right: "画面キャプチャ"

copy:
  heading: "ChatGPTとは？"
  items:
    - label: "ツール名"
      text: "ChatGPT（チャットジーピーティー）"
    - label: "提供元"
      text: "OpenAI"
    - label: "概要"
      text: "テキストで会話しながら様々なタスクをこなせるAIツール"
    - label: "特徴"
      text: "Excelファイルのアップロード・編集・ダウンロードが可能"
  bottom_message: "「自分専用の事務アシスタント」を作れる"

visual:
  left:
    logo: "ChatGPTロゴ"
  right:
    type: "screenshot"
    description: "ChatGPTの画面キャプチャ"

notes:
  - "ツール名は太字強調"
  - "画面キャプチャは最新版を使用"
```

---

# スライド6: ChatGPT基本情報

```yaml
layout:
  type: "カード形式"
  card_count: 5
  card_style: "アイコン付き横並び"

copy:
  heading: "ChatGPT基本情報"
  cards:
    - label: "料金"
      text: "無料プランあり（有料版は月額約3,000円）"
    - label: "GPTs機能"
      text: "有料プラン（Plus）で利用可能"
    - label: "プロジェクト機能"
      text: "無料プランでも利用可能"
    - label: "ファイルサイズ"
      text: "1ファイルあたり最大512MB"
    - label: "ファイル数"
      text: "無料5件、Plus20件/プロジェクト"
  bottom_message: "今回の用途なら、まずは無料プランから試せます"

visual:
  cards:
    - icon: "yen"
    - icon: "robot"
    - icon: "folder"
    - icon: "storage"
    - icon: "document"

notes:
  - "アイコンはフラットデザイン"
  - "「無料プランあり」は太字強調"
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
      title: "フォーマット変換が一瞬で完了"
      text: "AIが自動で項目を対応付け"
    - label: "②"
      title: "一度設定すれば同じ品質"
      text: "転記ミス・バラつきがなくなる"
    - label: "③"
      title: "事務作業の時間を大幅削減"
      text: "月末処理が数分で終わる"
  bottom_message: "これから各メリットを詳しく紹介します"

visual:
  center_element:
    text: "ChatGPT × Excel変換"
    style: "中央配置・背景色付き"
  items:
    - icon: "lightning"
    - icon: "check_circle"
    - icon: "clock"

notes:
  - "中央に「ChatGPT × Excel変換」を配置"
  - "周囲に3つのメリットを放射状に配置"
```

---

# スライド8: メリット① フォーマット変換が一瞬で完了

```yaml
layout:
  type: "左右2分割"
  left: "Before"
  right: "After"
  divider: "center_arrow"

copy:
  heading: "メリット① フォーマット変換が一瞬で完了"
  before:
    title: "Before"
    points:
      - "列の順番が違う、項目名が違う…"
      - "手作業で1つずつコピー＆ペースト"
      - "どこに何を入れるか毎回確認"
  after:
    title: "After"
    points:
      - "「変換して」とお願いするだけ"
      - "AIが自動で項目を対応付け"
      - "正しい位置に自動で当て込み"
  bottom_message: "列の順番が違っても、項目名が微妙に違っても、AIが賢く判断"

visual:
  before:
    image_description: "バラバラなExcelシートと困っている人"
    tone: "暗め・煩雑な雰囲気"
  after:
    image_description: "整ったExcelシートと笑顔の人"
    tone: "明るめ・スッキリした雰囲気"
  bottom_message:
    style: "強調枠"

notes:
  - "Beforeは暗め、Afterは明るめの色調で対比"
  - "中央に矢印を配置"
```

---

# スライド9: メリット② 一度設定すれば同じ品質

```yaml
layout:
  type: "フロー図中心"
  flow_direction: "horizontal"
  steps: 3

copy:
  heading: "メリット② 一度設定すれば同じ品質"
  steps:
    - number: "初回"
      text: "ルールを設定"
      detail: "「このフォーマットに変換してね」"
    - number: "2回目以降"
      text: "ファイルをアップロード"
      detail: "ドラッグ＆ドロップするだけ"
    - number: "結果"
      text: "毎回同じ品質で変換"
      detail: "人によるバラつきなし"
  bottom_message: "転記ミスや品質のバラつきがなくなる"

visual:
  flow:
    - step: "初回"
      icon: "settings"
    - arrow: true
    - step: "2回目以降"
      icon: "upload"
    - arrow: true
    - step: "結果"
      icon: "check"
  bottom_message:
    style: "強調枠"

notes:
  - "各ステップは番号付きで視覚的に区切る"
  - "矢印は右向き"
```

---

# スライド10: メリット③ 事務作業の時間を大幅に削減

```yaml
layout:
  type: "左右2分割"
  left: "Before"
  right: "After"
  divider: "center_arrow"

copy:
  heading: "メリット③ 事務作業の時間を大幅に削減"
  before:
    title: "Before"
    points:
      - "月末の請求処理に何時間もかかる"
      - "週次報告の集計で残業…"
      - "本来やるべき確認作業に手が回らない"
  after:
    title: "After"
    points:
      - "請求処理が数分で完了"
      - "週次報告もサクッと終わる"
      - "確認作業やお客様対応に集中できる"
  bottom_message: "浮いた時間で、本来やるべき業務に集中"

visual:
  before:
    image_description: "残業している事務担当（時計は20時）"
    tone: "暗め・疲れた雰囲気"
  after:
    image_description: "定時で帰る事務担当（時計は17時）"
    tone: "明るめ・元気な雰囲気"
  bottom_message:
    style: "強調枠"

notes:
  - "時計のイラストで時間短縮を視覚化"
  - "Beforeは夜、Afterは夕方の明るさで表現"
```

---

# スライド11: 様々なExcel作業に応用できる

```yaml
layout:
  type: "放射状配置"
  center: "ChatGPT"
  items_count: 5

copy:
  heading: "様々なExcel作業に応用できる"
  items:
    - title: "請求書の取り込み"
      text: "協力業者からの請求書を経理システム用に変換"
    - title: "出来高報告の集計"
      text: "現場ごとの報告書を統一フォーマットに"
    - title: "発注リストの作成"
      text: "各現場の発注依頼をまとめて発注書に"
    - title: "顧客データの整理"
      text: "お客様情報を管理台帳フォーマットに"
    - title: "変更依頼の統合"
      text: "バラバラな変更依頼を一覧表に"
  bottom_message: "「元データを自社フォーマットに当て込む」作業ならなんでもOK"

visual:
  center:
    element: "ChatGPTロゴ"
    style: "大きめ・中央配置"
  items:
    - icon: "receipt"
    - icon: "chart"
    - icon: "clipboard"
    - icon: "users"
    - icon: "edit"
  bottom_message:
    style: "強調枠"

notes:
  - "中央にChatGPTロゴ、周囲に5つの活用例を放射状に配置"
  - "住宅会社の実務に即した例を選定"
```

---

# スライド12: 全体の流れ

```yaml
layout:
  type: "フロー図中心"
  flow_direction: "vertical"
  steps: 3

copy:
  heading: "全体の流れ"
  steps:
    - number: "手順1"
      text: "指示書（プロンプト）を作らせる"
      detail: "ChatGPTに変換ルールを作ってもらう"
    - number: "手順2"
      text: "GPTsを作成する"
      detail: "自分専用の変換ボットを作る"
    - number: "手順3"
      text: "実行する"
      detail: "ファイルをアップして変換"
  bottom_message: "これから各手順を詳しく説明します"

visual:
  flow:
    - step: 1
      icon: "document"
    - arrow: true
    - step: 2
      icon: "robot"
    - arrow: true
    - step: 3
      icon: "play"
  bottom_message:
    style: "強調枠"

notes:
  - "縦方向のフローで3ステップを表現"
  - "各ステップは番号とアイコンで視覚化"
```

---

# スライド13: 【実演】手順1：指示書を作らせる

```yaml
layout:
  type: "左右分割"
  left: "手順リスト"
  right: "画面イメージ"

copy:
  heading: "【実演】手順1：指示書を作らせる"
  steps:
    - "ChatGPTのチャット画面を開く"
    - "2つのファイルをアップロード（自社フォーマット＋元データ）"
    - "「このフォーマットに変換するプロンプトを作って」と指示"
    - "出力されたプロンプトをコピーして控えておく"
  note: "※実際の画面で実演します"

visual:
  right:
    type: "screenshot_placeholder"
    description: "ChatGPTにファイルをアップロードする画面"
  steps:
    style: "番号付きリスト"

notes:
  - "実演で補完されるため簡潔に"
  - "ファイルアップロードのUIを見せる"
```

---

# スライド14: 【実演】手順2：GPTsを作成する

```yaml
layout:
  type: "左右分割"
  left: "手順リスト"
  right: "画面イメージ"

copy:
  heading: "【実演】手順2：GPTsを作成する"
  steps:
    - "「GPTを探す」→「作成する」をクリック"
    - "「構成」タブを選択"
    - "名前を入力（例：Excel正規化ボット）"
    - "指示欄に手順1のプロンプトを貼り付け"
    - "知識に自社フォーマットのExcelをアップロード"
    - "「Code Interpreter」にチェック（必須）"
    - "「自分のみ」で保存"
  note: "※有料プラン（Plus）が必要です"

visual:
  right:
    type: "screenshot_placeholder"
    description: "GPTs作成画面"
  steps:
    style: "番号付きリスト"

notes:
  - "Code Interpreterのチェックを忘れずに強調"
  - "有料プラン必須であることを明記"
```

---

# スライド15: 【実演】手順3：実行する

```yaml
layout:
  type: "左右分割"
  left: "手順リスト"
  right: "画面イメージ"

copy:
  heading: "【実演】手順3：実行する"
  steps:
    - "作成したGPTsを開く"
    - "変換したいExcelファイルをドラッグ＆ドロップ"
    - "「お願いします」と送信"
    - "AIが自動で変換処理を実行"
    - "変換されたファイルをダウンロード"
  note: "※実際の画面で実演します"

visual:
  right:
    type: "screenshot_placeholder"
    description: "GPTsでファイルを変換している画面"
  steps:
    style: "番号付きリスト"

notes:
  - "ダウンロードリンクが表示される様子を見せる"
  - "変換結果のExcelを開いて確認する様子も"
```

---

# スライド16: 補足：プロジェクト機能を使う場合

```yaml
layout:
  type: "左右分割"
  left: "手順リスト"
  right: "画面イメージ"

copy:
  heading: "補足：プロジェクト機能を使う場合（無料プランでも可）"
  steps:
    - "サイドバーから「プロジェクト」を選択"
    - "新規プロジェクトを作成"
    - "カスタム指示に手順1のプロンプトを貼り付け"
    - "プロジェクトファイルに自社フォーマットを追加"
    - "このプロジェクト内のチャットで元データをアップして変換"
  note: "※無料プランはファイル5件まで、Plusは20件まで"

visual:
  right:
    type: "screenshot_placeholder"
    description: "プロジェクト機能の画面"
  steps:
    style: "番号付きリスト"

notes:
  - "GPTsが使えない場合の代替手段"
  - "無料プランでも試せることを強調"
```

---

# スライド17: 職種別おすすめの使い方

```yaml
layout:
  type: "カード横並び"
  columns: 3

copy:
  heading: "職種別おすすめの使い方"
  cards:
    - role: "経理担当"
      text: "協力業者からの請求書を経理システム用フォーマットに自動変換"
    - role: "工務担当"
      text: "現場からの出来高報告を統一フォーマットに集計"
    - role: "営業事務"
      text: "お客様からの変更依頼を管理台帳に自動転記"
  bottom_message: "どの職種でも「コピペ作業」を大幅削減"

visual:
  cards:
    - icon: "calculator"
      color: "navy"
    - icon: "hard_hat"
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

# スライド18: まとめ

```yaml
layout:
  type: "カード横並び"
  columns: 4
  card_style: "フラット塗り"

copy:
  heading: "まとめ"
  cards:
    - label: "①"
      text: "フォーマット変換が一瞬で完了（AIが自動で項目を対応付け）"
    - label: "②"
      text: "一度設定すれば同じ品質（転記ミス・バラつきなし）"
    - label: "③"
      text: "事務作業の時間を大幅削減（月末処理が数分で）"
    - label: "④"
      text: "様々なExcel作業に応用可能（請求書・報告書・台帳など）"
  cta:
    prefix: "🚀"
    text: "ぜひ普段手作業でやっているExcel転記作業を、ChatGPTで自動化してみてください！"

visual:
  cards:
    - icon: "lightning"
    - icon: "check_circle"
    - icon: "clock"
    - icon: "repeat"
  cta:
    style: "強調枠"

notes:
  - "各カードはフラット塗りアイコン"
  - "色はネイビー基調、アクセントはオレンジ"
```

---

# スライド19: エンディング

```yaml
layout:
  type: "中央配置"
  simple: true

copy:
  main_message: "ご視聴ありがとうございました"
  sub_message: "次回の講座でお会いしましょう"
  supplement: "ChatGPTの詳しい操作方法は別途解説動画をご用意しています"

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
| 画面キャプチャ | ChatGPT実際の画面 | 実演スライド、ツール紹介 |
| ロゴ | ChatGPT公式サイト | タイトル、ツール紹介 |
| Excelアイコン | Microsoft公式 | フォーマット変換のイメージ |
| フロー図 | PowerPoint図形で作成 | 手順説明、Before/After |

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
- [x] メリットが個別スライドに分割されている（3枚）
- [x] 実演部分は簡素になっている（4枚）

### 住宅業界向けチェック
- [x] 住宅業界での活用イメージが含まれている
- [x] 職種別おすすめを含めている
- [x] Before/Afterで現場の変化がわかる

### まとめチェック
- [x] まとめスライドで要点が4つに集約されている
- [x] 行動を促すCTA（Call To Action）がある
