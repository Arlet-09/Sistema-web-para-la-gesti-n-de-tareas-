# Guía de evidencias y documentos del remedial DevOps

Este archivo organiza los entregables solicitados en el documento Remedial: Implementación de las fases de DevOps utilizando GitHub. Las capturas deben mostrar resultados reales del repositorio y no sustituir los archivos fuente.

## Fase 1. Planificación (Plan)
**Archivos/documentos**
- `README.md`: nombre, descripción, objetivo, tecnologías y ejecución del sistema.
- `historias-usuario.md`: historias HU01–HU06 con criterios de aceptación.
- `docs/plan-devops.md`: integrantes, responsabilidades, ramas y flujo de trabajo.

**Evidencias**
- [ ] URL del repositorio.
- [ ] Captura del tablero GitHub Projects con Backlog, To Do, In Progress, Review y Done.
- [ ] Captura de las historias de usuario.
- [ ] Captura de los Issues con responsable, estado, prioridad, estimación, fase DevOps y fecha límite.
- [ ] Distribución real de responsabilidades del equipo.

## Fase 2. Desarrollo (Code)
**Archivos/documentos**
- Código fuente: `app.py`, `templates/index.html`, `static/css/style.css`, `static/js/app.js`.
- Dependencias: `requirements.txt`.
- Pruebas: `tests/test_app.py`.
- Registro de desarrollo: puede incorporarse en este documento con integrantes, rama utilizada y funcionalidad desarrollada.

**Evidencias**
- [ ] Captura de las seis ramas feature y main.
- [ ] Historial de commits de cada integrante.
- [ ] Pull Requests hacia main, con descripción y revisión.
- [ ] Capturas del sistema funcionando.
- [ ] Verificar que las funcionalidades solicitadas estén implementadas.

## Fase 3. Integración continua (Build / CI)
**Archivos/documentos**
- `.github/workflows/ci.yml`: workflow de integración continua.
- `tests/test_app.py`: pruebas unitarias automatizadas.

**Evidencias**
- [ ] Captura del workflow CI en GitHub Actions.
- [ ] Captura de una ejecución exitosa de pruebas.
- [ ] Captura o registro de un error detectado y su corrección, si ocurrió.
- [ ] Captura de la ejecución posterior a la corrección.

## Fase 4. Pruebas (Test)
**Archivos/documentos**
- `docs/matriz-pruebas.md`: casos CP01 en adelante, datos de prueba y resultados esperados.
- Añadir una columna de resultado obtenido y estado (Aprobada/Fallida) después de ejecutar cada prueba.

**Evidencias**
- [ ] Matriz de pruebas completada con resultados reales.
- [ ] Capturas de pruebas funcionales: alta, consulta, edición, eliminación, estado y prioridad.
- [ ] Issues específicos de errores encontrados, únicamente si se detectaron.
- [ ] Pull Request o commit con la corrección.
- [ ] Nueva ejecución exitosa de GitHub Actions.

## Fase 5. Entrega continua (Release)
**Archivos/documentos**
- `.github/workflows/delivery.yml`: workflow activado al publicar un Release.
- Release `v1.0.0`: notas de versión y funcionalidades incluidas.
- Artefacto `TaskManager-v1`: paquete generado por GitHub Actions.

**Evidencias**
- [ ] Captura del Release publicado.
- [ ] Captura de la ejecución exitosa del workflow de entrega.
- [ ] Captura o descarga del artefacto generado.
- [ ] Notas de versión.

## Fase 6. Despliegue continuo (Deploy)
**Archivos/documentos**
- `render.yaml` conserva la configuración propuesta para Render; si se usa otro proveedor, documentar el proveedor real y su configuración.
- Registrar el proveedor utilizado, la fecha de despliegue y la URL pública.

**Evidencias**
- [ ] Captura de la plataforma y del despliegue exitoso.
- [ ] URL pública real de TaskManager.
- [ ] Captura de la página principal publicada.
- [ ] Capturas de las operaciones principales funcionando en el entorno publicado.

**Estado actual:** pendiente de completar un despliegue exitoso. No colocar una URL inventada ni marcar esta fase como terminada antes de probarla.

## Fase 7. Operación y monitoreo (Operate & Monitor)
**Archivos/documentos**
- `docs/operacion-monitoreo.md`: procedimiento de salud, incidencias y monitoreo.
- `.github/workflows/monitor.yml`: comprobación programada de `/health` cuando se configure el secreto `TASKMANAGER_URL`.
- Crear un **registro de monitoreo** con fecha/hora, URL revisada, disponibilidad, tiempo de respuesta, resultado y observaciones.
- Crear un **registro de incidencias** con fecha, funcionalidad afectada, descripción, evidencia, responsable y solución. Si no se detectaron fallas, indicarlo expresamente.
- Incluir al menos tres mejoras para una versión futura y su prioridad.

**Evidencias**
- [ ] Captura del endpoint `/health` devolviendo estado correcto.
- [ ] Captura de una ejecución real del workflow de monitoreo con URL configurada.
- [ ] Registro de incidencias reales o declaración de que no se detectaron incidencias durante la revisión.
- [ ] Tres propuestas de mejora.
- [ ] Planeación breve de la versión 2.

## Documento final de resultados y conclusiones
Entregar un informe breve con:
1. Portada: nombre del proyecto, integrantes, asignatura, docente y fecha.
2. Objetivo y descripción de TaskManager.
3. Resumen de las siete fases y enlaces a sus evidencias.
4. Resultados reales de las pruebas y de GitHub Actions.
5. Estado del Release y del despliegue.
6. Resultados de operación y monitoreo.
7. Conclusiones del equipo.
8. Respuestas a las 12 preguntas de análisis del remedial.

**Importante:** el remedial solicita evidencias de repositorio, tablero, código, ramas, Pull Requests, Actions, matriz, Release, despliegue y resultados/conclusiones. No todo es un documento independiente; las capturas y enlaces verificables forman parte de la entrega.
