# Operación y monitoreo de TaskManager

## Estado de despliegue
El Release v1.0.0 está publicado y el workflow de entrega continua generó el artefacto TaskManager-v1. La publicación del artefacto no significa que la aplicación esté desplegada en Internet.

## Comprobación de salud
La aplicación expone GET /health. La respuesta esperada es HTTP 200:
```json
{"status":"ok","service":"TaskManager","database":"ok"}
```
La ruta ejecuta una consulta simple a SQLite para comprobar conectividad con la base de datos.

## Configurar monitoreo automático
1. Desplegar la aplicación en un proveedor compatible con Flask.
2. Copiar la URL pública completa (sin /health).
3. En GitHub abrir Settings > Secrets and variables > Actions.
4. Crear el secret TASKMANAGER_URL con la URL pública.
5. Abrir Actions > Monitoreo de TaskManager y ejecutar Run workflow.
6. El workflow también se ejecuta cada 30 minutos.
7. Si falla, revisar la URL, el estado del proveedor y los logs de la aplicación.

## Operación e incidencias
- Registrar cada error real como un GitHub Issue con pasos para reproducirlo, resultado esperado, resultado obtenido y evidencia.
- Revisar logs del proveedor y GitHub Actions.
- Asignar responsable, prioridad y fase Operate.
- Corregir en una rama y abrir Pull Request.
- Cerrar la incidencia después de repetir la prueba afectada.

## Limitación de persistencia
La configuración Vercel usa /tmp para SQLite. Ese almacenamiento es temporal y no debe usarse como base persistente de producción. Para conservar tareas tras reinicios o despliegues, conectar PostgreSQL o usar un proveedor con disco persistente. No almacenar datos sensibles en la demostración.

## Despliegue rápido gratuito en Vercel
Vercel Hobby es gratuito para proyectos personales. La plataforma reconoce aplicaciones Flask y puede desplegarlas directamente desde GitHub.
1. Crear cuenta en https://vercel.com/signup con GitHub.
2. Seleccionar Add New > Project.
3. Importar el repositorio Sistema-web-para-la-gesti-n-de-tareas-.
4. Dejar que Vercel detecte Flask/Python automáticamente; no configurar comandos de build de Node.
5. Pulsar Deploy y esperar el resultado.
6. Abrir la URL *.vercel.app y comprobar /health y las funciones del sistema.
7. En GitHub, crear el secret TASKMANAGER_URL con la URL de Vercel para activar el monitoreo automático.

La aplicación utiliza SQLite en /tmp cuando se ejecuta en Vercel. /tmp es temporal: los registros pueden perderse entre invocaciones o despliegues. Este despliegue es para demostración académica. Para persistencia real se debe migrar a PostgreSQL u otra base de datos administrada.
