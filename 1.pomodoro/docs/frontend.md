# フロントエンド モジュールドキュメント

---

## ファイル構成

```
static/
├── css/
│   └── style.css    # グローバルスタイルシート
└── js/
    └── app.js       # UIロジック（フェーズ1 UIモック）

templates/
└── index.html       # メイン画面テンプレート
```

---

## `static/js/app.js`

フェーズ1のUIモック実装です。実際のカウントダウンロジック（フェーズ2〜3で実装予定）は含まれていません。

### 定数

| 定数名 | 値 | 説明 |
|---|---|---|
| `RING_CIRCUMFERENCE` | `2 * Math.PI * 80 ≈ 502.65` | プログレスリングの円周（`r=80`） |

### UI状態（`State`）

```javascript
const State = Object.freeze({
  IDLE: 'idle',       // 未開始
  RUNNING: 'running', // 動作中
  PAUSED: 'paused',   // 一時停止中
});
```

### DOM参照

| 変数名 | 対応するHTML要素 | 説明 |
|---|---|---|
| `modeLabel` | `#mode-label` | 現在モード表示（「作業中」など） |
| `timeDisplay` | `#time-display` | 残り時間表示（`mm:ss`形式） |
| `ringFill` | `#progress-ring-fill` | SVGプログレスリング（塗りつぶし部分） |
| `btnStart` | `#btn-start` | 開始/一時停止/再開ボタン |
| `btnSkip` | `#btn-skip` | スキップボタン |
| `btnReset` | `#btn-reset` | リセットボタン |

### 関数

#### `setProgress(ratio)`

プログレスリングの充填率を設定します。

| 引数 | 型 | 説明 |
|---|---|---|
| `ratio` | `number` | `1.0` = 満タン、`0.0` = 空。範囲外の値はクランプされる |

SVGの `stroke-dashoffset` を計算することでリングのアニメーションを制御します。

```javascript
const offset = RING_CIRCUMFERENCE * (1 - Math.max(0, Math.min(1, ratio)));
ringFill.style.strokeDashoffset = offset;
```

#### `updateUI()`

現在のUIステート（`currentState`）に応じてボタン表示と `aria-label` を更新します。

| 状態 | `btnStart` テキスト | `btnSkip` 表示 |
|---|---|---|
| `IDLE` | `開始` | 非表示 |
| `RUNNING` | `一時停止` | 表示 |
| `PAUSED` | `再開` | 表示 |

### イベントハンドラ

| ボタン | アクション |
|---|---|
| `btnStart` | `IDLE→RUNNING→PAUSED→RUNNING` のサイクルで状態遷移 |
| `btnReset` | 状態を`IDLE`に戻し、表示を`25:00`・プログレス満タンにリセット |
| `btnSkip` | リセットと同じ動作（現状はIDLEに戻すのみ） |

---

## `static/css/style.css`

### 主要CSSクラス

| クラス名 | 説明 |
|---|---|
| `.timer-card` | タイマー全体のカードコンテナ（幅340px、白背景） |
| `.card-titlebar` | タイトルバー（タイトルとウィンドウ風コントロール） |
| `.mode-label` | 現在モード表示テキスト（`aria-live="polite"` 対応） |
| `.progress-ring-container` | SVGプログレスリングのコンテナ（200×200px） |
| `.progress-ring` | SVG要素（12時方向スタートのため`-90deg`回転） |
| `.progress-ring__track` | リングのトラック（背景円）`stroke: #EEEEF8` |
| `.progress-ring__fill` | リングの進捗部分 `stroke: #6466F1`、アニメーション`0.5s linear` |
| `.time-display` | 残り時間テキスト（リング中央に絶対配置） |
| `.btn` | ボタン共通スタイル（角丸、トランジション） |
| `.btn-primary` | プライマリボタン（青系: `#3B3DB4`） |
| `.btn-secondary` | セカンダリボタン（白背景、灰色ボーダー） |
| `.progress-card` | 今日の進捗カード（薄紫背景: `#F4F4FC`） |
| `.stat-value` | 進捗数値（大フォント） |
| `.stat-value.stat-highlight` | ハイライト数値（青紫: `#5B5BD6`） |

---

## `templates/index.html`

Jinja2テンプレート（Flaskが配信）。現状は静的HTMLとして機能します。

### 主要HTML要素

| ID | 役割 |
|---|---|
| `#mode-label` | 現在のモード表示（`aria-live="polite"`） |
| `#time-display` | 残り時間表示（初期値`25:00`） |
| `#progress-ring-fill` | SVGプログレスリング塗りつぶし要素 |
| `#btn-start` | 開始/一時停止/再開ボタン |
| `#btn-skip` | スキップボタン（初期は非表示） |
| `#btn-reset` | リセットボタン |
| `#completed-count` | 今日の完了セッション数（現在はダミー値`4`） |
| `#focus-time` | 今日の集中時間（現在はダミー値`1時間40分`） |
