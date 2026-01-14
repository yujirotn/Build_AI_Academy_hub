# スライドデザインガイド

## 概要

スライドを作成する際のデザインルールを記載します。

---

# presentation_design_spec_for_copy_visual_layout.yaml
# 目的: copy / visual / layout 記法のスライド定義を「表示ルール」と「見た目（デザイン）」で安全にレンダリングするためのデザイン仕様
# コンセプト: 「白い紙面に、ネイビーの信頼とオレンジの前向きを“道しるべ”として添える」

rendering_contract:
  # 重要: “指示文がスライドに印字される事故”を構造で防ぐ
  display_text_sources:
    - "copy"         # スライドに表示してよいテキストは copy 配下のみ
  never_render_as_text:
    - "layout"       # レイアウト指示（非表示）
    - "visual"       # 図解/イラスト/アイコン指定（非表示）
    - "notes"        # 補足指示（非表示）
  allowed_text_fields_examples:
    - "copy.title"
    - "copy.subtitle"
    - "copy.body"
    - "copy.bullets[]"
    - "copy.cards[].heading"
    - "copy.cards[].text"
    - "copy.table.headers[]"
    - "copy.table.rows[][]"
  # 例外: 画面上にラベルとして表示したい文字がある場合は copy 側に明示して入れる
  visual_label_rule: "ラベル表示が必要な場合のみ copy に書く（例: copy.badges[].text）。visual 側に文章を入れない。"

document:
  ratio: "16:9"
  base_layout_grid:
    columns: 12
    gutters: 24
    margins:
      left: 72
      right: 72
      top: 54
      bottom: 54
  background:
    fill: "#FFFFFF"  # (ホワイト)
    texture: "none"

design_tokens:
  color:
    base: "#FFFFFF"          # ホワイト
    ink: "#1F2937"           # チャコールグレー（本文）
    navy: "#0B2D4B"          # ディープネイビー（見出し/主要）
    slate: "#4A6B85"         # スレートブルー（補助）
    orange: "#F28C1B"        # アンバーオレンジ（アクセント）
    line: "#D7DEE6"          # ライトグレー（罫線）
    card_bg: "#F3F6F9"       # ペールグレー（カード）
    highlight_bg: "#FFF4E6"  # ペールオレンジ（強調枠）
    danger: "#D94841"        # 注意（必要時のみ）
    success: "#2F855A"       # 成功（必要時のみ）
  typography:
    font_families:
      jp: ["Noto Sans JP", "Hiragino Kaku Gothic ProN", "Yu Gothic", "Meiryo", "sans-serif"]
      en: ["Inter", "Roboto", "system-ui", "sans-serif"]
    scale:  # 16:9 / 録画視聴想定（小さくしない）
      h1: { size: 44, weight: 800, line_height: 1.15, letter_spacing: 0.0, color: "#0B2D4B" }
      h2: { size: 34, weight: 800, line_height: 1.18, letter_spacing: 0.0, color: "#0B2D4B" }
      h3: { size: 26, weight: 700, line_height: 1.22, letter_spacing: 0.0, color: "#0B2D4B" }
      body_l: { size: 24, weight: 500, line_height: 1.45, color: "#1F2937" }
      body: { size: 22, weight: 500, line_height: 1.5, color: "#1F2937" }
      body_s: { size: 20, weight: 500, line_height: 1.5, color: "#1F2937" }
      caption: { size: 16, weight: 500, line_height: 1.35, color: "#4A6B85" }
      badge: { size: 16, weight: 700, line_height: 1.0, color: "#0B2D4B" }
      mono_number: { size: 22, weight: 700, line_height: 1.1, font: "en", tabular: true, color: "#0B2D4B" }
  radius:
    card: 16
    pill: 999
    bubble: 18
    tag: 10
  shadow:
    card: { x: 0, y: 8, blur: 24, spread: 0, color: "rgba(11,45,75,0.10)" }
    float: { x: 0, y: 12, blur: 34, spread: 0, color: "rgba(11,45,75,0.14)" }
  stroke:
    thin: 1
    medium: 2
  spacing:
    section_gap: 28
    item_gap: 16
    card_padding: 20
    bubble_padding: 18

visual_style:
  illustration:
    style: "フラット塗り（親しみやすい）"
    outline: "なし（必要時のみ #D7DEE6 で薄く）"
    palette: ["#0B2D4B", "#4A6B85", "#F28C1B", "#F3F6F9", "#FFFFFF"]
    character_tone: "営業担当・設計担当などは“穏やかな表情”で、困り→解決の対比が分かる"
  icons:
    style: "フラット塗り"
    primary_color: "#0B2D4B"
    accent_color: "#F28C1B"
    size_default: 28
    mapping_suggestions:
      search: "🔍"
      calculator: "🧮"
      clock: "⏰"
      repeat: "🔄"
      info: "ⓘ"
      warning: "⚠️"
      check: "✅"
      document: "📄"
      pdf: "📕"
  screenshot_frame:
    frame: { radius: 16, stroke: "#D7DEE6", stroke_width: 1, fill: "#FFFFFF" }
    title_bar: { show: true, height: 18, dot_colors: ["#F87171", "#FBBF24", "#34D399"] }
    caption_style: "caption"

components:
  header:
    # ほぼ全スライド共通の“上部見出し帯”
    area: { x: 72, y: 44, w: "calc(100%-144)", h: 70 }
    title_style: "h2"
    divider:
      show: true
      color: "#D7DEE6"
      thickness: 1
      offset_y: 64
  subheader:
    style: "body_s"
    color: "#4A6B85"

  badge:
    shape: "pill"
    padding: { x: 14, y: 8 }
    variants:
      level_beginner:
        fill: "#FFF4E6"
        stroke: "#F28C1B"
        text_color: "#0B2D4B"
        icon: "check"
      date:
        fill: "#F3F6F9"
        stroke: "#D7DEE6"
        text_color: "#0B2D4B"
  callout:
    # 下部メッセージ（強調枠）用
    container:
      fill: "#FFF4E6"
      stroke: "#F28C1B"
      stroke_width: 2
      radius: 16
      padding: { x: 18, y: 14 }
    text_style: "body"
    emphasis:
      method: "accent_bar_left"
      bar_color: "#F28C1B"
      bar_width: 6
  card:
    base:
      fill: "#F3F6F9"
      stroke: "#D7DEE6"
      stroke_width: 1
      radius: 16
      shadow: "card"
      padding: { x: 20, y: 18 }
    heading_style: "h3"
    body_style: "body_s"
  checklist:
    bullet_icon: "check"
    bullet_color: "#F28C1B"
    text_style: "body"
    row_gap: 14
  speech_bubble:
    fill: "#FFFFFF"
    stroke: "#D7DEE6"
    stroke_width: 2
    radius: 18
    tail: { show: true, size: 14 }
    text_style: "body_s"
  table:
    header:
      fill: "#F3F6F9"
      text_style: "body_s"
      text_color: "#0B2D4B"
    body:
      fill: "#FFFFFF"
      text_style: "body_s"
      text_color: "#1F2937"
    grid:
      stroke: "#D7DEE6"
      stroke_width: 1
    zebra: { show: true, fill: "#FBFCFD" }

layout_templates:
  # layout.type をこの一覧に揃えると、copy/visual の解釈が安定します
  - type: "cover_center"
    description: "タイトル中央配置。左上ロゴ（任意）、バッジ2つ、下にサブコピー。イラストは下部〜中央に大きく。"
    regions:
      logo: { x: 72, y: 44, w: 260, h: 40, show_if: "visual.logo != null" }
      title: { x: 72, y: 160, w: "calc(100%-144)", h: 140, align: "center" }
      subtitle: { x: 120, y: 310, w: "calc(100%-240)", h: 60, align: "center" }
      badges: { x: 72, y: 90, w: "calc(100%-144)", h: 44, align: "right" }
      hero_illustration: { x: 180, y: 380, w: "calc(100%-360)", h: 300 }

  - type: "illustration_with_bubbles"
    description: "中央にイラスト、周囲に吹き出し。下部に強調枠の結論。"
    regions:
      header: { use_component: "header" }
      center_illustration: { x: 260, y: 170, w: "calc(100%-520)", h: 300 }
      bubbles:
        positions:
          - { x: 72, y: 190, w: 340, h: 120 }
          - { x: "calc(100%-412)", y: 200, w: 340, h: 120 }
          - { x: 120, y: 340, w: 380, h: 120 }
      callout: { x: 72, y: 520, w: "calc(100%-144)", h: 140 }

  - type: "hero_message_flow"
    description: "中央に強いメッセージ＋下にサブ。中央付近に困り→ロゴ→笑顔の簡易フロー。下部に箇条のベネフィット枠。"
    regions:
      header: { use_component: "header" }
      hero_message: { x: 120, y: 170, w: "calc(100%-240)", h: 120, align: "center" }
      flow: { x: 220, y: 300, w: "calc(100%-440)", h: 140 }
      sub_message: { x: 120, y: 450, w: "calc(100%-240)", h: 60, align: "center" }
      callout: { x: 72, y: 520, w: "calc(100%-144)", h: 140 }

  - type: "checklist_with_screenshot"
    description: "左にチェックリスト、右に画面イメージ（スクショ枠）。下部に励ましメッセージ枠。"
    regions:
      header: { use_component: "header" }
      checklist: { x: 72, y: 170, w: 620, h: 360 }
      screenshot: { x: 720, y: 170, w: "calc(100%-792)", h: 360 }
      callout: { x: 72, y: 550, w: "calc(100%-144)", h: 110 }

  - type: "two_column_explain_screenshot"
    description: "左に説明テキスト（定義/概要）、右にロゴ＋画面キャプチャ。下に一言の比喩。"
    regions:
      header: { use_component: "header" }
      left_text: { x: 72, y: 170, w: 620, h: 390 }
      right_visual: { x: 720, y: 170, w: "calc(100%-792)", h: 390 }
      footer_note: { x: 72, y: 575, w: "calc(100%-144)", h: 60 }

  - type: "info_cards_grid"
    description: "基本情報をカードで整理（2x2 または 3x2）。アイコン付き。"
    regions:
      header: { use_component: "header" }
      cards_grid: { x: 72, y: 170, w: "calc(100%-144)", h: 460, grid: { cols: 2, rows: 2, gap: 18 } }
      footer_note: { x: 72, y: 635, w: "calc(100%-144)", h: 40 }

  - type: "three_benefits_row"
    description: "メリット3つを横並びカード。中央タイトル、下に誘導文。"
    regions:
      header: { use_component: "header" }
      cards_row: { x: 72, y: 220, w: "calc(100%-144)", h: 300, grid: { cols: 3, gap: 18 } }
      footer_note: { x: 72, y: 545, w: "calc(100%-144)", h: 60 }

  - type: "before_after_split"
    description: "左右2分割（Before/After）。各側に短文＋イラスト。下部に強調枠。"
    regions:
      header: { use_component: "header" }
      left: { x: 72, y: 170, w: "calc((100%-162)/2)", h: 380 }
      right: { x: "calc(72 + (100%-162)/2 + 18)", y: 170, w: "calc((100%-162)/2)", h: 380 }
      callout: { x: 72, y: 570, w: "calc(100%-144)", h: 90 }

  - type: "flow_steps_center"
    description: "フロー図中心（設定→質問→出力）。下に強調枠。"
    regions:
      header: { use_component: "header" }
      flow: { x: 120, y: 210, w: "calc(100%-240)", h: 300 }
      steps_table: { x: 120, y: 510, w: "calc(100%-240)", h: 120 }

  - type: "radial_usecases"
    description: "中央にNotebookLM、周囲に活用例を放射状。下部に強調枠。"
    regions:
      header: { use_component: "header" }
      center: { x: "calc(50%-110)", y: 240, w: 220, h: 220 }
      satellites: { count: 6, radius: 260, card_w: 220, card_h: 90 }
      callout: { x: 72, y: 590, w: "calc(100%-144)", h: 80 }

  - type: "demo_steps_with_screenshot"
    description: "左に手順ステップ、右に画面イメージ。注記はcaptionで。"
    regions:
      header: { use_component: "header" }
      steps: { x: 72, y: 170, w: 620, h: 430 }
      screenshot: { x: 720, y: 170, w: "calc(100%-792)", h: 430 }
      note: { x: 72, y: 615, w: "calc(100%-144)", h: 40 }

  - type: "warning_list"
    description: "警告アイコン付きのリスト。カード背景で可読性を上げる。"
    regions:
      header: { use_component: "header" }
      list_card: { x: 72, y: 190, w: "calc(100%-144)", h: 430 }
      footer_note: { x: 72, y: 635, w: "calc(100%-144)", h: 40 }

  - type: "role_cards_3col"
    description: "職種別おすすめ（3カラムカード）。下部に強調枠。"
    regions:
      header: { use_component: "header" }
      cards_row: { x: 72, y: 220, w: "calc(100%-144)", h: 320, grid: { cols: 3, gap: 18 } }
      callout: { x: 72, y: 565, w: "calc(100%-144)", h: 90 }

  - type: "summary_cards_4col"
    description: "まとめ（4カード横並び）。アイコン＋短文。"
    regions:
      header: { use_component: "header" }
      cards_row: { x: 72, y: 230, w: "calc(100%-144)", h: 320, grid: { cols: 4, gap: 16 } }

content_mapping_rules:
  # copy/visual/layout の各要素が、どのコンポーネントに流し込まれるか
  title_handling:
    source: "copy.title"
    component: "header.title_style"
  subtitle_handling:
    source: "copy.subtitle"
    component: "subheader"
  badges_handling:
    source: "copy.badges[]"
    component: "badge"
    examples:
      - { kind: "level", variant: "level_beginner" }
      - { kind: "date", variant: "date" }
  callout_handling:
    source: "copy.callout"
    component: "callout"
  bullets_handling:
    source: "copy.bullets[]"
    component: "checklist"
  cards_handling:
    source: "copy.cards[]"
    component: "card"
  table_handling:
    source: "copy.table"
    component: "table"
  visual_assets:
    illustration: "visual.illustration"
    screenshot: "visual.screenshot"
    icons: "visual.cards[].icon"
    flow: "visual.flow"

quality_rules:
  readability:
    max_bullets_per_slide: 5
    max_lines_per_bullet: 1
    avoid_small_text_below: 18
  emphasis:
    accent_usages_per_slide_max: 2
    method_priority: ["badge", "callout", "underline_orange", "icon_accent"]
  japanese_text:
    punctuation: "全角優先（、。）"
    english_terms:
      style: "角丸ラベル（枠:#D7DEE6、下線:#F28C1B）"
      font: "en"

# 備考:
# - スライド定義側で layout.type を layout_templates の type 名に合わせると、見た目がブレにくい
# - 例: スライド1=cover_center, スライド2=illustration_with_bubbles, スライド3=hero_message_flow ... のように指定
