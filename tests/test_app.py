import sys
from pathlib import Path

# Ensure the repository root is importable when pytest collects this file in CI.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest
from app import create_app


@pytest.fixture
def client(tmp_path):
    application = create_app({
        "TESTING": True,
        "DATABASE": str(tmp_path / "tasks.sqlite3"),
    })
    return application.test_client()


def create_task(client, **overrides):
    payload = {
        "title": "Preparar reporte",
        "description": "Entrega semanal",
        "priority": "high",
    }
    payload.update(overrides)
    return client.post("/api/tasks", json=payload)


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"TaskManager" in response.data


def test_list_starts_empty(client):
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert response.get_json() == []


def test_create_task(client):
    response = create_task(client)
    assert response.status_code == 201
    assert response.get_json()["title"] == "Preparar reporte"


def test_create_requires_title(client):
    response = create_task(client, title="  ")
    assert response.status_code == 400
    assert "title" in response.get_json()["fields"]


def test_create_rejects_invalid_priority(client):
    response = create_task(client, priority="urgent")
    assert response.status_code == 400


def test_update_task(client):
    task = create_task(client).get_json()
    response = client.put(
        f"/api/tasks/{task['id']}",
        json={
            "title": "Tarea editada",
            "description": "Descripción actualizada",
            "priority": "medium",
            "status": "in_progress",
        },
    )
    assert response.status_code == 200
    assert response.get_json()["title"] == "Tarea editada"


def test_change_status(client):
    task = create_task(client).get_json()
    response = client.patch(
        f"/api/tasks/{task['id']}/status",
        json={"status": "completed"},
    )
    assert response.status_code == 200
    assert response.get_json()["status"] == "completed"


def test_change_status_rejects_invalid_value(client):
    task = create_task(client).get_json()
    response = client.patch(
        f"/api/tasks/{task['id']}/status",
        json={"status": "blocked"},
    )
    assert response.status_code == 400


def test_delete_task(client):
    task = create_task(client).get_json()
    response = client.delete(f"/api/tasks/{task['id']}")
    assert response.status_code == 200
    assert client.get(f"/api/tasks/{task['id']}").status_code == 404


def test_update_missing_task_returns_404(client):
    response = client.put("/api/tasks/999", json={"title": "No existe"})
    assert response.status_code == 404
