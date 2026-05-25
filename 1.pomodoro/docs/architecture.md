# アーキテクチャ概要

Pomodoroタイマーの現在の実装構成を示します。

---

## 全体構成

```
1.pomodoro/
├── app.py                  # Flaskアプリケーション（エントリポイント）
├── templates/
│   └── index.html          # メイン画面テンプレート
├── static/
│   ├── css/
│   │   └── style.css       # スタイルシート
│   └── js/
│       └── app.js          # フロントエンドJavaScript（UIモック）
├── tests/
│   ├── conftest.py         # pytestセットアップ
│   └── test_routes.py      # Flask APIテスト
├── requirements.txt        # Python依存パッケージ
├── features.md             # 機能仕様
└── plan.md                 # 実装計画
```

---

## バックエンド（Flask）

### `app.py`

- **Flaskアプリケーションファクトリ**: `app = Flask(__name__)` で単一アプリインスタンスを生成
- **インメモリ設定ストア**: `_settings` ディクショナリでデフォルト設定を保持（永続化なし）
- **ルーティング**: 3つのルートを直接定義（models / repositories / services レイヤーは未実装）

現在の設計は **フェーズ5（設定API）** 相当の薄いバックエンドです。レイヤード構造（repository / service）はフェーズ7の履歴機能導入時に追加予定です。

---

## フロントエンド（JavaScript）

### `static/js/app.js`

フェーズ1のUIモック実装です。実際のカウントダウンロジックは未実装で、ボタン操作によるUI状態遷移のみを担当します。

**UI状態機械**

```
IDLE ──[開始ボタン]──> RUNNING
RUNNING ──[一時停止ボタン]──> PAUSED
PAUSED ──[再開ボタン]──> RUNNING
RUNNING / PAUSED ──[リセット or スキップ]──> IDLE
```

| 状態 | 説明 |
|------|------|
| `idle` | 未開始（初期状態） |
| `running` | タイマー動作中 |
| `paused` | 一時停止中 |

---

## 依存関係

| パッケージ | バージョン要件 | 用途 |
|---|---|---|
| `flask` | `>=3.0.0` | Webフレームワーク |
| `pytest` | `>=8.0.0` | テストフレームワーク |
| `pytest-flask` | `>=1.3.0` | FlaskのTestクライアント統合 |

---

## 実装フェーズと現在地

| フェーズ | 内容 | 状態 |
|---|---|---|
| フェーズ0 | Flask起動・テンプレート配信 | ✅ 完了 |
| フェーズ1 | UIモック（見た目・操作導線） | ✅ 完了 |
| フェーズ2 | Core状態機械（reducer形式） | 🔲 未着手 |
| フェーズ3 | 時間制御・Controller接続 | 🔲 未着手 |
| フェーズ4 | LocalStorage永続化 | 🔲 未着手 |
| フェーズ5 | Flask設定API連携 | ✅ 完了（APIのみ） |
| フェーズ6 | 通知・音・アクセシビリティ | 🔲 未着手 |
| フェーズ7 | セッション履歴・SQLite | 🔲 未着手 |
