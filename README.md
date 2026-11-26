# TaskManager-DevOps

Sistema web para gestionar tareas administrativas. Permite registrar, consultar, editar, eliminar y actualizar el estado y prioridad de las tareas.

## Tecnologías
- Python 3.12 y Flask
- SQLite
- HTML, CSS y JavaScript
- Pytest
- GitHub Actions

## Estructura
- `app.py`: aplicación Flask y API REST.
- `templates/index.html`: interfaz web.
- `static/css/style.css`: estilos.
- `static/js/app.js`: interacción con la API.
- `tests/test_app.py`: pruebas automatizadas.
- `historias-usuario.md`: HU01–HU06.
- `docs/`: matriz de pruebas y plan DevOps.
- `.github/workflows/`: CI y preparación de artefacto de Release.

## Ejecución local
```bash
python -m venv .venv
```
En Windows:
```powershell
.venv\Scripts\activate
```
En Linux/macOS:
```bash
source .venv/bin/activate
```
Instalar y ejecutar:
```bash
pip install -r requirements.txt
python app.py
```
Abrir http://127.0.0.1:5000.

## Pruebas
```bash
pytest -q
```

La base SQLite se crea automáticamente en la carpeta instance. Para cambiar la ubicación, configura TASKMANAGER_DATABASE.

## Flujo Git
Crear una rama desde main para cada frente de trabajo y abrir un Pull Request hacia main. No integrar cambios sin revisión.
