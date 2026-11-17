# Informe de cierre de pruebas - SIDEM

> Basado en la norma ISO/IEC/IEEE 29119-3 (*Test Completion Report*). Es el documento final de la entrega (confirmado con el docente el 16/11, pregunta 8 de `preguntas-para-el-profe.md`).
> **Estado:** versión 1.0, final. Incluye la primera ronda de ejecución (08 y 12/11/2026) y el retest de las correcciones (16/11/2026).

---

## 1. Información del documento

| Campo | Valor |
|---|---|
| Identificador | `SIDEM-IC-2026-01` |
| Versión | 1.0 (final) |
| Fecha | 17/11/2026 |
| Autores | Marcos Duque Jaramillo, Sebastián Díaz Jiménez, Nicolás Cataño Durango, Julián Ramírez Molina |
| Plan al que responde | `SIDEM-PP-2026-01`, versión 1.0 (`docs/plan-de-pruebas.md`) |
| Aprobación | Roberto José Calderón Bermejo, docente del curso |

**Historial del informe:**

| Versión | Fecha | Quién | Cambio |
|---|---|---|---|
| 0.1 | 12/11/2026 | Julián Ramírez Molina | Primera versión con la ejecución registrada hasta el 12/11. |
| 1.0 | 17/11/2026 | Marcos Duque Jaramillo y Nicolás Cataño Durango | Versión final: ejecución manual completa, retest del 16/11, defectos cerrados, criterios de finalización y lecciones aprendidas. Marcos, como encargado de organizar la exposición, consolidó con Nicolás el cierre del informe. |

**Fuentes usadas:** `docs/ejecucion-manual.md`, `docs/defectos.md`, `docs/retest.md`, `docs/avances.md`, `evidencias/README.md` y las salidas de pytest de `evidencias/pytest/` (08/11, 12/11 y retest del 16/11).

---

## 2. Resumen

Se probó SIDEM (FastAPI + PostgreSQL), versión commit `77f71b2`, en una copia de demostración con Docker y datos ficticios (entorno AMB-01, datos DAT-01). No se usó Moodle ni la base de producción.

**Primera ronda (08 y 12/11/2026).** Las pruebas automáticas con pytest se corrieron dos veces con la demo recién reiniciada, en computadores distintos, con el mismo resultado: 19 pruebas, 16 pasan y 3 fallan. El 12/11 el equipo ejecutó a mano los 8 casos con parte manual (TC-01 a TC-08), con capturas en `evidencias/`. Se registraron 5 defectos (DEF-01 a DEF-05): 1 alto, 2 medios y 2 bajos.

**Correcciones y retest (16/11/2026).** Cada defecto se corrigió con un parche sobre `77f71b2` (`demo/correcciones/`, parches `0001` a `0005`), cada uno con su prueba automática. En el retest, con las imágenes `77f71b2-correcciones` y la base en UTC, pasan las 19 pruebas y `db.sql` se instala sin errores. Los 5 defectos quedan cerrados.

**Resultado final:** los 9 casos planeados (TC-01 a TC-09) están ejecutados y pasan, no queda ningún defecto abierto y se cumplen todos los criterios de finalización del plan (sección 7).

---

## 3. Lo que se ejecutó

### 3.1 Resultado por caso

"Auto" es pytest contra la demo. "Manual" es la ejecución en el navegador con la hoja de `ejecucion-manual.md` (12/11/2026). "Primera ronda" es el resultado con `77f71b2` sin cambios y "Retest" con las correcciones.

| Caso | Prioridad | Tipo planeado | Auto (primera ronda) | Manual | Primera ronda | Retest (16/11) | Defecto |
|---|---|---|---|---|---|---|---|
| TC-01 | P1 | Manual + automática | 3 de 3 pasan | 4 de 4 pasos pasan | Pasa | Pasa (3 de 3) | - |
| TC-02 | P1 | Manual + automática | 2 de 4 pasan, 2 fallan | Pasos 1 y 3 fallan; paso 2 cubierto en lo automático | Falla | Pasa (4 de 4) | DEF-01, DEF-04 |
| TC-03 | P1 | Manual + automática | 7 de 7 pasan | 7 de 7 pasos pasan | Pasa | Pasa (7 de 7) | - |
| TC-07 | P1 | Manual + automática | 1 de 1 pasa | 4 de 4 pasos pasan | Pasa | Pasa (1 de 1) | - |
| TC-04 | P2 | Manual | No aplica | 4 de 4 pasos pasan | Pasa | No aplica (sin defecto) | - |
| TC-08 | P2 | Manual | No aplica | 3 de 3 pasos pasan | Pasa | No aplica (sin defecto) | - |
| TC-05 | P2 | Manual + automática | 2 de 2 pasan | 4 de 4 pasos pasan | Pasa | Pasa (2 de 2) | - |
| TC-09 | P2 | Automática | 1 de 1 pasa (base en `America/Bogota`) | No aplica | Pasa | Pasa con la base en UTC (1 de 1) | DEF-03 |
| TC-06 | P3 | Manual | 0 de 1 pasan (complemento automático) | 4 de 4 pasos pasan | Falla | Pasa (1 de 1) | DEF-02 |

Quién ejecutó:

| Caso | Responsable | Ejecución registrada |
|---|---|---|
| TC-01, TC-02 | Marcos | Manual el 12/11 (`evidencias/TC-01_2026-11-12_Marcos_*`, `TC-02_2026-11-12_Marcos_*`). |
| TC-07, TC-04 | Sebastián | Manual el 12/11 (`evidencias/TC-07_2026-11-12_Sebastian*`, `TC-04_2026-11-12_Sebastian*`). Corrida de pytest del 12/11 y retest del 16/11. |
| TC-03, TC-08 | Nicolás | Manual el 12/11 (`evidencias/TC-03_2026-11-12_Nicolas.png`, `TC-08_2026-11-12_Nicolas_*`). |
| TC-05, TC-06, TC-09 | Julián | Manual de TC-05 y TC-06 el 12/11 (`evidencias/TC-05_2026-11-12_Julian_*`, `TC-06_2026-11-12_Julian_*`) y revisión de la salida de pytest de TC-09. |

### 3.2 Notas sobre los casos

- **TC-01.** El líder de Sistemas Digitales solo ve su departamento, no puede forzar el de Producción y no puede modificar el seguimiento. Los criterios de Logística siguen sin cambios al revisarlos como administrador.
- **TC-02.** En la primera ronda, el usuario de consulta veía 0 cursos en vez de 6 (DEF-04) y el líder sin departamento veía los 6 cursos en vez de 0 (DEF-01). El paso 2 (intentar guardar) no se pudo hacer a mano porque el usuario de consulta no veía cursos; lo cubre `test_consulta_no_puede_guardar`, que pasa en las tres corridas. En el retest, consulta ve los 6 cursos sin poder guardar y el líder sin departamento ve 0 cursos y "Sin datos".
- **TC-03 y TC-08.** Los 6 cursos muestran 80, 77, 50, 47, 100 y 0 % con el color esperado (verde, amarillo, amarillo, rojo, verde y rojo), y el panel da 6 cursos: 2 al día, 2 con alertas y 2 críticos. En TC-08, Sistemas Digitales da 3 cursos (1 al día, 2 con alertas, 0 críticos) y Producción 3 cursos (1 al día, 0 con alertas, 2 críticos). TC-08 se ejecutó sin `docker compose down -v` previo; los datos de la revisión 1 coincidían con `demo/seed_demo.py`.
- **TC-04 y TC-07.** Lo guardado en la revisión 2 se conserva al recargar y al volver a entrar, y queda en el curso y la revisión correctos sin tocar la revisión 1.
- **TC-05.** Los Excel de Sistemas Digitales y de Producción traen los mismos cursos y los mismos SI/NO de la revisión 1 que la pantalla de Seguimiento.
- **TC-06.** En el navegador, cerrar sesión lleva al login, "Atrás" deja el login y recargar sigue en el login. En la primera ronda, la prueba automática mostró que la cookie copiada antes del cierre seguía sirviendo (200 en lugar de 401, DEF-02). En el retest da 401.
- **TC-09.** En la primera ronda el bloqueo solo funcionó con la base en `America/Bogota` (DEF-03). En el retest, con la base en UTC, los 5 intentos fallidos dan 401, el 6.º con la clave correcta da 429 y pasados los 300 s vuelve a entrar.

### 3.3 Trazabilidad

| Riesgo | Condición | Caso | Evidencia | Defecto |
|---|---|---|---|---|
| R01 | CP-01, CP-02 | TC-01, TC-02 | `evidencias/TC-01_*`, `evidencias/TC-02_*`, `evidencias/pytest/` | DEF-04 (cerrado) |
| R02 | CP-02 | TC-02 | `evidencias/TC-02_*`, `evidencias/pytest/` | DEF-01 (cerrado) |
| R03 | CP-03 | TC-07 | `evidencias/TC-07_*`, `evidencias/pytest/` | - |
| R04 | CP-04 | TC-03 | `evidencias/TC-03_2026-11-12_Nicolas.png`, `evidencias/pytest/` | - |
| R05 | CP-05 | TC-04 | `evidencias/TC-04_*` | - |
| R06 | CP-06 | TC-08 | `evidencias/TC-08_2026-11-12_Nicolas_*.png` | - |
| R07 | CP-07 | TC-05 | `evidencias/TC-05_2026-11-12_Julian_*`, `evidencias/pytest/` | - |
| R08 | CP-08 | TC-09 | `evidencias/pytest/` | DEF-03 (cerrado) |
| R09 | CP-09 | TC-06 | `evidencias/TC-06_2026-11-12_Julian_*`, `evidencias/pytest/` | DEF-02 (cerrado) |

---

## 4. Métricas

### 4.1 Casos

| Métrica | Primera ronda | Después del retest |
|---|---|---|
| Casos planeados (TC-01 a TC-09) | 9 | 9 |
| Casos ejecutados | 9 | 9 |
| Casos que pasan | 7 | 9 |
| Casos que fallan | 2 (TC-02 y TC-06) | 0 |

Los casos extra TC-10 a TC-17 quedaron identificados en el plan (v0.4) y no se ejecutan en este ciclo, como se acordó con el docente.

### 4.2 Pruebas automáticas (pytest)

| Corrida | Pruebas | Pasan | Fallan | Duración |
|---|---|---|---|---|
| 08/11/2026 | 19 | 16 | 3 | 365,77 s |
| 12/11/2026 (Sebastián) | 19 | 16 | 3 | 367,94 s |
| 16/11/2026, retest (Sebastián) | 19 | 19 | 0 | 368,28 s |

En la primera ronda fallaban `test_consulta_puede_ver_el_seguimiento` (DEF-04), `test_lider_sin_departamento_no_ve_metricas` (DEF-01) y `test_sesion_cerrada_no_se_reutiliza` (DEF-02). En el retest pasan las tres.

### 4.3 Pasos manuales

| Caso | Pasos | Pasan | Fallan | Sin ejecutar a mano |
|---|---|---|---|---|
| TC-01 | 4 | 4 | 0 | 0 |
| TC-02 | 3 | 0 | 2 (DEF-04, DEF-01) | 1 (cubierto por pytest) |
| TC-03 | 7 | 7 | 0 | 0 |
| TC-04 | 4 | 4 | 0 | 0 |
| TC-05 | 4 | 4 | 0 | 0 |
| TC-06 | 4 | 4 | 0 | 0 |
| TC-07 | 4 | 4 | 0 | 0 |
| TC-08 | 3 | 3 | 0 | 0 |

Los dos pasos que fallaron en TC-02 se revisaron otra vez en el navegador en el retest (`evidencias/TC-02_2026-11-16_retest_Sebastian_*`) y dan lo esperado.

### 4.4 Defectos por severidad

| Severidad | Encontrados | Cerrados | Abiertos |
|---|---|---|---|
| Crítica | 0 | 0 | 0 |
| Alta | 1 (DEF-01) | 1 | 0 |
| Media | 2 (DEF-02, DEF-03) | 2 | 0 |
| Baja | 2 (DEF-04, DEF-05) | 2 | 0 |
| **Total** | **5** | **5** | **0** |

---

## 5. Defectos

Detalle en `docs/defectos.md`. Versión de SIDEM: commit `77f71b2`; correcciones en `demo/correcciones/`.

| ID | Caso | Riesgo | Severidad | Qué pasaba | Corrección | Estado |
|---|---|---|---|---|---|---|
| DEF-01 | TC-02 | R02 | Alta | El líder de departamento sin departamento asignado veía las métricas de los 6 cursos. | Sin departamento no ve nada; el alcance por departamento es explícito, con opción "Todos". | Cerrado (retest 16/11) |
| DEF-02 | TC-06 | R09 | Media | La cookie de sesión seguía sirviendo después de cerrar sesión. | Contador de sesión `token_version`: al cerrar sesión, los tokens anteriores dejan de servir. | Cerrado (retest 16/11) |
| DEF-03 | TC-09 | R08 | Media | El bloqueo de login dependía de la zona horaria de PostgreSQL; con UTC no se activaba. | La aplicación registra la fecha en UTC; el bloqueo funciona con la base en cualquier zona. | Cerrado (retest 16/11) |
| DEF-04 | TC-02 | R01 | Baja | Un rol personalizado con permiso de ver el seguimiento no veía ningún curso. | Misma regla que DEF-01: alcance explícito; el usuario de consulta tiene "Todos". | Cerrado (retest 16/11) |
| DEF-05 | - | - | Baja | `sql/db.sql` fallaba al instalar SIDEM en una base nueva. | La migración solo corre si la columna anterior existe. | Cerrado (retest 16/11) |

**Retest (16/11/2026, Sebastián).** Se levantó la demo desde cero con las imágenes `77f71b2-correcciones` y la base en UTC (guía en `docs/retest.md`). Resultado: 19 de 19 pruebas pasan, 0 líneas `ERROR:` al crear la base y las capturas de DEF-01 y DEF-04 en el navegador dan lo esperado. Las 650 pruebas propias de SIDEM siguen pasando con los parches. Los issues #1 a #5 de GitHub quedan cerrados con el resultado.

---

## 6. Desviaciones del plan

| # | Qué cambió | Cuándo | Dónde está registrado |
|---|---|---|---|
| 1 | TC-01 pasó a probar al líder de departamento (el rol que se limita por departamento y que no puede editar). | 08/11, plan v0.2 | Plan, 1.4 y 5.3 |
| 2 | TC-03 y DAT-01 se rehicieron con los pesos reales de los criterios para caer justo en 80 % y 50 % (y en 77 % y 47 %). | 08/11, plan v0.2 | Plan, 1.4 y 5.3 |
| 3 | DAT-01 recibió la revisión 2 y la zona horaria de la base. | 08/11, plan v0.3 | Plan, 1.4 y 5.4 |
| 4 | Se agregó una prueba automática a TC-06 (reutilizar la cookie tras cerrar sesión), además de la revisión manual. | 08/11, plan v0.3 | Plan, 5.3 |
| 5 | En la primera ronda la demo se ajustó a la zona horaria `America/Bogota` para poder ejecutar TC-09 (DEF-03). El retest se hizo con la base en UTC. | 08/11 y 16/11 | `avances.md` (HAL-05) y `defectos.md` |
| 6 | Se agregaron TC-07, TC-08 y TC-09 para cubrir R03, R06 y R08, que no tenían caso en el Taller 5. | Plan v0.1 | Plan, 5.3 |
| 7 | Se registraron los casos TC-10 a TC-17 (dos por integrante) sin ejecutarlos. | 10/11, plan v0.4 | Plan, 1.4 y 5.3 |
| 8 | El cronograma se ajustó a la exposición del 17/11. | 10/11, plan v0.5 | Plan, 1.4 y 8 |
| 9 | En TC-05 los dos Excel se bajaron con la misma sesión y la misma petición que usa el botón, porque el navegador integrado no dejó guardar la descarga. | 12/11 | `ejecucion-manual.md` (TC-05) |
| 10 | TC-08 se ejecutó sin reiniciar la base con `docker compose down -v`, que el plan pide como estado inicial. Los datos coincidían con DAT-01. | 12/11 | `ejecucion-manual.md` (TC-08) |
| 11 | El paso 2 de TC-02 no se pudo ejecutar a mano (sin cursos visibles por DEF-04); lo cubre la prueba automática `test_consulta_no_puede_guardar`. | 12/11 | `ejecucion-manual.md` (TC-02) |
| 12 | Las correcciones se hicieron como parches sobre la versión congelada `77f71b2`, para que el retest probara exactamente lo mismo más las correcciones. | 13/11 a 16/11 | `demo/correcciones/`, plan 3.1 |

---

## 7. Evaluación de los criterios de finalización

Criterios de la sección 5.5 del plan, después del retest.

### 7.1 Módulos críticos (F02, F03, F04)

| Criterio | Estado | Detalle |
|---|---|---|
| 100 % de los casos P1 ejecutados | Se cumple | TC-01, TC-02, TC-03 y TC-07 tienen ejecución manual y automática. |
| 100 % de las combinaciones de la tabla de decisión y de los valores límite | Se cumple | Los 6 valores límite del semáforo (TC-03) pasan en lo automático y en lo manual. Las combinaciones de rol y departamento de TC-01 y TC-02 pasan en el retest. |
| Ningún defecto crítico o alto abierto | Se cumple | DEF-01 (alta) quedó cerrado en el retest. |

### 7.2 Módulos secundarios (F01, F05, F06)

| Criterio | Estado | Detalle |
|---|---|---|
| 100 % de los casos diseñados ejecutados | Se cumple | TC-05 (F06), TC-06 y TC-09 (F01) y TC-08 (F05) están ejecutados. |
| Ningún defecto crítico abierto | Se cumple | No hubo defectos críticos. |
| Máximo 2 defectos menores abiertos | Se cumple | 0 abiertos: DEF-02 y DEF-03 quedaron cerrados en el retest. |

**Conclusión.** Se cumplen todos los criterios de finalización. El ciclo de pruebas se da por terminado.

---

## 8. Riesgos residuales

| Riesgo | Situación |
|---|---|
| R01 | Cubierto (TC-01 y TC-02). DEF-04 cerrado. TC-16 y TC-17 (cambiar el ID en la URL, subirse el rol) quedan identificados para un próximo ciclo. |
| R02 | Cubierto (TC-02). DEF-01, el defecto más importante del ciclo, cerrado. |
| R03 | Cubierto en lo manual y en lo automático (TC-07). |
| R04 | Cubierto en lo manual y en lo automático (TC-03). TC-12 (curso sin criterios evaluados) queda identificado. |
| R05 | Cubierto en lo manual (TC-04). |
| R06 | Cubierto en lo manual (TC-08), sin prueba automática. TC-13 (curso repetido o con dos docentes) queda identificado. |
| R07 | Cubierto en lo manual y en lo automático (TC-05) con datos normales. TC-15 (observaciones que empiezan por `=` o `+` en el Excel) queda identificado. |
| R08 | Cubierto (TC-09). DEF-03 cerrado: el bloqueo ya no depende de la zona horaria de la base. |
| R09 | Cubierto (TC-06). DEF-02 cerrado. TC-14 (cambio de contraseña con dos sesiones abiertas) queda identificado. |
| R10 | Aceptado sin pruebas en el plan: no está entre los casos del equipo y no hay entorno de carga. |

También quedan fuera de este ciclo, por decisión del plan: la integración con Moodle, el seguimiento a estudiantes y las pruebas de rendimiento. Las correcciones están probadas en la demo; llevarlas a producción le corresponde al equipo de SIDEM.

---

## 9. Lecciones aprendidas

- **Las pruebas automáticas dieron resultados antes que las manuales.** La corrida de pytest del 08/11 ya mostró DEF-01, DEF-02 y DEF-04. Conviene automatizar primero lo que se puede y dejar la parte manual para lo que se ve en pantalla.
- **Reiniciar la demo antes de cada corrida dio resultados repetibles.** Las corridas del 08/11 y del 12/11, en computadores distintos, dieron el mismo resultado, y el retest partió de una base nueva.
- **Tener la demo en imágenes de Docker facilitó el retest.** Sebastián repitió todo con un `docker load` y la guía de `retest.md`, sin compilar SIDEM.
- **La zona horaria de la base afecta el bloqueo de login.** Se descubrió en la primera corrida de TC-09. En el próximo ciclo debería estar en los requisitos del entorno desde el principio.
- **Probar el navegador y el servidor por separado sirve.** TC-06 pasaba en el navegador pero fallaba en el servidor, y esa diferencia solo se vio por tener las dos pruebas.
- **Los casos de riesgo bajo también encuentran defectos.** R09 tenía exposición baja y aun así produjo DEF-02.
- **Cada corrección con su prueba automática hizo que el retest fuera directo.** Las 3 pruebas que fallaban se convirtieron en la verificación de las correcciones.

---

## 10. Reconocimiento del equipo

| Integrante | Aporte registrado en el repositorio |
|---|---|
| Marcos Duque Jaramillo | Líder de pruebas, entorno de demostración (Docker, imágenes y Drive del equipo) y correcciones de DEF-01 a DEF-05. Casos TC-01 y TC-02. Organización de la exposición; versión 1.0 de este informe, junto con Nicolás. |
| Sebastián Díaz Jiménez | Pruebas automáticas con pytest, corrida del 12/11 y retest del 16/11. Casos TC-07 y TC-04. |
| Nicolás Cataño Durango | Datos de prueba DAT-01 y su verificación. Casos TC-03 y TC-08. Versión 1.0 de este informe, junto con Marcos. |
| Julián Ramírez Molina | Ejecución manual de TC-05 y TC-06, revisión de TC-09, primera versión de este informe (v0.1) y la parte de retest y cierre de la exposición. |
