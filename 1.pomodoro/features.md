# Pomodoroタイマー 実装機能一覧

## 1. MVPで必須の機能

### 1.1 画面配信
- Flaskでトップ画面を配信する
- テンプレートと静的ファイルを読み込める構成にする

### 1.2 タイマー基本UI
- 現在モード表示（作業中 / 休憩中）
- 残り時間表示（mm:ss）
- 円形プログレス表示
- 操作ボタン（開始 / 一時停止 / 再開 / リセット / スキップ）
- 今日の進捗表示（完了セッション数、集中時間）

### 1.3 タイマー状態機械（Core）
- 状態: `focus`, `short_break`, `long_break`, `paused`
- イベント: `start`, `pause`, `resume`, `reset`, `skip`, `tick`, `complete`
- reducer形式の純粋関数で状態遷移を定義する
- 不正遷移を防止する（例: 未開始で `pause` 不可）

### 1.4 時間計算ロジック
- `endAt` 基準で残時間を再計算する
- タブ非アクティブ復帰時のズレを補正する
- 0秒到達時に `complete` を発火する

### 1.5 セッション進行ルール
- 作業完了で休憩へ遷移する
- 指定回数ごとに長休憩へ遷移する
- 完了カウントを更新する
- 集中時間を加算する

### 1.6 設定管理（フロント）
- 設定項目を編集できる
  - `focus_minutes`
  - `short_break_minutes`
  - `long_break_minutes`
  - `long_break_interval`
  - `auto_start_break`
  - `auto_start_focus`
  - `notification_enabled`
  - `sound_enabled`
- LocalStorageへ保存・復元する

### 1.7 Flask API（薄いバックエンド）
- `GET /api/settings`
- `PUT /api/settings`
- 入力値バリデーション
- エラーレスポンス設計（400 / 500）

### 1.8 通知と音
- セッション完了時に通知する
- 完了音を再生する
- ブラウザ許可状態をハンドリングする

### 1.9 テスト
- Core状態遷移テスト
- 時間計算テスト（FakeClock）
- Controller / UseCaseテスト
- Flask APIテスト

## 2. MVP後の拡張機能

### 2.1 セッション履歴API
- `POST /api/sessions`
- `GET /api/sessions?date=YYYY-MM-DD`

### 2.2 永続化拡張
- SQLite導入
- 履歴テーブル設計（`planned_seconds`, `actual_seconds`, `completed` など）

### 2.3 UX・アクセシビリティ
- キーボード操作対応
- ARIAラベル整備
- 色コントラスト調整
- モバイル表示最適化

### 2.4 信頼性
- 異常系テスト拡充
- データ破損時の復旧方針
- ログ出力方針

## 3. 実装順（推奨）
1. Flask最小起動と1画面配信
2. Core状態機械と単体テスト
3. UI接続（Controller / Presenter）
4. LocalStorage保存
5. 設定API連携
6. 通知・音・アクセシビリティ
7. 履歴とSQLite（必要時）
