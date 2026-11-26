# Plan de trabajo DevOps

## Equipo
La actividad contempla tres integrantes. Asignar nombres y cuentas reales cuando el equipo esté definido:
- Integrante 1: backend Flask, API y SQLite.
- Integrante 2: interfaz HTML, CSS y JavaScript.
- Integrante 3: pruebas, GitHub Actions, documentación y despliegue.

## Ramas de desarrollo
Cada rama se crea desde `main` y se integra mediante Pull Request:
- `feature/registro-tareas`: HU01 y captura inicial de HU06.
- `feature/editar-tareas`: HU02, HU03 y HU05.
- `feature/eliminar-tareas`: HU04.
- HU06 también requiere validar que la prioridad pueda modificarse al editar.

## Flujo
Plan → Code → Build → Test → Release → Deploy → Operate → Monitor.

No integrar directamente a main sin revisión. Cada Pull Request debe describir cambios, relacionarse con su Issue y comprobar CI.
