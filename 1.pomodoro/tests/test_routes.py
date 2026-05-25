"""
フェーズ0+1 — Flask ルートおよびUI要素の存在確認テスト
"""
import pytest
from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


class TestIndexRoute:
    """GET / の疎通とUI主要要素の存在確認"""

    def test_returns_200(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_contains_mode_label(self, client):
        html = client.get("/").data.decode("utf-8")
        assert 'id="mode-label"' in html

    def test_contains_time_display(self, client):
        html = client.get("/").data.decode("utf-8")
        assert 'id="time-display"' in html

    def test_contains_start_button(self, client):
        html = client.get("/").data.decode("utf-8")
        assert 'id="btn-start"' in html

    def test_contains_skip_button(self, client):
        html = client.get("/").data.decode("utf-8")
        assert 'id="btn-skip"' in html

    def test_contains_reset_button(self, client):
        html = client.get("/").data.decode("utf-8")
        assert 'id="btn-reset"' in html

    def test_contains_progress_ring(self, client):
        html = client.get("/").data.decode("utf-8")
        assert "progress-ring" in html

    def test_contains_today_progress_card(self, client):
        html = client.get("/").data.decode("utf-8")
        assert "今日の進捗" in html


class TestSettingsAPI:
    """GET /api/settings — デフォルト設定の返却確認"""

    def test_returns_200(self, client):
        response = client.get("/api/settings")
        assert response.status_code == 200

    def test_returns_json(self, client):
        response = client.get("/api/settings")
        assert response.content_type == "application/json"

    def test_has_focus_minutes(self, client):
        data = client.get("/api/settings").get_json()
        assert data["focus_minutes"] == 25

    def test_has_short_break_minutes(self, client):
        data = client.get("/api/settings").get_json()
        assert data["short_break_minutes"] == 5

    def test_has_long_break_minutes(self, client):
        data = client.get("/api/settings").get_json()
        assert data["long_break_minutes"] == 15

    def test_has_long_break_interval(self, client):
        data = client.get("/api/settings").get_json()
        assert data["long_break_interval"] == 4


class TestSettingsUpdateAPI:
    """PUT /api/settings — 設定更新の確認"""

    def test_update_focus_minutes(self, client):
        response = client.put("/api/settings", json={"focus_minutes": 30})
        assert response.status_code == 200
        assert response.get_json()["focus_minutes"] == 30

    def test_invalid_body_returns_400(self, client):
        response = client.put("/api/settings", data="not-json",
                               content_type="text/plain")
        assert response.status_code == 400

    def test_unknown_key_returns_400(self, client):
        response = client.put("/api/settings", json={"unknown_key": 99})
        assert response.status_code == 400
