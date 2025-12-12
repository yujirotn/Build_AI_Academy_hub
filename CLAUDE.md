# Build AI Academy 台本作成ガイド

## Build AI Academyとは

- 住宅業界特化のAI活用eラーニングプラットフォーム
- 運営：株式会社SHO-SAN AI事業部
- 目的：現場で「今日から使える」AIスキルを身につける

## 視聴者像

- 住宅・建設会社の社員（営業、事務、現場監督など）
- 年齢層：30-50代中心
- ITスキル：Excel基本操作ができるレベル
- 視聴状況：業務の合間、移動中、自宅学習

## 台本の文体ルール

- 口語調で書く（「です・ます」＋「〜ですね」「〜してみましょう」）
- 一文は話して15秒以内（約40字）
- 専門用語は初出時に必ず言い換え・補足
- 「では」「それでは」で場面転換を明示

## 台本フォーマット

3列構成で記載すること：
| 時間 | ナレーション | 画面指示 |

## スライド用アウトライン

- [`agent_docs/material_outline_method.md`](agent_docs/material_outline_method.md)

## フォルダ構成

- `作成済台本/`
  - `ユースケース/` - ユースケース系の台本とスライド用アウトラインを格納
  - `概念系/` - 概念系の台本とスライド用アウトラインを格納
  - `ツール解説/` - ツール系の台本とスライド用アウトラインを格納
- `リサーチ済み情報/` - AIツールのリサーチ結果を格納
- `agent_docs/` - 資料作成と台本作成ガイドライン
  - `usecase_method.md` - ユースケース系台本の書き方
  - `general_method.md` - 概念系台本の書き方
  - `tool_howto.md` - ツール系の台本の書き方
  - `material_outline_method.md` - ジャンル共通の資料作成方法
  - `material_design.md` - スライドを作成する際のデザイン
  - `search_info.md` - AIツール情報収集エージェントプロンプト

## リサーチルール

ユーザーからAIツールのリサーチを依頼された場合：

1. [`agent_docs/search_info.md`](agent_docs/search_info.md) に従って情報収集を行う
2. リサーチ結果は `リサーチ済み情報/` フォルダにMDファイルとして保存する
3. ファイル命名規則: `YYYY-MM-DD_ツール名.md`

## 台本作成ルール

### ファイル形式

- 台本はMarkdown（.md）ファイルで作成する

### 必須記載項目

- **作成日**: 台本が作成された日付（YYYY-MM-DD形式）
- **タイトル**: 台本のタイトル

### ファイル命名規則

- `YYYY-MM-DD_ジャンル_タイトル.md` の形式で保存する

## 台本の種類

台本は大きく3種類に分類される。種類によって構成・書き方が異なる。

| 種類 | 説明 | 例 | 書き方ガイド |
|------|------|-----|-------------|
| **ユースケース系** | 特定のAIツールを使った実践的な活用方法を紹介 | NotebookLMでカタログ検索、ChatGPTで議事録作成 | [`agent_docs/usecase_method.md`](agent_docs/usecase_method.md) |
| **概念系** | AIの基礎知識や考え方、業界動向などを解説 | 生成AIとは何か、プロンプトの基本 | [`agent_docs/general_method.md`](agent_docs/general_method.md) |
| **ツール解説** | AIツールの基本的な使い方を解説 | ChatGPTの始め方、Geminiの使い方 | [`agent_docs/tool_howto.md`](agent_docs/tool_howto.md) |
