# Informe de cierre de pruebas - SIDEM

> Basado en la norma ISO/IEC/IEEE 29119-3 (*Test Completion Report*).
> **Estado:** BORRADOR v0.1. Todos los datos salen de lo registrado en el repositorio. Lo que no está registrado aparece como "pendiente".

---

## 1. Información del documento

| Campo | Valor |
|---|---|
| Identificador | `SIDEM-IC-2026-01` |
| Versión | 0.1 (borrador) |
| Fecha | 12/11/2026 |
| Autores | Marcos Duque Jaramillo, Sebastián Díaz Jiménez, Nicolás Castaño Durango, Julián Ramírez Molina |
| Plan al que responde | `SIDEM-PP-2026-01`, versión 0.5 (`docs/plan-de-pruebas.md`) |
| Aprobación | Roberto José Calderón Bermejo, docente del curso |

**Fuentes usadas:** `docs/ejecucion-manual.md`, `docs/defectos.md`, `docs/avances.md`, `evidencias/pytest/ejecucion_2026-11-08.txt` y `evidencias/pytest/ejecucion_2026-11-12_Sebastian.txt`.

---

## 2. Resumen

Se probó SIDEM (FastAPI + PostgreSQL), versión commit `77f71b2`, en una copia de demostración con Docker y datos ficticios (entorno AMB-01, datos DAT-01). La aplicación no se modificó. No se usó Moodle ni la base de producción.

Se ejecutaron las pruebas automáticas con pytest dos veces con la demo recién reiniciada: el 08/11/2026 y el 12/11/2026 (en otro computador, a cargo de Sebastián). Las dos corridas dieron el mismo resultado: 19 pruebas, 16 pasan y 3 fallan. El 12/11/2026 Julián ejecutó a mano TC-05 y TC-06 en el navegador.

Hasta esta versión del informe:
- Hay 5 defectos registrados (DEF-01 a DEF-05), todos abiertos.
- Los 3 fallos de pytest corresponden a DEF-01, DEF-02 y DEF-04.
- Las hojas de ejecución manual de TC-01, TC-02, TC-03, TC-04, TC-07 y TC-08 están sin resultados en `main`, así que su parte manual aparece como pendiente (ver sección 3).

---

## 3. Lo que se ejecutó

### 3.1 Resultado por caso

Fechas: 08/11/2026 y 12/11/2026. "Auto" es pytest contra la demo. "Manual" es la ejecución en el navegador con la hoja de `ejecucion-manual.md`.

| Caso | Prioridad | Tipo planeado | Auto (pruebas) | Manual | Resultado del caso | Defecto |
|---|---|---|---|---|---|---|
| TC-01 | P1 | Manual + automática | 3 de 3 pasan | Pendiente | Pasa en lo automático; manual pendiente | - |
| TC-02 | P1 | Manual + automática | 2 de 4 pasan, 2 fallan | Pendiente | Falla | DEF-01, DEF-04 |
| TC-03 | P1 | Manual + automática | 7 de 7 pasan | Pendiente | Pasa en lo automático; manual pendiente | - |
| TC-07 | P1 | Manual + automática | 1 de 1 pasa | Pendiente | Pasa en lo automático; manual pendiente | - |
| TC-04 | P2 | Manual | No aplica | Pendiente | Sin ejecutar | - |
| TC-08 | P2 | Manual | No aplica | Pendiente | Sin ejecutar | - |
| TC-05 | P2 | Manual + automática | 2 de 2 pasan | 4 de 4 pasos pasan | Pasa | - |
| TC-09 | P2 | Automática | 1 de 1 pasa | No aplica | Pasa | DEF-03 (ver sección 5) |
| TC-06 | P3 | Manual | 0 de 1 pasan (complemento automático) | 4 de 4 pasos pasan | Falla | DEF-02 |

Quién ejecutó:

| Caso | Responsable en el plan | Ejecución registrada |
|---|---|---|
| TC-01, TC-02 | Marcos | Corridas de pytest del 08/11 (equipo) y del 12/11 (Sebastián). Manual pendiente. Existe una captura previa, `evidencias/TC-02_2026-11-08_Marcos.jpg`, pero la hoja manual de TC-02 no está llena. |
| TC-07, TC-04 | Sebastián | Corrida de pytest del 12/11 (TC-07). Manual pendiente en los dos. |
| TC-03, TC-08 | Nicolás | Corridas de pytest (TC-03). Manual pendiente en `main`. |
| TC-05, TC-06, TC-09 | Julián | Manual de TC-05 y TC-06 el 12/11. Revisión de la salida de pytest de TC-09 el 12/11. |

### 3.2 Notas sobre los casos

- **TC-05.** El Excel de Sistemas Digitales trae los mismos 3 cursos que Seguimiento (Programación Básica, Bases de Datos y Redes I) y los mismos SI/NO de la revisión 1 en los 6 criterios. El de Producción trae los mismos 3 cursos (Procesos Industriales, Calidad y Logística) con los mismos SI/NO. Evidencia: `evidencias/TC-05_2026-11-12_Julian_*` (capturas y los dos `.xlsx`). Al abrir Seguimiento la pantalla quedó en la revisión 2 y hubo que elegir la revisión 1 a mano.
- **TC-06.** En el navegador, cerrar sesión lleva al login, "Atrás" deja el login y recargar sigue en el login. La prueba automática complementaria falla porque la cookie copiada antes del cierre sigue sirviendo (200 en lugar de 401). Evidencia: `evidencias/TC-06_2026-11-12_Julian_*` y las dos salidas de pytest.
- **TC-09.** `test_bloqueo_y_desbloqueo` aparece como PASSED en las dos corridas: 5 intentos fallidos dan 401, el 6.º con la clave correcta da 429, poco antes de los 300 s sigue en 429 y pasados los 300 s da 200. Esto fue con la base de la demo en la zona horaria `America/Bogota`.
- **TC-02.** Los dos fallos son los de las pruebas `test_consulta_puede_ver_el_seguimiento` (el usuario de consulta ve 0 cursos en vez de 6) y `test_lider_sin_departamento_no_ve_metricas` (el líder sin departamento ve 6 cursos en vez de 0).

### 3.3 Trazabilidad

| Riesgo | Condición | Caso | Evidencia | Defecto |
|---|---|---|---|---|
| R01 | CP-01, CP-02 | TC-01, TC-02 | `evidencias/pytest/` (08/11 y 12/11) | DEF-04 |
| R02 | CP-02 | TC-02 | `evidencias/pytest/` (08/11 y 12/11) | DEF-01 |
| R03 | CP-03 | TC-07 | `evidencias/pytest/` (08/11 y 12/11) | - |
| R04 | CP-04 | TC-03 | `evidencias/pytest/` (08/11 y 12/11) | - |
| R05 | CP-05 | TC-04 | Sin ejecución | - |
| R06 | CP-06 | TC-08 | Sin ejecución en `main` | - |
| R07 | CP-07 | TC-05 | `evidencias/TC-05_2026-11-12_Julian_*`, `evidencias/pytest/` | - |
| R08 | CP-08 | TC-09 | `evidencias/pytest/` (08/11 y 12/11) | DEF-03 |
| R09 | CP-09 | TC-06 | `evidencias/TC-06_2026-11-12_Julian_*`, `evidencias/pytest/` | DEF-02 |

---

## 4. Métricas

### 4.1 Casos

| Métrica | Valor |
|---|---|
| Casos planeados (TC-01 a TC-09) | 9 |
| Casos con alguna ejecución registrada | 7 (TC-01, 02, 03, 05, 06, 07, 09) |
| Casos sin ejecución registrada | 2 (TC-04 y TC-08) |
| Casos que pasan | 5 (TC-01, 03, 05, 07, 09) |
| Casos que fallan | 2 (TC-02 y TC-06) |
| Casos con parte manual pendiente aunque su parte automática pasa | 3 (TC-01, TC-03, TC-07) |

Los casos extra TC-10 a TC-17 se identificaron en el plan (v0.4) pero no se ejecutan en esta ronda.

### 4.2 Pruebas automáticas (pytest)

| Corrida | Pruebas | Pasan | Fallan | Duración |
|---|---|---|---|---|
| 08/11/2026 | 19 | 16 | 3 | 365,77 s |
| 12/11/2026 (Sebastián) | 19 | 16 | 3 | 367,94 s |

Las pruebas que fallan son las mismas en las dos corridas: `test_consulta_puede_ver_el_seguimiento` (DEF-04), `test_lider_sin_departamento_no_ve_metricas` (DEF-01) y `test_sesion_cerrada_no_se_reutiliza` (DEF-02).

### 4.3 Pasos manuales

| Caso | Pasos | Pasan | Fallan |
|---|---|---|---|
| TC-05 | 4 | 4 | 0 |
| TC-06 | 4 | 4 | 0 |

### 4.4 Defectos por severidad

| Severidad | Cantidad | Defectos |
|---|---|---|
| Crítica | 0 | - |
| Alta | 1 | DEF-01 |
| Media | 2 | DEF-02, DEF-03 |
| Baja | 2 | DEF-04, DEF-05 |
| **Total** | **5** | Todos abiertos |

---

## 5. Defectos

Detalle en `docs/defectos.md`. Versión de SIDEM: commit `77f71b2`.

| ID | Caso | Riesgo | Severidad | Resumen | Estado |
|---|---|---|---|---|---|
| DEF-01 | TC-02 | R02 | Alta | El líder de departamento sin departamento asignado ve las métricas de los 6 cursos. | Abierto |
| DEF-02 | TC-06 | R09 | Media | La cookie de sesión sigue sirviendo después de cerrar sesión. | Abierto |
| DEF-03 | TC-09 | R08 | Media | El bloqueo de login depende de la zona horaria de PostgreSQL; con UTC no se activa. | Abierto |
| DEF-04 | TC-02 | R01 | Baja | Un rol personalizado con permiso de ver el seguimiento no ve ningún curso. | Abierto |
| DEF-05 | - | - | Baja | `sql/db.sql` falla al instalar SIDEM en una base nueva. | Abierto |

**Retest.** No hay retest registrado: SIDEM no se modificó durante el ciclo, así que ningún defecto cambió de estado. En DEF-03 la demo se ajustó a la zona horaria `America/Bogota` para poder ejecutar TC-09, pero el defecto sigue abierto porque falta revisar la zona horaria de la base de producción.

---

## 6. Desviaciones del plan

| # | Qué cambió | Cuándo | Dónde está registrado |
|---|---|---|---|
| 1 | TC-01 pasó a probar al líder de departamento (el rol que se limita por departamento y que no puede editar). | 08/11, plan v0.2 | Plan, 1.4 y 5.3 |
| 2 | TC-03 y DAT-01 se rehicieron con los pesos reales de los criterios para caer justo en 80 % y 50 % (y en 77 % y 47 %). | 08/11, plan v0.2 | Plan, 1.4 y 5.3 |
| 3 | DAT-01 recibió la revisión 2 y la zona horaria de la base. | 08/11, plan v0.3 | Plan, 1.4 y 5.4 |
| 4 | Se agregó una prueba automática a TC-06 (reutilizar la cookie tras cerrar sesión), además de la revisión manual. | 08/11, plan v0.3 | Plan, 5.3 |
| 5 | La demo se ajustó a la zona horaria del servidor porque con UTC el bloqueo de TC-09 no se activaba (DEF-03). | 08/11 | `avances.md` (HAL-05) y `defectos.md` |
| 6 | Se agregaron TC-07, TC-08 y TC-09 para cubrir R03, R06 y R08, que no tenían caso en el Taller 5. | Plan v0.1 | Plan, 5.3 |
| 7 | Se registraron los casos TC-10 a TC-17 (dos por integrante) sin ejecutarlos. | 10/11, plan v0.4 | Plan, 1.4 y 5.3 |
| 8 | El cronograma se ajustó a la exposición del 17/11. | 10/11, plan v0.5 | Plan, 1.4 y 8 |
| 9 | En TC-05 los dos Excel se bajaron con la misma sesión y la misma petición que usa el botón, porque el navegador integrado no dejó guardar la descarga. | 12/11 | `ejecucion-manual.md` (TC-05) |
| 10 | No se hizo regresión ni retest en este ciclo porque no se corrigió ningún defecto. | 12/11 | Sección 5 de este informe |

---

## 7. Evaluación de los criterios de finalización

Criterios de la sección 5.5 del plan, comparados con lo registrado hasta hoy.

### 7.1 Módulos críticos (F02, F03, F04)

| Criterio | Estado | Detalle |
|---|---|---|
| 100 % de los casos P1 ejecutados | No se puede dar por cumplido | Los 4 casos P1 (TC-01, 02, 03, 07) tienen ejecución automática. Su ejecución manual está pendiente en `main`. |
| 100 % de las combinaciones de la tabla de decisión y de los valores límite | No se puede dar por cumplido | Los 6 valores límite del semáforo (TC-03) pasan en lo automático. Las pruebas de la tabla de decisión (TC-01 y TC-02) se ejecutaron en lo automático, pero sin la parte manual. |
| Ningún defecto crítico o alto abierto | No se cumple | DEF-01 es de severidad alta y sigue abierto. |

### 7.2 Módulos secundarios (F01, F05, F06)

| Criterio | Estado | Detalle |
|---|---|---|
| 100 % de los casos diseñados ejecutados | No se cumple | TC-08 (F05, R06) no tiene ejecución registrada en `main`. TC-05 (F06), TC-06 y TC-09 (F01) sí se ejecutaron. |
| Ningún defecto crítico abierto | Se cumple | No hay defectos críticos. |
| Máximo 2 defectos menores abiertos | Se cumple, en el límite | En estos módulos hay 2 abiertos: DEF-02 (R09) y DEF-03 (R08), ambos de severidad media. |

**Conclusión.** Con lo registrado hasta hoy, los criterios de finalización no se cumplen del todo. Faltan las partes manuales de los casos P1, el caso TC-08 y el cierre de DEF-01.

---

## 8. Riesgos residuales

| Riesgo | Situación |
|---|---|
| R01 | DEF-04 abierto. La parte manual de TC-01 y TC-02 está pendiente. |
| R02 | DEF-01 abierto (severidad alta): un líder sin departamento ve las métricas de todos los cursos. Es el riesgo residual más importante. |
| R03 | Cubierto solo en lo automático (TC-07). Manual pendiente. |
| R04 | Cubierto en lo automático (TC-03). Manual pendiente. |
| R05 | Sin cubrir en este ciclo: TC-04 no tiene ejecución registrada. |
| R06 | Sin cubrir en `main`: TC-08 no tiene ejecución registrada. |
| R07 | Cubierto: TC-05 pasa en manual y en automático para los dos departamentos. |
| R08 | TC-09 pasa con la base en `America/Bogota`. DEF-03 sigue abierto hasta revisar la zona horaria de producción. |
| R09 | DEF-02 abierto: una cookie copiada antes de cerrar sesión sigue funcionando. El comportamiento del navegador sí es correcto (TC-06 manual). TC-14 (cambio de contraseña con dos sesiones) no se ejecutó. |
| R10 | Aceptado sin pruebas en el plan (no hay entorno de carga). |

También quedan fuera de este ciclo, por decisión del plan: la integración con Moodle, el seguimiento a estudiantes y las pruebas de rendimiento. Los casos TC-10 a TC-17 quedan identificados, no ejecutados. TC-15 (fórmulas en el Excel exportado) es relevante para R07, que hoy solo se cubrió con datos normales.

---

## 9. Lecciones aprendidas

Observaciones basadas en lo que pasó en el ciclo:

- **Las pruebas automáticas dieron resultados antes que las manuales.** La corrida de pytest del 08/11 ya mostró los defectos DEF-01, DEF-02 y DEF-04. Conviene seguir automatizando primero lo que se puede, y dejar la parte manual para lo que se ve en pantalla.
- **Reiniciar la demo antes de cada corrida dio resultados repetibles.** Las corridas del 08/11 y del 12/11, hechas en computadores distintos, dieron el mismo resultado.
- **La zona horaria de la base afecta el bloqueo de login.** Se descubrió en la primera corrida de TC-09. En el próximo ciclo, la zona horaria debería estar en la lista de requisitos del entorno desde el principio.
- **Las hojas manuales se llenaron tarde.** A la fecha de este informe varias siguen vacías en `main`. En un próximo ciclo convendría repartir las fechas de ejecución manual desde el inicio y revisar el avance cada día.
- **Probar el comportamiento del navegador y el del servidor por separado sirve.** TC-06 pasa en el navegador pero falla en el servidor, y esa diferencia solo se vio por tener las dos pruebas.
- **Los casos de riesgo bajo también pueden encontrar defectos.** R09 tenía exposición baja y aun así produjo DEF-02.
- **Quedó pendiente un retest.** El plan lo contempla, pero sin cambios en SIDEM no hubo nada que repetir. Si el equipo de SIDEM corrige los defectos, conviene repetir TC-02, TC-06 y TC-09 con la demo reiniciada.

---

## 10. Reconocimiento del equipo

| Integrante | Aporte registrado en el repositorio |
|---|---|
| Marcos Duque Jaramillo | Líder de pruebas y entorno de demostración (Docker, imágenes y Drive del equipo). Casos TC-01 y TC-02. |
| Sebastián Díaz Jiménez | Pruebas automáticas con pytest y corrida completa del 12/11/2026. Casos TC-07 y TC-04. |
| Nicolás Castaño Durango | Datos de prueba DAT-01 y su verificación. Casos TC-03 y TC-08. |
| Julián Ramírez Molina | Ejecución manual de TC-05 y TC-06, revisión de TC-09 y este informe. |

---

## 11. Pendientes para cerrar la versión 1.0

- Registrar las ejecuciones manuales de TC-01, TC-02, TC-03, TC-04, TC-07 y TC-08 en `ejecucion-manual.md` y actualizar las secciones 3, 4, 7 y 8.
- Cambiar el estado de los defectos si se corrige alguno y repetir los casos afectados.
- Confirmar la zona horaria de la base de producción (DEF-03).
