"""Aplicación web TaskManager desarrollada con Flask y SQLite."""
import os
import sqlite3
from pathlib import Path
from flask import Flask, g, jsonify, render_template, request

VALID_STATUSES = {"pending", "in_progress", "completed"}
VALID_PRIORITIES = {"high", "medium", "low"}

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=os.environ.get("TASKMANAGER_DATABASE", "/tmp/taskmanager.sqlite3" if os.environ.get("VERCEL") else str(Path(app.instance_path) / "taskmanager.sqlite3")),
        SECRET_KEY=os.environ.get("SECRET_KEY", "development-only-change-me"),
    )
    if test_config:
        app.config.update(test_config)
    Path(app.config["DATABASE"]).parent.mkdir(parents=True, exist_ok=True)

    def get_db():
        if "db" not in g:
            g.db = sqlite3.connect(app.config["DATABASE"])
            g.db.row_factory = sqlite3.Row
        return g.db

    @app.teardown_appcontext
    def close_db(_error=None):
        db = g.pop("db", None)
        if db is not None:
            db.close()

    with app.app_context():
        get_db().execute("""CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL DEFAULT '',
            priority TEXT NOT NULL DEFAULT 'medium',
            status TEXT NOT NULL DEFAULT 'pending',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )""")
        get_db().commit()

    @app.get("/health")
    def health():
        # Comprueba tanto la aplicación como el acceso a SQLite.
        get_db().execute("SELECT 1").fetchone()
        return jsonify({"status": "ok", "service": "TaskManager", "database": "ok"})

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/api/tasks")
    def list_tasks():
        rows = get_db().execute("SELECT * FROM tasks ORDER BY id DESC").fetchall()
        return jsonify([dict(row) for row in rows])

    @app.post("/api/tasks")
    def create_task():
        data = request.get_json(silent=True) or {}
        title = str(data.get("title", "")).strip()
        description = str(data.get("description", "")).strip()
        priority = str(data.get("priority", "medium")).lower()
        status = str(data.get("status", "pending")).lower()
        errors = {}
        if not title:
            errors["title"] = "El nombre de la tarea es obligatorio."
        if priority not in VALID_PRIORITIES:
            errors["priority"] = "Prioridad no válida."
        if status not in VALID_STATUSES:
            errors["status"] = "Estado no válido."
        if errors:
            return jsonify({"error": "Datos no válidos.", "fields": errors}), 400
        db = get_db()
        cursor = db.execute(
            "INSERT INTO tasks (title, description, priority, status) VALUES (?, ?, ?, ?)",
            (title, description, priority, status),
        )
        db.commit()
        row = db.execute("SELECT * FROM tasks WHERE id = ?", (cursor.lastrowid,)).fetchone()
        return jsonify(dict(row)), 201

    @app.put("/api/tasks/<int:task_id>")
    def update_task(task_id):
        db = get_db()
        old = db.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
        if old is None:
            return jsonify({"error": "La tarea no existe."}), 404
        data = request.get_json(silent=True) or {}
        title = str(data.get("title", old["title"])).strip()
        description = str(data.get("description", old["description"])).strip()
        priority = str(data.get("priority", old["priority"])).lower()
        status = str(data.get("status", old["status"])).lower()
        if not title or priority not in VALID_PRIORITIES or status not in VALID_STATUSES:
            return jsonify({"error": "Datos no válidos."}), 400
        db.execute("""UPDATE tasks SET title=?, description=?, priority=?, status=?,
                   updated_at=CURRENT_TIMESTAMP WHERE id=?""",
                   (title, description, priority, status, task_id))
        db.commit()
        row = db.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
        return jsonify(dict(row))

    @app.patch("/api/tasks/<int:task_id>/status")
    def update_status(task_id):
        data = request.get_json(silent=True) or {}
        status = str(data.get("status", "")).lower()
        if status not in VALID_STATUSES:
            return jsonify({"error": "Estado no válido."}), 400
        db = get_db()
        cursor = db.execute("UPDATE tasks SET status=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
                            (status, task_id))
        db.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "La tarea no existe."}), 404
        row = db.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
        return jsonify(dict(row))

    @app.delete("/api/tasks/<int:task_id>")
    def delete_task(task_id):
        db = get_db()
        cursor = db.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        db.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "La tarea no existe."}), 404
        return jsonify({"message": "Tarea eliminada correctamente."})

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
