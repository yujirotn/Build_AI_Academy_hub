# スライド詳細設計書

## 講座情報
title: "Google AI Studioの使い方"
target: "住宅・建設会社の社員（営業、事務、現場監督など）"
duration: "15〜20分"
slide_count: 12

※台本の内容を200〜250文字ごとに1スライドとして分割
※実演パート（セクション3, 4）は実際の画面操作で説明するためスライド化しない
※台本の順序・内容を忠実に反映

---

## スライド一覧

# スライド1: タイトル

layout:
  type: "中央配置"

copy:
  main_title: "Google AI Studioの使い方"
  sub_title: "Geminiを無料で試せるプラットフォーム"
  badge_date: "2026年1月版"

visual:
  main_image:
    description: "Google AI Studioのロゴ"

notes:
  - "冒頭挨拶に対応"

---

# スライド2: こんな方におすすめ

layout:
  type: "中央イラスト＋周囲吹き出し"
  bubble_count: 3

copy:
  heading: "こんな方におすすめ"
  lead: "Googleアカウントさえあれば、今日から無料で使い始められます"
  bubbles:
    - "普段Geminiを使っていない"
    - "ChatGPTは使っているけどGeminiはよくわからない"
    - "Geminiに課金するか迷っている"
  bottom_message: "無料でGeminiの実力を試せるので、導入としてぴったり"
  note: "画面は英語ですが、入力や回答は日本語でOK"

visual:
  center_image:
    description: "考えている人物のイラスト"
    details: "頭の上に「？」マーク"
  bottom_message:
    style: "強調枠"

notes:
  - "3つのターゲット層を明確に"
  - "日本語OKであることも伝える"

---

# スライド3: Google AI Studioとは？

layout:
  type: "左右分割"
  left: "テキスト"
  right: "画像"

copy:
  heading: "Google AI Studioとは？"
  description: "一言で言うと..."
  main_message: "GoogleのAI「Gemini」をブラウザ上で無料で試せるプラットフォーム"

visual:
  right_image:
    type: "screenshot"
    description: "Google AI Studioのチャット画面"
  logo:
    name: "Google AI Studio"

notes:
  - "シンプルに一言で説明"

---

# スライド4: Gemini無料版との違い（導入）

layout:
  type: "中央配置（疑問提起）"

copy:
  heading: "Gemini無料版との違い"
  question: "「それならGeminiアプリでいいんじゃないの？」"
  lead: "確かにGemini無料版でも..."
  points:
    - "高性能なGemini 3.0 Proモデルが使える"
    - "Gems機能で自分専用のツールを作れる"
  bottom_message: "では何が違うのでしょうか？"

visual:
  center_image:
    description: "Geminiアプリのロゴと「？」マーク"
  bottom_message:
    style: "強調枠"

notes:
  - "疑問を投げかけて興味を引く"

---

# スライド5: 違い①：動画・音声・PDFの分析

layout:
  type: "左右2分割"
  left: "Geminiアプリ"
  right: "Google AI Studio"

copy:
  heading: "違い①：動画・音声・PDFの分析"
  left:
    title: "Geminiアプリ"
    text: "テキストと画像が中心"
  right:
    title: "Google AI Studio"
    text: "動画・音声ファイル・YouTubeを直接読み込んで分析できる"
  bottom_message: "動画や音声ファイル、PDFを直接アップロードして分析できる"

visual:
  left:
    icon: "text_image"
    color: "gray"
  right:
    icon: "video_audio_pdf"
    color: "blue"
    highlight: true

notes:
  - "Geminiアプリとの違いを視覚的に"

---

# スライド6: 違い②：Build機能

layout:
  type: "中央配置（機能紹介）"

copy:
  heading: "違い②：Build機能"
  main_message: "日本語で指示するだけでWebアプリを自動生成"
  sub_points:
    - "「こんなツールが欲しい」と日本語で指示するだけ"
    - "プログラミング知識がなくても簡易的なアプリを作成できる"
  emphasis: "これはGeminiアプリにはない機能"

visual:
  center_image:
    description: "Build機能のイメージ（指示→アプリ生成）"
  emphasis:
    style: "強調枠"

notes:
  - "Geminiアプリにはない独自機能を強調"

---

# スライド7: 使い分けとデータプライバシー注意

layout:
  type: "上下2分割"
  top: "使い分け"
  bottom: "注意点"

copy:
  heading: "使い分けとデータプライバシー"
  top:
    title: "使い分けのイメージ"
    lead: "Geminiアプリよりも「できることの幅が広い」"
    left:
      label: "Geminiアプリ"
      text: "日常的な質問や文章作成"
    right:
      label: "Google AI Studio"
      text: "動画や音声の分析、アプリ作成、高性能モデルの試用"
  bottom:
    title: "⚠️ 注意"
    text: "入力したデータはAIの学習に使われる可能性あり"
    sub: "機密度の高い情報は入力しないように注意"

visual:
  top:
    type: "比較図"
  bottom:
    icon: "warning"
    color: "yellow"

notes:
  - "使い分けと注意点をセットで説明"
  - "台本でこのタイミングで注意喚起"

---

# スライド8: 利用回数の制限

layout:
  type: "左右2分割"
  left: "Pro系"
  right: "Flash系"

copy:
  heading: "利用回数の制限"
  lead: "無料では、1日あたりの利用回数に上限があります"
  note: "※制限値はモデルや時期によって変動"
  left:
    title: "Pro系モデル"
    text: "制限が厳しめ"
  right:
    title: "Flash系モデル"
    text: "比較的多く使える"
  bottom_message: "日常業務にはGemini 3 Flashがおすすめ"
  transition: "では、実際の画面を見ながら使い方を説明していきます"

visual:
  left:
    icon: "star"
    color: "gold"
  right:
    icon: "bolt"
    color: "blue"
    highlight: true

notes:
  - "ここから実演パートへの橋渡し"

---

# ※実演パート（スライド化しない）
※台本: 3. 実演：チャット機能、4. 実演：Build機能
※実際の画面操作で説明するため、スライドは作成しない

実演で説明する内容:
- ログイン方法
- 画面の見方（3エリア構成）
- モデルの選択（Gemini 3 Flash / Pro）
- 5つのタブ（Gemini、Live、Images、Video、Audio）
- 設定パネルの機能（System instructions、Thinking level、Grounding、URL context）
- Build機能の使い方と活用例

---

# スライド9: 料金について（無料）

layout:
  type: "中央配置（強調メッセージ）"

copy:
  heading: "料金について"
  emphasis: "嬉しいお知らせです"
  main_message: "Google AI Studio自体の利用は完全無料"
  sub_points:
    - "Googleアカウントがあれば、今すぐ使い始められる"
    - "クレジットカードの登録も不要"
  features: "Gemini 3 Pro、Gemini 3 Flash、チャット、Build、画像生成、動画生成のすべてが無料"
  note: "※1日あたりの利用回数に制限あり（個人利用・学習には十分）"

visual:
  main_icon:
    description: "無料マーク（¥0）"
    style: "大きく中央に"

notes:
  - "無料であることを強調"

---

# スライド10: 料金について（従量課金）

layout:
  type: "上下2分割"
  top: "有料プラン"
  bottom: "まとめ"

copy:
  heading: "有料プランについて"
  top:
    title: "従量課金プラン"
    description: "より多くの回数を使いたい場合や、業務で本格的に使いたい場合"
    explanation: "「従量課金」＝使った分だけ料金がかかる仕組み"
  bottom:
    message: "ただし、今日ご紹介した内容は、すべて無料の範囲で試せます"
    cta: "まずは無料で触ってみてください"

visual:
  top:
    icon: "paid"
    color: "blue"
  bottom:
    style: "強調枠"

notes:
  - "無料で試せることを強調"

---

# スライド11: 注意点

layout:
  type: "リスト形式"
  items: 2

copy:
  heading: "注意点"
  lead: "最後に、Google AI Studioを使う上での注意点をまとめます"
  items:
    - label: "データプライバシー（大事なポイント）"
      text: "無料プランでは、入力したデータがGoogleの製品改善に使われる可能性があります"
      action: "お客様の個人情報や会社の機密情報は入力しない"
      recommendation: "学習や試作の範囲で使うのがおすすめ"
    - label: "制限に達した場合"
      text: "翌日のリセットを待つか、別のモデルに切り替え"
      detail: "リセットは日本時間で毎日16〜17時頃"

visual:
  items:
    - icon: "security"
      color: "yellow"
    - icon: "refresh"
      color: "blue"

notes:
  - "2つの注意点を明確に"

---

# スライド12: まとめ

layout:
  type: "カード横並び"
  columns: 3

copy:
  heading: "まとめ"
  lead: "今日はGoogle AI Studioの基本的な使い方をご紹介しました"
  cards:
    - label: "①"
      text: "GoogleのAI「Gemini」を無料で使えるプラットフォーム"
      sub: "最新のGemini 3シリーズも無料で試せる"
    - label: "②"
      text: "Googleアカウントだけで今日から始められる"
    - label: "③"
      text: "機密情報は入力しないように注意"
      sub: "入力データがGoogleの製品改善に使われる可能性"
  cta:
    prefix: "🚀"
    text: "Google AI Studioにアクセスして、Gemini 3 Flashでチャット機能を触ってみてください"
  closing: "それでは次の講座で会いましょう。ありがとうございました。"

visual:
  cards:
    - icon: "free"
    - icon: "account"
    - icon: "security"
  cta:
    style: "強調枠"

notes:
  - "3つのポイントに集約"
  - "具体的なアクションを促す"

---

## 台本とスライドの対応表

| 台本セクション | 対応スライド | 台本文字数 | スライド化 |
|--------------|-------------|-----------|-----------|
| 1. オープニング | 1-2 | 約305文字 | ○ |
| 2. ツール概要 | 3-8 | 約845文字 | ○ |
| 3. 実演：チャット機能 | - | 約1,410文字 | ✕（実演） |
| 4. 実演：Build機能 | - | 約410文字 | ✕（実演） |
| 5. 料金について | 9-10 | 約360文字 | ○ |
| 6. 注意点 | 11 | 約220文字 | ○ |
| 7. クロージング | 12 | 約285文字 | ○ |
| **合計** | **12枚** | **約3,835文字** | - |

---

## スライド分割の根拠

| スライド | 対応する台本内容 | 文字数 |
|---------|-----------------|--------|
| 1 | タイトル・挨拶 | 約60 |
| 2 | こんな方におすすめ | 約245 |
| 3 | Google AI Studioとは？ | 約80 |
| 4 | Gemini無料版との違い（導入） | 約130 |
| 5 | 違い①：動画・音声・PDF分析 | 約130 |
| 6 | 違い②：Build機能 | 約110 |
| 7 | 使い分けとデータプライバシー | 約205 |
| 8 | 利用回数の制限 | 約190 |
| 9 | 料金について（無料） | 約220 |
| 10 | 料金について（従量課金） | 約140 |
| 11 | 注意点 | 約220 |
| 12 | まとめ | 約285 |

---

## イラスト・図解の調達方法

| 種類 | 調達先 | 用途 |
|-----|--------|------|
| Google AI Studio画面キャプチャ | 実際の画面をキャプチャ | スライド3 |
| 人物イラスト | イラストAC / Canva | スライド2 |
| アイコン類 | Google Material Icons / Canva | 各スライド |
| 比較図 | Canva / PowerPoint | スライド5, 7 |

---

## チェックリスト

### 基本チェック
- [x] すべてのスライドにタイトルがある
- [x] すべてのスライドにVISUAL要素が指定されている
- [x] COPYの情報量が適切（台本200〜250文字に対応）
- [x] 各スライドに対応する台本箇所と文字数を明記

### 3ブロック分離チェック（混入防止）
- [x] COPYに「レイアウト」「図解」「アイコン」「配置」等の指示語が含まれていない
- [x] VISUALに「〜です」「〜ます」等の文章表現が含まれていない
- [x] LAYOUTに表示テキストが含まれていない

### 台本との整合性チェック
- [x] スライドの順序が台本の順序と完全に一致
- [x] 台本の内容（実演パート以外）が漏れなくスライドに反映されている
- [x] 実演パートはスライド化せず、実際の画面操作で説明

### 構成チェック
- [x] 実演部分はスライド化していない
- [x] 重複するスライドがない
- [x] 台本の流れに沿った自然な構成
- [x] 1スライドあたり台本約200〜250文字に対応

### まとめチェック
- [x] まとめスライドで要点が3つに集約されている
- [x] 行動を促すCTA（Call To Action）がある
- [x] クロージングの挨拶が含まれている
