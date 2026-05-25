# API リファレンス

Pomodoroタイマーが提供するREST APIの仕様です。

---

## 共通仕様

| 項目 | 値 |
|------|-----|
| ベースURL | `http://localhost:5000` |
| リクエスト形式 | `application/json` |
| レスポンス形式 | `application/json` |

---

## エンドポイント一覧

### `GET /`

トップ画面（HTMLページ）を返します。

**レスポンス**

- `200 OK` — `text/html` でHTMLページを返す

---

### `GET /api/settings`

現在の設定値を取得します。

**レスポンス例**

```json
{
  "focus_minutes": 25,
  "short_break_minutes": 5,
  "long_break_minutes": 15,
  "long_break_interval": 4,
  "auto_start_break": false,
  "auto_start_focus": false,
  "notification_enabled": true,
  "sound_enabled": true
}
```

**ステータスコード**

| コード | 説明 |
|--------|------|
| `200 OK` | 設定を正常に返却 |

---

### `PUT /api/settings`

設定値を更新します。リクエストボディには更新したいキーのみ含めてください。

**リクエスト例**

```http
PUT /api/settings
Content-Type: application/json

{
  "focus_minutes": 30,
  "auto_start_break": true
}
```

**レスポンス例**

```json
{
  "focus_minutes": 30,
  "short_break_minutes": 5,
  "long_break_minutes": 15,
  "long_break_interval": 4,
  "auto_start_break": true,
  "auto_start_focus": false,
  "notification_enabled": true,
  "sound_enabled": true
}
```

**ステータスコード**

| コード | 説明 |
|--------|------|
| `200 OK` | 更新後の設定全体を返却 |
| `400 Bad Request` | リクエストボディがJSONオブジェクトでない、または不明なキーが含まれる |

**エラーレスポンス例（400）**

```json
{ "error": "リクエストボディはJSONオブジェクトである必要があります" }
```

```json
{ "error": "不明なキー: unknown_key" }
```

---

## 設定フィールド定義

| フィールド名 | 型 | デフォルト値 | 説明 |
|---|---|---|---|
| `focus_minutes` | `integer` | `25` | 作業セッションの長さ（分） |
| `short_break_minutes` | `integer` | `5` | 短休憩の長さ（分） |
| `long_break_minutes` | `integer` | `15` | 長休憩の長さ（分） |
| `long_break_interval` | `integer` | `4` | 長休憩を挟む作業セッション回数 |
| `auto_start_break` | `boolean` | `false` | 作業完了後に休憩を自動開始するか |
| `auto_start_focus` | `boolean` | `false` | 休憩完了後に作業を自動開始するか |
| `notification_enabled` | `boolean` | `true` | ブラウザ通知を有効にするか |
| `sound_enabled` | `boolean` | `true` | 完了音を有効にするか |
