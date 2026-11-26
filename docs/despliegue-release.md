# Release y despliegue de TaskManager

## Estado de validación
La integración continua de GitHub Actions ejecutó correctamente la instalación de dependencias y las pruebas automatizadas en el commit c42f42209a28bb4435ee1bf41c6ec8ab5f8e46aa.

## Crear el Release en GitHub
1. Abrir la pestaña Releases del repositorio.
2. Seleccionar Draft a new release.
3. Crear una etiqueta nueva: v1.0.0.
4. Seleccionar la rama main.
5. Título: TaskManager v1.0.0.
6. Descripción: Primera versión funcional con registro, consulta, edición, eliminación, estados, prioridades, validaciones y pruebas automatizadas.
7. Seleccionar Publish release.
8. El workflow Entrega Continua generará un artefacto descargable llamado TaskManager-v1.

## Despliegue en Render
1. Iniciar sesión en Render y elegir New > Web Service.
2. Conectar el repositorio Arlet-09/Sistema-web-para-la-gesti-n-de-tareas-.
3. Seleccionar la rama main.
4. Render detectará render.yaml. Si solicita los comandos manualmente:
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app:app
5. Crear el servicio y esperar a que finalice el despliegue.
6. Abrir la URL pública generada por Render y probar el registro, consulta, edición, cambio de estado y eliminación.

## Consideración de persistencia
La aplicación usa SQLite. El almacenamiento local de un servicio web gratuito puede ser efímero y perder datos al reiniciar o volver a desplegar. Para conservar datos en producción se necesita un disco persistente compatible con el plan de Render o migrar la base de datos a PostgreSQL. Para una demostración académica, probar el CRUD después del despliegue y no almacenar información sensible.

## Operación y monitoreo
- Revisar la pestaña Logs de Render si el servicio no inicia.
- Revisar Actions para verificar que CI y el artefacto de Release hayan finalizado correctamente.
- Registrar incidencias como GitHub Issues.
- No marcar el despliegue como completado hasta abrir y probar la URL pública.
