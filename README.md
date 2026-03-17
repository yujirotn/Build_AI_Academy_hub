# Build AI Academy — コンテンツ制作パイプライン

住宅業界特化 AI eラーニング「**Build AI Academy**」の台本・スライド・音声・動画を一気通貫で制作するためのリポジトリです。

> 運営：株式会社SHO-SAN AI事業部

---

## 概要

**Build AI Academy（BAA）** は、工務店・住宅会社向けに AI 活用スキルを体系的に学べる eラーニングサービスです。

このリポジトリは、講座コンテンツの **制作パイプライン** を担います。

- リサーチ → 台本作成 → スライド設計 → 音声合成 → 動画レンダリング
- Claude Code のスキルコマンド（`/baa:*`）で各工程を自動化
- ElevenLabs（音声）+ Remotion（動画）による制作自動化

---

## ディレクトリ構成

```
BAA資料作成FMT/
├── CLAUDE.md                    # スキル定義・ワークフロー・環境構築
├── requirements.txt             # Python依存パッケージ
├── .env.example                 # 環境変数テンプレート
│
├── scripts/                     # Python自動化ツール群
│   ├── generate_audio.py        #   音声生成メイン（ElevenLabs）
│   ├── generate_video.py        #   Remotion動画プロジェクト生成
│   ├── text_processor.py        #   台本テキスト前処理
│   └── elevenlabs_client.py     #   ElevenLabs APIクライアント
│
├── remotion/                    # Remotion動画合成プロジェクト
│   └── src/                     #   動画コンポーネント（React + Tailwind）
│
├── baa-script-production/       # スキルプラグイン本体（symlink）
│   ├── shared/references/       #   共通ルール（文体・フォーマット）
│   ├── skills/*/SKILL.md        #   各スキルの定義
│   └── skills/*/references/     #   スキル別ガイドライン
│
├── agent_docs/                  # コンテンツガイドライン原本
│   ├── general_method.md        #   概念系テンプレート
│   ├── tool_howto.md            #   ツール解説テンプレート
│   ├── usecase_method.md        #   ユースケーステンプレート
│   ├── comparison_method.md     #   比較系テンプレート
│   ├── material_outline_method_v2.md  # スライドアウトライン設計
│   ├── material_design.md       #   スライドデザインガイド
│   ├── note_writing.md          #   note記事ガイド
│   ├── LINE告知文.md             #   LINE告知文テンプレート
│   └── search_info.md           #   リサーチガイド
│
├── 作成済台本/                   # 作成済みコンテンツ格納
│   ├── 概念系/
│   ├── ツール解説/
│   ├── ユースケース/
│   └── 比較系/
│
├── LINE告知文/                   # LINE告知文の出力先
└── LIXIL to BAA/                 # LIXIL向け企画書プロジェクト
```

---

## セットアップ

### 1. Python環境

```bash
pip install -r requirements.txt
```

依存パッケージ: `elevenlabs`, `python-dotenv`, `pydub`, `requests`

### 2. 環境変数

```bash
cp .env.example .env
```

`.env` を編集して以下を設定:

| 変数名 | 説明 |
|--------|------|
| `ELEVENLABS_API_KEY` | ElevenLabs APIキー |
| `ELEVENLABS_VOICE_ID` | 使用する音声ID |
| `ELEVENLABS_MODEL_ID` | モデルID（デフォルト: `eleven_ttv_v3`） |

### 3. Remotion（動画生成）

```bash
cd remotion && npm install
```

### 4. Whisper（オプション — 字幕同期）

```bash
brew install ffmpeg
pip install openai-whisper
```

---

## ワークフロー（制作パイプライン）

```
リサーチ → 台本作成 → スライドアウトライン → 読み上げファイル → 整合性チェック
    → 音声生成 → スライドPNG作成(手動/Canva) → 動画プロジェクト生成 → プレビュー → レンダリング
```

### スキルコマンド一覧

| # | スキル | コマンド | 説明 |
|---|--------|----------|------|
| 1 | リサーチ | `/baa:research ツール名` | AIツールの情報収集 |
| 2 | 台本作成 | `/baa:script-create トピック` | 4種類を自動判別して台本生成 |
| 3 | スライドアウトライン | `/baa:slide-outline 台本パス` | スライド構成を設計 |
| 4 | 読み上げファイル | `/baa:reading-script フォルダパス` | 音声合成用テキスト生成 |
| 5 | 整合性チェック | `/baa:consistency-check フォルダパス` | 台本⇔スライドの整合性検証 |
| 6 | 音声生成 | `/baa:audio-generate ファイルパス` | ElevenLabsで音声合成 |
| 7 | スライドPNG | *（Canva等で手動作成 — 1920×1080 PNG）* | — |
| 8 | 動画生成 | `/baa:video-generate フォルダパス --slide-dir PNGフォルダ --component-name Name` | Remotionプロジェクト生成 |
| 9 | note記事 | `/baa:note-article 台本パス` | note掲載用記事を生成 |
| 10 | LINE告知文 | `/baa:line-announce 台本パス` | LINE配信用の告知文を生成 |

### 一括実行

```bash
/baa:full-pipeline トピック
```

音声生成まで一括実行。スライドPNG作成は手動、動画生成は `/baa:video-generate` で個別実行。

---

## 主要コンポーネント

### scripts/ — Python自動化ツール

| ファイル | 役割 |
|----------|------|
| `generate_audio.py` | 台本テキストをElevenLabsで音声ファイルに変換 |
| `generate_video.py` | Remotion動画プロジェクトのTSXファイルを自動生成 |
| `text_processor.py` | 台本テキストの前処理（分割・整形） |
| `elevenlabs_client.py` | ElevenLabs APIとの通信を担当 |

### remotion/ — 動画合成パイプライン

- **フレームワーク**: Remotion 4.x + React 19 + Tailwind CSS 4
- **共通コンポーネント**: `src/AICopyright/Slide.tsx`, `Subtitle.tsx`
- **プレビュー**: `cd remotion && npm run dev`
- **レンダリング**: `cd remotion && npx remotion render [ComponentName]`

### agent_docs/ — コンテンツガイドライン

台本の種別ごとにテンプレートとルールを定義。スキルコマンド実行時に自動参照される。

### baa-script-production/ — スキルプラグイン

Claude Code のスキル定義本体。`shared/references/` に共通ルール、`skills/*/SKILL.md` に各スキルの実行ロジックを格納。

---

## 動画仕様

| 項目 | 仕様 |
|------|------|
| 解像度 | 1920 × 1080（Full HD） |
| FPS | 30fps |
| スライド画像 | PNG形式 |
| 音声 | ElevenLabs TTS（`eleven_ttv_v3`モデル） |
| 字幕同期 | Whisper（オプション） |
| レンダリング | Remotion CLI |

---

## コンテンツ種別

台本は以下の4種類に自動分類され、対応するテンプレートで生成されます。

| 種別 | 説明 | 例 |
|------|------|----|
| **概念系** | AI技術・制度の基礎知識を解説 | 生成AIとは何か、AI活用と著作権 |
| **ツール解説** | 具体的なAIツールの使い方をステップ形式で紹介 | ChatGPT Codex解説、NotebookLM活用術 |
| **ユースケース** | 住宅業界の実務での活用シーンを紹介 | Geminiで営業ロープレを強化する方法 |
| **比較系** | 複数ツール・手法を比較して最適解を提示 | — |

---

## ライセンス

UNLICENSED — 社内プロジェクト
