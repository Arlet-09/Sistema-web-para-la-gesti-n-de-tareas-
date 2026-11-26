import pytest
from app import create_app

@pytest.fixture
def client(tmp_path):
    app=create_app({"TESTING":True,"DATABASE":str(tmp_path/"tasks.sqlite3")})
    return app.test_client()

def test_home_page(client):
    response=client.get("/")
    assert response.status_code==200
    assert b"TaskManager" in response.data

def test_list_starts_empty(client):
    response=client.get("/api/tasks")
    assert response.status_code==200
    assert response.get_json()==[]

def test_create_task(client):
    response=client.post("/api/tasks",json={"title":"Preparar reporte","description":"Entrega semanal","priority":"high"})
    assert response.status_code==201
    assert response.get_json()["title"]=="Preparar reporte"

def test_create_requires_title(client):
    response=client.post("/api/tasks",json={"title":"  "})
    assert response.status_code==400

def test_update_task(client):
    task=client.post("/api/tasks",json={"title":"Tarea inicial"}).get_json()
    response=client.put(f"/api/tasks/{task['id']}",json={"title":"Tarea editada","priority":"medium","status":"in_progress"})
    assert response.status_code==200
    assert response.get_json()["title"]=="Tarea editada"

def test_change_status(client):
    task=client.post("/api/tasks",json={"title":"Tarea"}).get_json()
    response=client.patch(f"/api/tasks/{task['id']}/status",json={"status":"completed"})
    assert response.status_code==200
    assert response.get_json()["status"]=="completed"

def test_delete_task(client):
    task=client.post("/api/tasks",json={"title":"Eliminar"}).get_json()
    response=client.delete(f"/api/tasks/{task['id']}")
    assert response.status_code==200
    assert client.get(f"/api/tasks/{task['id']}").status_code==404
