# Matriz de pruebas funcionales

| ID | Caso | Resultado esperado |
|---|---|---|
| CP01 | Registrar tarea válida | Se guarda y aparece en el listado. |
| CP02 | Registrar sin nombre | Se muestra validación y no se guarda. |
| CP03 | Consultar tareas | Se muestra el listado. |
| CP04 | Editar tarea | Se actualizan los datos. |
| CP05 | Eliminar tarea | Desaparece del listado. |
| CP06 | Cambiar estado | Se guarda el estado elegido. |
| CP07 | Asignar prioridad | Se guarda alta, media o baja. |
| CP08 | Prioridad no válida | La API responde HTTP 400. |
| CP09 | Consultar tarea inexistente | La API responde HTTP 404. |
