# Hojas de ejecución manual

Guía para que cada integrante ejecute en el navegador los casos que le corresponden (sección 7.1 del plan). Las pruebas automáticas ya cubren la parte de la API; aquí se revisa lo que ve el usuario en pantalla.

**Antes de empezar cada procedimiento:**
1. Levantar la demo y dejarla en su estado inicial (`demo/README.md`, "Volver al estado inicial").
2. Abrir Chrome en http://localhost:8090.
3. Contraseña de todos los usuarios: `Demo-SIDEM-2026`.

**Al terminar cada caso:** llenar la columna "Obtenido", marcar "Pasa" o "Falla" y guardar la captura en `evidencias/` con el nombre `TC-XX_AAAA-MM-DD_<integrante>.png`. Si falla, registrar el defecto en `docs/defectos.md` (y como issue en GitHub, con la plantilla).

---

## PROC-01 (P1)

### TC-01 - Alcance por departamento · Marcos

| # | Paso | Esperado | Obtenido | Pasa / Falla |
|---|---|---|---|---|
| 1 | Entrar como `lider.sd@sidem.test` y abrir **Métricas**. | Solo aparecen los 3 cursos de Sistemas Digitales. | | |
| 2 | Buscar en los filtros la opción de ver Producción. | No aparece, o si se fuerza, el sistema la rechaza. | | |
| 3 | Intentar abrir **Seguimiento** desde el menú o escribiendo `/seguimiento`. | El líder de departamento no tiene acceso al seguimiento. | | |
| 4 | Cerrar sesión, entrar como `admin@sidem.test` y revisar Logística (DEMO). | Sus criterios no cambiaron. | | |

### TC-02 - Permisos por rol · Marcos

| # | Paso | Esperado | Obtenido | Pasa / Falla |
|---|---|---|---|---|
| 1 | Entrar como `consulta@sidem.test` y abrir **Seguimiento**. | Ve los cursos, sin botón de guardar o con el guardado bloqueado. | | |
| 2 | Si hay algún control de edición, intentar guardar un cambio. | El sistema no deja guardar. | | |
| 3 | Entrar como `lider.sindep@sidem.test` y abrir **Métricas**. | No ve ningún curso. | | |

> La prueba automática ya mostró que los pasos 1 y 3 no dan lo esperado (HAL-02 y HAL-04 en `avances.md`). La captura de pantalla sirve como evidencia visual del defecto.

### TC-03 - Semáforo en los valores límite · Nicolás

Entrar como `lider@sidem.test`, abrir **Métricas**, periodo actual, revisión 1.

| # | Curso | Esperado | Obtenido | Pasa / Falla |
|---|---|---|---|---|
| 1 | Programación Básica (DEMO) | 80 % verde | 80 % verde | Pasa |
| 2 | Bases de Datos (DEMO) | 77 % amarillo | 77 % amarillo | Pasa |
| 3 | Redes I (DEMO) | 50 % amarillo | 50 % amarillo | Pasa |
| 4 | Procesos Industriales (DEMO) | 47 % rojo | 47 % rojo | Pasa |
| 5 | Calidad (DEMO) | 100 % verde | 100 % verde | Pasa |
| 6 | Logística (DEMO) | 0 % rojo | 0 % rojo | Pasa |
| 7 | Resumen del panel | 2 verdes, 2 amarillos, 2 rojos | 6 cursos: 2 al día, 2 con alertas, 2 críticos | Pasa |

Ejecutado el 12/11/2026 por Nicolás Durango, con apoyo del asistente de IA en el navegador. Periodo 2026-2, revisión 1 - semana 2. Evidencia: `evidencias/TC-03_2026-11-12_Nicolas.png`.

### TC-07 - El registro queda en el curso y la revisión correctos · Sebastián

| # | Paso | Esperado | Obtenido | Pasa / Falla |
|---|---|---|---|---|
| 1 | Entrar como `revisor.sd@sidem.test`, abrir **Seguimiento**, revisión 2. | Aparecen Programación Básica y Bases de Datos, sin criterios cumplidos. | | |
| 2 | En Programación Básica marcar dos criterios con una observación y guardar. | Mensaje de guardado correcto. | | |
| 3 | Revisar Bases de Datos en la revisión 2. | Sigue sin criterios cumplidos. | | |
| 4 | Cambiar a la revisión 1 y revisar Programación Básica. | Sigue en 80 %, sin la observación nueva. | | |

---

## PROC-02 (P2)

### TC-04 - Lo guardado se conserva al recargar · Sebastián

| # | Paso | Esperado | Obtenido | Pasa / Falla |
|---|---|---|---|---|
| 1 | Entrar como `revisor.sd@sidem.test`, abrir Redes I (DEMO), revisión 1. | Se ven los 6 criterios. | | |
| 2 | Marcar un criterio, escribir una observación y guardar. | Mensaje de guardado correcto. | | |
| 3 | Recargar la página (F5) y abrir el mismo curso. | El criterio y la observación siguen ahí. | | |
| 4 | Cerrar sesión, volver a entrar y abrir el curso. | Los datos siguen iguales. | | |

### TC-08 - Totales del panel · Nicolás

| # | Paso | Esperado | Obtenido | Pasa / Falla |
|---|---|---|---|---|
| 1 | Con la base recién reiniciada, contar a mano en `demo/README.md` cuántos cursos hay por color. | 2 verdes, 2 amarillos, 2 rojos; 6 cursos. | Conteo hecho con la lista `CURSOS` de `demo/seed_demo.py` (ver "Verificación de DAT-01" en `avances.md`): 2 verdes, 2 amarillos, 2 rojos; 6 cursos. | Pasa |
| 2 | Entrar como `lider@sidem.test` y anotar los totales de **Métricas** y **Dashboard**. | Coinciden con el conteo del paso 1. | Métricas, revisión 1: 6 cursos revisados, 2 al día, 2 con alertas, 2 críticos, cumplimiento global 59 %. El Dashboard del líder solo muestra los módulos (Métricas, Actividad en Moodle, Manual), sin totales. | Pasa |
| 3 | Filtrar por Sistemas Digitales y luego por Producción. | SD: 1 verde, 2 amarillos. PR: 1 verde, 2 rojos. | SD: 3 cursos, 1 al día, 2 con alertas, 0 críticos (69 %). PR: 3 cursos, 1 al día, 0 con alertas, 2 críticos (49 %). | Pasa |

Ejecutado el 12/11/2026 por Nicolás Durango, con apoyo del asistente de IA en el navegador. Evidencias: `evidencias/TC-08_2026-11-12_Nicolas_todos.png`, `_SD.png` y `_PR.png`.

### TC-05 - El Excel coincide con la pantalla · Julián

| # | Paso | Esperado | Obtenido | Pasa / Falla |
|---|---|---|---|---|
| 1 | Entrar como `revisor.sd@sidem.test` y exportar el Excel filtrado por Sistemas Digitales. | Se descarga el archivo. | | |
| 2 | Comparar los cursos del Excel con los de **Seguimiento** filtrado igual. | Los mismos 3 cursos. | | |
| 3 | Comparar los SI/NO de la revisión 1 de cada curso. | Coinciden con la pantalla. | | |
| 4 | Repetir con Producción. | Igual que arriba. | | |

### TC-09 - Bloqueo por intentos fallidos · Julián

Es automático (`test_tc09_bloqueo_login.py`). Julián revisa la salida en `evidencias/pytest/` y confirma que muestra los 5 rechazos, el bloqueo y el desbloqueo.

---

## PROC-03 (P3)

### TC-06 - Sesión cerrada · Julián

| # | Paso | Esperado | Obtenido | Pasa / Falla |
|---|---|---|---|---|
| 1 | Entrar como `consulta@sidem.test` y abrir cualquier página. | Carga normal. | | |
| 2 | Cerrar sesión. | Vuelve al login. | | |
| 3 | Presionar "Atrás" en el navegador. | Redirige al login, no muestra datos. | | |
| 4 | Recargar la página en la que quedó. | Sigue en el login. | | |

> La prueba automática complementaria encontró que la cookie copiada antes del cierre sigue sirviendo (HAL-03). Este caso manual revisa solo el comportamiento del navegador.
