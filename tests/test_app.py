import os
import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("SMARTGATE_DB_PATH", str(tmp_path / "smartgate-test.db"))
    monkeypatch.setenv("SMARTGATE_API_KEY", "test-key-for-ci-only")
    with TestClient(app) as c:
        yield c


def headers():
    return {"X-API-Key": "test-key-for-ci-only"}


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_root(client):
    assert client.get("/").json()["status"] == "prototype"


def test_valid_permit_opens_simulated_barrier(client):
    r = client.post("/api/v1/access/check", json={"plate": "SK 12345"}, headers=headers())
    assert r.status_code == 200
    assert r.json()["decision"] == "OPEN"
    assert r.json()["simulated"] is True


def test_inactive_permit_denied(client):
    r = client.post("/api/v1/access/check", json={"plate": "KR 98765"}, headers=headers())
    assert r.json()["decision"] == "DENY"
    assert r.json()["reason"] == "inactive"


def test_expired_permit_denied(client):
    r = client.post("/api/v1/access/check", json={"plate": "SB 2026A"}, headers=headers())
    assert r.json()["reason"] == "expired"


def test_unknown_permit_denied(client):
    r = client.post("/api/v1/access/check", json={"plate": "XX 12345"}, headers=headers())
    assert r.json()["decision"] == "DENY"


def test_invalid_plate_rejected(client):
    r = client.post("/api/v1/access/check", json={"plate": "@!bad"}, headers=headers())
    assert r.status_code == 422


def test_no_api_key_rejected(client):
    r = client.post("/api/v1/access/check", json={"plate": "SK 12345"})
    assert r.status_code == 401


def test_wrong_api_key_rejected(client):
    r = client.post("/api/v1/access/check", json={"plate": "SK 12345"}, headers={"X-API-Key":"wrong"})
    assert r.status_code == 401


def test_summary_aggregated(client):
    client.post("/api/v1/access/check", json={"plate": "SK 12345"}, headers=headers())
    r = client.get("/api/v1/events/summary", headers=headers())
    assert r.status_code == 200
    assert r.json()["counts"]["OPEN"] == 1
    assert r.json()["pending_sync"] == 1
    assert r.json()["cloud_sync_implemented"] is False
    assert "SK12345" not in r.text
