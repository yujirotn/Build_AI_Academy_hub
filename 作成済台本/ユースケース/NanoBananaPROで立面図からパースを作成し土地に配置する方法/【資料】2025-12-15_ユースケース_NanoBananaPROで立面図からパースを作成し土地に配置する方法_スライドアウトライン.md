# スライド詳細設計書（v2形式）

## 講座情報

```yaml
title: "NanoBanana PROで立面図からパースを作成し土地に配置する方法"
target: "住宅会社の営業担当・設計担当"
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
  main_title: "NanoBanana PROで立面図からパースを作成し土地に配置する方法"
  sub_title: "白黒の図面を、お客様の土地にリアルに建てる"
  badge_difficulty: "初心者向け"
  badge_date: "2025年12月版"

visual:
  logo: "Build AI Academy"
  main_image:
    description: "立面図 → 外観パース → 土地に配置 の3ステップ変換イメージ"
    style: "明るく未来感のある雰囲気"

notes:
  - "立面図からリアルな外観イメージが生成される様子を視覚化"
  - "NanoBanana PROのロゴも小さく配置"
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
    - "立面図を見せても「イメージが湧かない」と言われる…"
    - "外観パースを外注すると数万円＆数日かかる…"
    - "「この土地に建つとどうなる？」と聞かれて答えられない…"
  bottom_message: "課題の本質は「お客様が完成イメージを具体的に想像できない」こと"

visual:
  center_image:
    description: "困っている営業担当"
    details: "立面図を持って困惑している様子"
  bubbles:
    style: "吹き出し（白背景・グレー枠）"
  bottom_message:
    style: "強調枠（濃い背景色）"

notes:
  - "営業担当は男性・女性どちらでもOK"
  - "立面図は白黒の図面をイメージ"
```

---

# スライド3: その悩み、NanoBanana PROで解決できます

```yaml
layout:
  type: "中央配置（強調メッセージ）"
  flow_direction: "horizontal"

copy:
  main_message: "AIに立面図を渡せば、リアルな外観パースを一瞬で生成"
  sub_message: "さらに、お客様の土地に配置することも可能"
  bottom_keywords:
    - "数十秒で完成"
    - "外注不要"
    - "土地に配置"

visual:
  flow:
    - element: "白黒の立面図"
    - arrow: true
    - element: "NanoBanana PROロゴ"
    - arrow: true
    - element: "土地に配置されたリアルな外観パース"
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
    - "立面図から外観パースを一瞬で作る方法"
    - "Googleマップの土地写真に建物を配置する方法"
    - "外壁や屋根の色をその場で変更する方法"
    - "NanoBanana PROの基本的な使い方"
  bottom_message: "初めての方でも、動画を見ながら一緒に操作できます"

visual:
  checklist:
    icon: "checkmark"
    color: "green"
  side_image:
    description: "NanoBanana PRO画面イメージ"
    type: "screenshot"
  bottom_message:
    style: "強調枠"

notes:
  - "チェックマークは緑色で統一"
  - "各項目は太字強調"
```

---

# スライド5: NanoBanana PROとは？

```yaml
layout:
  type: "左右分割"
  left: "テキスト説明"
  right: "画面キャプチャ"

copy:
  heading: "NanoBanana PROとは？"
  items:
    - label: "ツール名"
      text: "NanoBanana PRO（ナノバナナ プロ）"
    - label: "提供元"
      text: "BANANA GEMINI経由で利用"
    - label: "ベース"
      text: "Google Gemini（生成AI）"
    - label: "特徴"
      text: "画像をアップロードして指示を出すと、AIが画像を生成・編集"
  bottom_message: "立面図からパースを作ったり、背景を入れ替えたりできる"

visual:
  left:
    logo: "NanoBanana PROロゴ"
  right:
    type: "screenshot"
    description: "NanoBanana PROの画面キャプチャ"

notes:
  - "ツール名は太字強調"
  - "画面キャプチャは最新版を使用"
```

---

# スライド6: NanoBanana PRO基本情報

```yaml
layout:
  type: "カード形式"
  card_count: 4
  card_style: "アイコン付き横並び"

copy:
  heading: "NanoBanana PRO基本情報"
  cards:
    - label: "アクセス"
      text: "BANANA GEMINIから利用"
    - label: "推奨プラン"
      text: "Gemini Advanced（有料）"
    - label: "操作方法"
      text: "画像アップロード＋テキスト指示"
    - label: "生成時間"
      text: "数十秒で画像生成"
  bottom_message: "※生成された画像はあくまでイメージです。実際とは異なる場合があります"

visual:
  cards:
    - icon: "link"
    - icon: "star"
    - icon: "upload"
    - icon: "clock"

notes:
  - "アイコンはフラットデザイン"
  - "注意事項は小さめに表示"
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
      title: "外観パースが一瞬で完成"
      text: "設計ソフト不要・外注不要"
    - label: "②"
      title: "お客様の土地に配置"
      text: "リアルな完成イメージを提供"
    - label: "③"
      title: "バリエーション提案"
      text: "その場で色味・素材を変更"
  bottom_message: "これから各メリットを詳しく紹介します"

visual:
  center_element:
    text: "NanoBanana PRO × 外観提案"
    style: "中央配置・背景色付き"
  items:
    - icon: "image"
    - icon: "map_pin"
    - icon: "palette"

notes:
  - "中央に「NanoBanana PRO × 外観提案」を配置"
  - "周囲に3つのメリットを放射状に配置"
```

---

# スライド8: メリット① 外観パースが一瞬で完成

```yaml
layout:
  type: "左右2分割"
  left: "Before"
  right: "After"
  divider: "center_arrow"

copy:
  heading: "メリット① 外観パースが一瞬で完成"
  before:
    title: "Before"
    points:
      - "設計ソフトで作ると時間がかかる"
      - "外注すると数万円＆数日待ち"
      - "お客様を待たせてしまう"
  after:
    title: "After"
    points:
      - "立面図をアップロードするだけ"
      - "数十秒でリアルな画像が完成"
      - "その場でお客様にお見せできる"
  bottom_message: "白黒の立面図が、立体感のあるリアルな画像に変換される"

visual:
  before:
    image_description: "白黒の立面図と待っているお客様"
    tone: "暗め・時間がかかる雰囲気"
  after:
    image_description: "リアルな外観パースを見て喜ぶお客様"
    tone: "明るめ・スピード感"
  bottom_message:
    style: "強調枠"

notes:
  - "Beforeは暗め、Afterは明るめの色調で対比"
  - "中央に矢印を配置"
```

---

# スライド9: メリット② お客様の土地に配置

```yaml
layout:
  type: "左右2分割"
  left: "Before"
  right: "After"
  divider: "center_arrow"

copy:
  heading: "メリット② お客様の土地に配置"
  before:
    title: "Before"
    points:
      - "パースの背景が真っ白"
      - "どこかの展示場みたいな風景"
      - "「イメージしてください」としか言えない"
  after:
    title: "After"
    points:
      - "Googleマップで土地の写真を取得"
      - "その土地にパースを配置"
      - "「自分の土地に建った姿」をリアルに提示"
  bottom_message: "お客様が「この土地に、この家が建つ」を具体的に確認できる"

visual:
  before:
    image_description: "背景が真っ白な外観パース"
    tone: "抽象的・イメージしにくい"
  after:
    image_description: "実際の土地に建物が配置された画像"
    tone: "具体的・リアル"
  bottom_message:
    style: "強調枠"

notes:
  - "Afterは実際のストリートビュー風の背景"
  - "家が土地に自然に配置されているイメージ"
```

---

# スライド10: メリット③ バリエーションをその場で提案

```yaml
layout:
  type: "中央配置"
  variation_count: 3

copy:
  heading: "メリット③ バリエーションをその場で提案"
  examples:
    - "「外壁をもう少し白くして」"
    - "「屋根の色をグレーにして」"
    - "「窓枠を黒にして」"
  bottom_message: "色味や素材感を変えたパターンを何枚も作って、お客様と一緒に選べる"

visual:
  center_image:
    description: "同じ家の外観バリエーション3パターン"
    details: "外壁色違い（白・ベージュ・グレー）を横並び"
  examples:
    style: "吹き出し風"
  bottom_message:
    style: "強調枠"

notes:
  - "同じ建物で色違いの3パターンを並べる"
  - "お客様と営業担当が一緒に選んでいるイメージ"
```

---

# スライド11: 全体の流れ

```yaml
layout:
  type: "フロー図中心"
  flow_direction: "horizontal"
  steps: 5

copy:
  heading: "全体の流れ"
  steps:
    - number: "1"
      text: "ツールを開く"
      detail: "BANANA GEMINIからアクセス"
    - number: "2"
      text: "パース作成"
      detail: "立面図から外観パースを生成"
    - number: "3"
      text: "土地写真取得"
      detail: "Googleマップでスクショ"
    - number: "4"
      text: "土地に配置"
      detail: "パースを土地に配置"
    - number: "5"
      text: "調整"
      detail: "色味・素材を変更"
  bottom_message: "これから各手順を詳しく説明します"

visual:
  flow:
    - step: 1
      icon: "browser"
    - arrow: true
    - step: 2
      icon: "image"
    - arrow: true
    - step: 3
      icon: "map"
    - arrow: true
    - step: 4
      icon: "home"
    - arrow: true
    - step: 5
      icon: "settings"
  bottom_message:
    style: "強調枠"

notes:
  - "横方向のフローで5ステップを表現"
  - "各ステップは番号とアイコンで視覚化"
```

---

# スライド12: 【実演】手順1：NanoBanana PROを開く

```yaml
layout:
  type: "左右分割"
  left: "手順リスト"
  right: "画面イメージ"

copy:
  heading: "【実演】手順1：NanoBanana PROを開く"
  steps:
    - "ブラウザでBANANA GEMINIを開く"
    - "NanoBanana PROを選択"
  note: "※実際の画面で実演します"

visual:
  right:
    type: "screenshot_placeholder"
    description: "BANANA GEMINIのトップ画面"
  steps:
    style: "番号付きリスト"

notes:
  - "実演で補完されるため簡潔に"
  - "BANANA GEMINIのUIを見せる"
```

---

# スライド13: 【実演】手順2：立面図から外観パースを作成

```yaml
layout:
  type: "左右分割"
  left: "手順リスト"
  right: "画面イメージ"

copy:
  heading: "【実演】手順2：立面図から外観パースを作成"
  steps:
    - "立面図の画像ファイルをドラッグ＆ドロップ"
    - "「この立面図から外観パースを作成して」と入力"
    - "必要に応じて「明るい雰囲気で」など補足"
    - "生成された画像を確認"
  note: "※気に入らなければ再生成を依頼"

visual:
  right:
    type: "screenshot_placeholder"
    description: "立面図をアップロードして外観パースが生成される様子"
  steps:
    style: "番号付きリスト"

notes:
  - "立面図 → 外観パースの変換を見せる"
  - "AIの出力結果をハイライト"
```

---

# スライド14: 【実演】手順3：土地の写真を取得

```yaml
layout:
  type: "左右分割"
  left: "手順リスト"
  right: "画面イメージ"

copy:
  heading: "【実演】手順3：土地の写真を取得"
  steps:
    - "Googleマップでお客様の建てたい土地を検索"
    - "ストリートビューで土地が見える角度を探す"
    - "スクリーンショットを撮る"
  note: "※土地がよく見える状態でスクショ"

visual:
  right:
    type: "screenshot_placeholder"
    description: "Googleマップのストリートビュー画面"
  steps:
    style: "番号付きリスト"

notes:
  - "Googleマップの操作を見せる"
  - "土地が見える角度の選び方がポイント"
```

---

# スライド15: 【実演】手順4：パースを土地に配置

```yaml
layout:
  type: "左右分割"
  left: "手順リスト"
  right: "画面イメージ"

copy:
  heading: "【実演】手順4：パースを土地に配置"
  steps:
    - "土地の写真をNanoBanana PROにアップロード"
    - "「この土地に、先ほど作成したパースの家を建てて」と指示"
    - "生成された画像を確認"
  note: "※土地に家が配置された画像が出力される"

visual:
  right:
    type: "screenshot_placeholder"
    description: "土地に家が配置された合成画像"
  steps:
    style: "番号付きリスト"

notes:
  - "土地写真 + パース → 合成画像 の流れ"
  - "自然に配置されている様子を強調"
```

---

# スライド16: 【実演】手順5：外観の調整

```yaml
layout:
  type: "左右分割"
  left: "手順リスト"
  right: "画面イメージ"

copy:
  heading: "【実演】手順5：外観の調整（オプション）"
  steps:
    - "「外壁をもう少し白くして」など色味変更を依頼"
    - "「屋根をグレーにして」など素材変更を依頼"
    - "複数パターンを作成して比較"
  note: "※バリエーションを作ってお客様と一緒に選ぶ"

visual:
  right:
    type: "screenshot_placeholder"
    description: "外観の色味を調整している画面"
  steps:
    style: "番号付きリスト"

notes:
  - "色変更のビフォーアフターを見せる"
  - "お客様との打ち合わせで使うイメージ"
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
    - role: "営業担当"
      text: "商談時にその場で外観パースを生成、お客様の土地に配置して提案"
    - role: "設計担当"
      text: "設計段階で外観イメージを確認、色味・素材のバリエーション検討"
    - role: "コーディネーター"
      text: "外壁・屋根の色提案時に複数パターンを作成してお客様と一緒に選定"
  bottom_message: "お客様に「完成イメージ」をリアルに伝えて、満足度アップ"

visual:
  cards:
    - icon: "businessperson"
      color: "navy"
    - icon: "architect"
      color: "navy"
    - icon: "palette"
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
  columns: 3
  card_style: "フラット塗り"

copy:
  heading: "まとめ"
  cards:
    - label: "①"
      text: "立面図から外観パースを一瞬で作成（設計ソフト・外注不要）"
    - label: "②"
      text: "お客様の土地に配置できる（Googleマップ活用）"
    - label: "③"
      text: "色味・素材をその場で変更可能（バリエーション提案）"
  cta:
    prefix: "🚀"
    text: "ぜひお客様への提案にNanoBanana PROを活用して、満足度アップを実感してください！"

visual:
  cards:
    - icon: "image"
    - icon: "map_pin"
    - icon: "palette"
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
  supplement: "新築提案だけでなく、リフォームの外観イメージ提案や建て替えのビフォーアフター比較にも応用できます"

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
| 人物イラスト | いらすとや、ソコスト | 課題提起、Before/After比較、職種別 |
| アイコン | Lucide、PowerPoint内蔵 | メリット説明、フロー図 |
| 画面キャプチャ | NanoBanana PRO実際の画面、Googleマップ | 実演スライド、ツール紹介 |
| 立面図サンプル | 自社CAD出力または素材サイト | 変換前のイメージ |
| 外観パースサンプル | NanoBanana PROで実際に生成 | 変換後のイメージ |
| フロー図 | PowerPoint図形で作成 | 手順説明、全体の流れ |

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
- [x] 実演部分は簡素になっている（5枚）

### 住宅業界向けチェック
- [x] 住宅業界での活用イメージが含まれている
- [x] 職種別おすすめを含めている
- [x] Before/Afterで現場の変化がわかる

### まとめチェック
- [x] まとめスライドで要点が3つに集約されている
- [x] 行動を促すCTA（Call To Action）がある
