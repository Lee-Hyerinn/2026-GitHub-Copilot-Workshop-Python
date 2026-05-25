# データモデル仕様

---

## 現在の実装

現時点では永続化レイヤー（データベース）は未実装です。設定値は `app.py` のインメモリ辞書 `_settings` に保持されます。サーバーを再起動するとデフォルト値にリセットされます。

---

## 設定モデル（`_settings`）

`GET /api/settings` および `PUT /api/settings` で扱う設定オブジェクトの定義です。

```python
_settings = {
    "focus_minutes": 25,          # int  — 作業セッション長（分）
    "short_break_minutes": 5,     # int  — 短休憩長（分）
    "long_break_minutes": 15,     # int  — 長休憩長（分）
    "long_break_interval": 4,     # int  — 長休憩を挟む作業回数
    "auto_start_break": False,    # bool — 作業完了後に休憩を自動開始
    "auto_start_focus": False,    # bool — 休憩完了後に作業を自動開始
    "notification_enabled": True, # bool — ブラウザ通知の有効化
    "sound_enabled": True,        # bool — 完了音の有効化
}
```

### バリデーションルール（`PUT /api/settings`）

- リクエストボディは JSON オブジェクトでなければならない
- 許可キー以外（`_settings` に存在しないキー）は `400 Bad Request` を返す
- 型チェックは現在実施していない（将来的に追加予定）

---

## 将来のデータモデル（未実装）

以下はフェーズ7で実装予定のセッション履歴モデルです（現在のコードには存在しません）。

### セッション履歴テーブル（SQLite 予定）

| カラム名 | 型 | 説明 |
|---|---|---|
| `id` | `INTEGER PRIMARY KEY` | 自動採番ID |
| `session_type` | `TEXT` | `focus` / `short_break` / `long_break` |
| `planned_seconds` | `INTEGER` | 予定秒数 |
| `actual_seconds` | `INTEGER` | 実際の経過秒数 |
| `completed` | `BOOLEAN` | セッションが完了したか |
| `started_at` | `DATETIME` | 開始日時 |
| `ended_at` | `DATETIME` | 終了日時 |
