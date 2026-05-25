/**
 * app.js — フェーズ1 UIモック
 *
 * 実際のカウントダウンロジックはフェーズ2〜3で実装する。
 * ここではボタン操作によるUI状態遷移のみを担当する。
 */

'use strict';

// ---- 定数 ----
const RING_CIRCUMFERENCE = 2 * Math.PI * 80; // ≈ 502.65 (r=80)

// ---- UI状態 ----
const State = Object.freeze({
  IDLE: 'idle',
  RUNNING: 'running',
  PAUSED: 'paused',
});

let currentState = State.IDLE;

// ---- DOM参照 ----
const modeLabel     = document.getElementById('mode-label');
const timeDisplay   = document.getElementById('time-display');
const ringFill      = document.getElementById('progress-ring-fill');
const btnStart      = document.getElementById('btn-start');
const btnSkip       = document.getElementById('btn-skip');
const btnReset      = document.getElementById('btn-reset');

// ---- ヘルパー ----

/**
 * プログレスリングの充填率を設定する。
 * @param {number} ratio - 1.0=満タン, 0.0=空
 */
function setProgress(ratio) {
  const offset = RING_CIRCUMFERENCE * (1 - Math.max(0, Math.min(1, ratio)));
  ringFill.style.strokeDashoffset = offset;
}

/** 現在のUIステートに応じてボタン表示を更新する */
function updateUI() {
  switch (currentState) {
    case State.IDLE:
      btnStart.textContent = '開始';
      btnStart.setAttribute('aria-label', 'タイマー開始');
      btnSkip.style.display = 'none';
      break;
    case State.RUNNING:
      btnStart.textContent = '一時停止';
      btnStart.setAttribute('aria-label', 'タイマーを一時停止');
      btnSkip.style.display = '';
      break;
    case State.PAUSED:
      btnStart.textContent = '再開';
      btnStart.setAttribute('aria-label', 'タイマーを再開');
      btnSkip.style.display = '';
      break;
  }
}

// ---- イベントハンドラ ----

btnStart.addEventListener('click', () => {
  switch (currentState) {
    case State.IDLE:
      currentState = State.RUNNING;
      break;
    case State.RUNNING:
      currentState = State.PAUSED;
      break;
    case State.PAUSED:
      currentState = State.RUNNING;
      break;
  }
  updateUI();
});

btnReset.addEventListener('click', () => {
  currentState = State.IDLE;
  timeDisplay.textContent = '25:00';
  timeDisplay.setAttribute('aria-label', '残り時間 25分00秒');
  modeLabel.textContent = '作業中';
  setProgress(1.0);
  updateUI();
});

btnSkip.addEventListener('click', () => {
  currentState = State.IDLE;
  timeDisplay.textContent = '25:00';
  timeDisplay.setAttribute('aria-label', '残り時間 25分00秒');
  modeLabel.textContent = '作業中';
  setProgress(1.0);
  updateUI();
});

// ---- 初期化 ----
setProgress(1.0);
updateUI();
