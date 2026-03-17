# Build AI Academy 台本作成プロジェクト

住宅業界特化のAI活用eラーニング「Build AI Academy」のコンテンツ制作プロジェクト。
運営：株式会社SHO-SAN AI事業部

## スキル一覧（`/baa:skill-name` で呼び出し）

| スキル | 説明 | 使い方 |
|--------|------|--------|
| `script-create` | 台本作成（4種類自動判別） | `/baa:script-create NotebookLMの使い方` |
| `slide-outline` | スライドアウトライン作成 | `/baa:slide-outline 台本ファイルパス` |
| `reading-script` | 読み上げ用ファイル作成 | `/baa:reading-script タイトルフォルダパス` |
| `consistency-check` | 台本⇔スライド整合性チェック | `/baa:consistency-check タイトルフォルダパス` |
| `research` | AIツールリサーチ | `/baa:research ツール名` |
| `note-article` | note記事作成 | `/baa:note-article 台本ファイルパス` |
| `line-announce` | LINE告知文作成 | `/baa:line-announce 台本ファイルパス` |
| `audio-generate` | 音声生成（ElevenLabs） | `/baa:audio-generate ファイルパス [--per-slide]` |
| `video-generate` | Remotion動画プロジェクト生成 | `/baa:video-generate フォルダパス --slide-dir PNGフォルダ --component-name Name` |
| `full-pipeline` | 全工程一括実行 | `/baa:full-pipeline トピック [--skip-audio] [--skip-video]` |

## 典型的なワークフロー

```
/baa:research ツール名           # 1. リサーチ
/baa:script-create トピック      # 2. 台本作成
/baa:slide-outline 台本パス      # 3. スライドアウトライン
/baa:reading-script フォルダパス  # 4. 読み上げ用ファイル
/baa:consistency-check フォルダパス # 5. 整合性チェック
/baa:audio-generate ファイルパス  # 6. 音声生成
# （Canvaでスライド画像を作成）      # 7. スライドPNG手動作成（1920x1080 PNG）
/baa:video-generate フォルダパス --slide-dir PNGフォルダ --component-name Name  # 8. 動画プロジェクト生成
```

一括実行: `/baa:full-pipeline トピック`（音声生成まで。スライドPNG作成は手動、動画生成は `/baa:video-generate`）

## 環境構築

### Python

```bash
pip install -r requirements.txt
```

### ElevenLabs 音声生成

`.env` ファイルを作成し、APIキーを設定する（`.env.example` を参照）。

```bash
cp .env.example .env
# .env を編集して ELEVENLABS_API_KEY と ELEVENLABS_VOICE_ID を設定
```

### Whisper 字幕同期（オプション）

動画生成時にWhisperで正確な字幕タイミングを同期する場合:

```bash
brew install ffmpeg
pip install openai-whisper
```

### Remotion 動画生成

```bash
cd remotion && npm install
```

## プロジェクト構成

```
BAA資料作成/
├── baa-script-production/     # スキルプラグイン本体
│   ├── shared/references/     #   共通ルール（文体・フォーマット・フォルダ構成）
│   ├── skills/*/SKILL.md      #   各スキルの定義
│   └── skills/*/references/   #   スキル別ガイドライン
├── scripts/                   # Pythonスクリプト
│   ├── generate_audio.py      #   音声生成メイン
│   ├── generate_video.py      #   Remotion動画プロジェクト生成
│   ├── text_processor.py      #   台本テキスト前処理
│   └── elevenlabs_client.py   #   ElevenLabs APIクライアント
├── remotion/                  # Remotion動画プロジェクト
│   └── src/                   #   動画コンポーネント（詳細は下記）
├── 作成済台本/                 # 作成済みコンテンツ
│   ├── 概念系/                #   概念系の台本・資料・音声
│   ├── ユースケース/           #   ユースケース系
│   ├── ツール解説/             #   ツール解説系
│   └── 比較系/                #   比較系
├── リサーチ済み情報/           # AIツールのリサーチレポート
├── LINE告知文/                # LINE告知文の出力先
├── agent_docs/                # ガイドライン原本（参照用）
├── 参考資料/                  # PDFや外部参考資料
└── LIXIL to BAA/              # LIXIL向け企画書プロジェクト
```

## Remotionプロジェクト

- 場所: `remotion/`
- 共通コンポーネント: `src/AICopyright/Slide.tsx`, `src/AICopyright/Subtitle.tsx`
- 動画エントリー（各動画ごとに1ファイル）:
  - `src/AICopyright.tsx` — AI活用と著作権
  - `src/AIAdKeihin.tsx` — AI広告と景品表示法
  - `src/KoumtenAI.tsx` — 工務店のAI社内推進の仕方
  - `src/GeminiSalesRoleplay.tsx` — Geminiで営業ロープレを強化する方法
  - `src/SeiseiAI.tsx` — 生成AIとは何か
  - `src/PromptDesign.tsx` — AIを上手に扱うポイント プロンプト設計
- プレビュー: `cd remotion && npm run dev`
- レンダリング: `cd remotion && npx remotion render [ComponentName]`
