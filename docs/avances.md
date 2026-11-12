# Bitácora de avances

Registro de lo que se hace en el proyecto, del más reciente al más antiguo. Reemplaza los informes de estado formales (ver tailoring, sección 2.3 del plan).

| Fecha | Quién | Avance | Siguiente paso |
|---|---|---|---|
| 12/11/2026 | Julián Ramírez | Informe de cierre en borrador v0.1 (`informe-de-cierre.md`, `SIDEM-IC-2026-01`) con lo registrado en `main`: 9 casos planeados, 8 con ejecución, 6 pasan y 2 fallan (TC-02 y TC-06); 5 defectos abiertos. Las partes manuales de TC-01, 02, 04 y 07 aparecen como pendientes. | Actualizar el informe cuando se integren las demás hojas manuales; preparar las diapositivas. |
| 12/11/2026 | Nicolás Cataño | Ejecución manual de TC-03 y TC-08 en la demo: los 6 cursos muestran el porcentaje y el color esperados, y los totales del panel coinciden en general, en Sistemas Digitales y en Producción. Todos los pasos pasan; no hay defectos nuevos. Evidencias en `evidencias/`. | Preparar la explicación de TC-12 y TC-13 y la exposición. |
| 12/11/2026 | Nicolás Cataño | Verificación a mano de DAT-01: los 6 cursos de la demo dan 80, 77, 50, 47, 100 y 0 %, igual a lo esperado en `demo/seed_demo.py`. Tabla en la sección "Verificación de DAT-01 (Nicolás)". | Ejecutar a mano TC-03 y TC-08. || 12/11/2026 | Sebastián Díaz | Corrida completa de las pruebas automáticas en un segundo computador, con la demo recién reiniciada (`docker compose down -v` y `up -d`): 19 pruebas, 16 pasan y 3 fallan, igual que el 08/11. Fallan `test_consulta_puede_ver_el_seguimiento` (DEF-04), `test_lider_sin_departamento_no_ve_metricas` (DEF-01) y `test_sesion_cerrada_no_se_reutiliza` (DEF-02). Duración: 6 min 8 s. Salida en `evidencias/pytest/ejecucion_2026-11-12_Sebastian.txt` y `.xml`. | Ejecutar a mano TC-07 y TC-04. |
| 12/11/2026 | Julián Ramírez | Ejecución manual de TC-05 (Sistemas Digitales y Producción: el Excel coincide con la pantalla en cursos y SI/NO de la revisión 1) y TC-06 (cerrar sesión, "Atrás" y recargar terminan en el login). Revisión de la evidencia de TC-09 en `evidencias/pytest/ejecucion_2026-11-08.txt`: `test_bloqueo_y_desbloqueo` aparece como PASSED. Hojas llenas en `ejecucion-manual.md`; capturas y Excel en `evidencias/`. | Informe de cierre (`informe-de-cierre.md`). |
| 08/11/2026 | Equipo | Primera corrida completa de las pruebas automáticas (TC-01, 02, 03, 05, 06, 07 y 09): 19 pruebas, 16 pasan y 3 fallan. Los 3 fallos son defectos de SIDEM (DEF-01, DEF-02 y DEF-04). Salida en `evidencias/pytest/ejecucion_2026-11-08.txt`. Se preparan las hojas de ejecución manual (`ejecucion-manual.md`). Plan en v0.3. | Ejecutar los casos manuales según el reparto y tomar las capturas. |
| 08/11/2026 | Equipo | Se monta la demo de SIDEM con Docker y datos ficticios (`demo/`). Al revisar el sistema se ajustan TC-01, TC-03 y DAT-01 en el plan (v0.2). Aparecen dos hallazgos (ver abajo). | Que cada integrante levante la demo en su equipo y revise sus casos. |
| 08/11/2026 | Equipo | Se crea el repositorio. Se consolidan Actividades 1 y 2, matriz de riesgos y Talleres 4 y 5. Primer borrador del plan (v0.1) con tailoring, trazabilidad y cronograma. | Revisar el plan con el docente (`preguntas-para-el-profe.md`). |
| 13/10/2026 | Equipo | Talleres 4 (estrategia) y 5 (casos y procedimientos). | - |
| - | Equipo | Matriz de riesgos R01-R10 y RP1-RP3. | - |
| 29/09/2026 | Equipo | Actividad 2 con coevaluación del equipo de RESTful Booker. | - |
| 22/09/2026 | Equipo | Actividad 1: alcance y metodología. | - |

## Verificación de DAT-01 (Nicolás)

SIDEM no cuenta criterios: suma sus pesos. Pesos de la revisión 1 (total 30):

| Criterio | 1 | 2 | 3 | 4 | 6 | 7 | Total |
|---|---|---|---|---|---|---|---|
| Peso | 5 | 5 | 7 | 5 | 6 | 2 | 30 |

Porcentaje = (suma de pesos cumplidos ÷ 30) × 100, redondeado. Verde si es ≥ 80, amarillo si es ≥ 50 y < 80, rojo si es < 50.

| Curso | Criterios cumplidos | Suma de pesos | % calculado | Color esperado |
|---|---|---|---|---|
| Programación Básica | 1, 2, 3, 4, 7 | 5 + 5 + 7 + 5 + 2 = 24 | 24 ÷ 30 = 80 % | Verde (en el límite) |
| Bases de Datos | 1, 2, 4, 6, 7 | 5 + 5 + 5 + 6 + 2 = 23 | 23 ÷ 30 = 76,7 → 77 % | Amarillo (justo debajo de 80) |
| Redes I | 1, 2, 4 | 5 + 5 + 5 = 15 | 15 ÷ 30 = 50 % | Amarillo (en el límite) |
| Procesos Industriales | 1, 3, 7 | 5 + 7 + 2 = 14 | 14 ÷ 30 = 46,7 → 47 % | Rojo (justo debajo de 50) |
| Calidad | todos | 30 | 100 % | Verde |
| Logística | ninguno | 0 | 0 % | Rojo |

Los 6 valores coinciden con el % esperado de la lista `CURSOS` en `demo/seed_demo.py`.

**Por qué estos valores.** Se usa la técnica de valores límite. Los errores suelen estar en los bordes, por ejemplo si el código usa `>` en vez de `>=`. Por eso se prueba justo en cada límite (80 y 50) y justo por debajo (77 y 47). Si el sistema compara mal, Programación Básica saldría amarilla en vez de verde, o Redes I saldría roja en vez de amarilla. Calidad (100 %) y Logística (0 %) cubren los extremos.

## Hallazgos

Lo que se observó al montar la demo y al ejecutar las pruebas. Los que se confirman como defecto pasan a `defectos.md`.

| ID | Qué se observó | Dónde | Relación con el plan | Estado |
|---|---|---|---|---|
| HAL-01 | `sql/db.sql` no se puede ejecutar completo en una base nueva: la migración de `seguimientos_estudiantes` usa la columna `estado_seguimiento`, que en una instalación nueva no existe. | `sql/db.sql`, línea 593 aprox. | Fuera del alcance (módulo de estudiantes), pero afecta la instalación. | Registrado como DEF-05. La demo lo rodea sin cambiar SIDEM. |
| HAL-02 | Un líder de departamento **sin departamento asignado** ve las estadísticas de todos los cursos. Se esperaba que no viera ninguno. | `services/dashboard_service.py`: `if dept_lista:` toma la lista vacía como "sin filtro". | Riesgo R02, caso TC-02. | Confirmado con TC-02. Registrado como DEF-01. |
| HAL-03 | Al cerrar sesión solo se borra la cookie del navegador. Si alguien copió la cookie antes, sigue funcionando hasta que vence. | `routes/auth.py`, `logout()`: no invalida el token en el servidor. | Riesgo R09, condición CP-09, complemento de TC-06. | Confirmado. Registrado como DEF-02. |
| HAL-04 | Un rol personalizado (el rol "consulta" de la demo) con permiso de ver el seguimiento no ve ningún curso. | `services/auth_service.py`, `get_departamentos_permitidos()`: los roles que no son los de siempre reciben una lista vacía. | Riesgo R01, caso TC-02. | Registrado como DEF-04. |
| HAL-05 | El bloqueo de login no se activó en la primera corrida de TC-09. Las fechas de `log_actividad` se guardan con `CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'`; si PostgreSQL está en UTC, quedan 5 horas atrás y la ventana de 300 s nunca las cuenta. | `sql/db.sql`, tabla `log_actividad`, columna `fecha`. | Riesgo R08, caso TC-09. | Registrado como DEF-03. La demo se ajustó a la zona horaria del servidor y TC-09 pasó. Falta revisar la zona horaria de la base de producción. |
