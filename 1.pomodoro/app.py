from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# デフォルト設定（フェーズ5でAPI永続化予定）
_settings = {
    "focus_minutes": 25,
    "short_break_minutes": 5,
    "long_break_minutes": 15,
    "long_break_interval": 4,
    "auto_start_break": False,
    "auto_start_focus": False,
    "notification_enabled": True,
    "sound_enabled": True,
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/settings", methods=["GET"])
def get_settings():
    return jsonify(_settings)


@app.route("/api/settings", methods=["PUT"])
def update_settings():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "リクエストボディはJSONオブジェクトである必要があります"}), 400

    allowed_keys = set(_settings.keys())
    unknown = set(data.keys()) - allowed_keys
    if unknown:
        return jsonify({"error": f"不明なキー: {', '.join(unknown)}"}), 400

    _settings.update(data)
    return jsonify(_settings)


if __name__ == "__main__":
    app.run(debug=True)
