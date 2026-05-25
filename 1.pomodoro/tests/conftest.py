import sys
import os

# 1.pomodoro/ をパスに追加して app モジュールをインポート可能にする
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
