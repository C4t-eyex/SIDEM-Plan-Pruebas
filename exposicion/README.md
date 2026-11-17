# Exposición final - SIDEM

**Fecha:** martes 17/11/2026 · **Duración:** 20 a 30 minutos (el docente acepta ese rango) · **Ensayo:** 16/11/2026.

Lo que el docente pidió destacar (ver [`docs/preguntas-para-el-profe.md`](../docs/preguntas-para-el-profe.md)):

1. Qué casos pueden perjudicar el aplicativo y qué se hizo para solucionarlo.
2. Cómo estaba SIDEM **antes** y **después** de las correcciones (con el video).
3. Las cláusulas de la norma solo cuando ayuden a explicar, en lenguaje sencillo.
4. Los 9 casos (TC-01 a TC-09) son los que se probaron; TC-07 a TC-09 se agregaron para complementar. TC-10 a TC-17 solo se mencionan como identificados y no ejecutados.

## Orden propuesto (unos 25 minutos)

La historia sigue el orden del trabajo: qué se planeó → cómo se probó → qué se encontró → qué se corrigió → cómo cerró.

| # | Parte | Quién | Láminas | Tiempo | Mensaje principal |
|---|---|---|---|---|---|
| 1 | SIDEM, plan y tailoring | Marcos | `Marcos_plan_y_riesgos.pptx` 1-2 | 4 min | Qué es SIDEM, qué se probó (versión congelada `77f71b2`) y qué se adaptó de la norma sin perder la trazabilidad. |
| 2 | Matriz de riesgos | Marcos | `Marcos_plan_y_riesgos.pptx` 3 | 2 min | Los 4 riesgos altos (R01 a R04) se volvieron casos P1. Ninguno llega a crítico. Menciona TC-16 y TC-17. |
| 3 | Valores límite (TC-03, TC-08) | Nicolás | `Nicolas_valores_limite.pptx` 1-2 | 3 min | Los errores están en los bordes: 80 %, 77 %, 50 %, 47 %. Los 6 cursos y los totales salieron bien. Menciona TC-12 y TC-13. |
| 4 | Pruebas automáticas | Sebastián | `Sebastian_pruebas_automaticas.pptx` 1-2 | 4 min | pytest contra la API. Primera ronda: 16 de 19, y los 3 fallos eran defectos de SIDEM. Menciona TC-10 y TC-11. |
| 5 | Defectos y correcciones (antes / después) | Marcos | `Marcos_defectos_y_correcciones.pptx` 1-7 | 8 min | **Todos** los defectos encontrados (DEF-01 a DEF-05), cada uno con qué hacía SIDEM antes de corregirlo y qué hace después. Video de DEF-01 y DEF-02. |
| 6 | Retest y cierre | Julián | `Julian_cierre.pptx` (falta) | 4 min | Retest: 19 de 19. Estado final de los defectos, criterios de finalización cumplidos y lecciones aprendidas. Menciona TC-14 y TC-15. |
| 7 | Preguntas | Todos | - | 2-5 min | - |

## Material del video

En la carpeta compartida del equipo (no va al repositorio por el peso):

| Archivo | Qué muestra |
|---|---|
| `DEF-01_antes_lider_sin_departamento_ve_todo.gif` | `lider.sindep` entra a Métricas y ve los cursos de toda la institución. |
| `DEF-01_despues_lider_sin_departamento_no_ve_cursos.gif` | El mismo usuario ve 0 cursos y "Sin datos". |
| `DEF-02_antes_sesion_cerrada_reutilizable.gif` | La cookie copiada sigue sirviendo después de cerrar sesión (200). |
| `DEF-02_despues_sesion_cerrada_no_se_reutiliza.gif` | La cookie copiada da 401 "Sesión expirada". |

Ya están dentro de `Marcos_defectos_y_correcciones.pptx` (antes a la izquierda, después a la derecha). Los GIF se mueven solos en modo presentación; en la vista de edición o en PDF solo se ve el primer cuadro.

## Contenido de la lámina 5 (defectos y correcciones)

> **Decisión de Marcos (16/11):** en la presentación van **todos** los defectos encontrados, no solo los del video. Cada uno se muestra con el **antes** (qué hacía SIDEM al encontrarlo) y el **después** (qué hace con la corrección), con su evidencia: GIF para DEF-01 y DEF-02, y capturas o resultados del retest para DEF-03, DEF-04 y DEF-05 (ver `evidencias/README.md`, sección "Retest").
>
> Los casos agregados **TC-06 a TC-09** siguen una dinámica parecida, como pruebas: qué se quería comprobar, cómo se probó y qué resultado dio. TC-06 y TC-09 encontraron DEF-02 y DEF-03, así que se ven con antes y después; TC-07 y TC-08 pasaron sin defecto. **TC-10 a TC-17** solo se mencionan.

| Defecto | Riesgo | Qué pasaba | Qué se hizo |
|---|---|---|---|
| DEF-01 (alta) | R02 | Un líder sin departamento veía todas las métricas. | Sin departamento no ve nada; al crear el usuario el departamento es obligatorio, con opción "Todos". |
| DEF-02 | R09 | La sesión cerrada se podía reutilizar con la cookie copiada. | Contador de sesión `token_version`: al cerrar sesión, los tokens anteriores dejan de servir. |
| DEF-03 | R08 | El bloqueo de login dependía de la zona horaria de la base. | La fecha la pone la aplicación en UTC; TC-09 pasa con la base en UTC. |
| DEF-04 | R01 | Un rol personalizado con permiso no veía cursos. | Misma regla que DEF-01: alcance explícito. |
| DEF-05 | - | `db.sql` fallaba en una base nueva. | El paso de migración solo corre si la columna vieja existe. |

Mensaje para decir: las correcciones están como parches sobre la versión probada (`demo/correcciones/`), con una prueba automática cada una. Las 650 pruebas de SIDEM siguen pasando.

## Qué falta para unir la presentación

| Pendiente | Quién | Depende de |
|---|---|---|
| Diapositivas del cierre (`Julian_cierre.pptx`) | Julián | - (el retest ya está: 19 de 19, defectos cerrados) |
| Unir las 4 presentaciones en `Exposicion_SIDEM.pptx` con portada, agenda y cierre | Marcos | Todas las anteriores |
| Ensayo completo cronometrado | Todos | Presentación unida |

## Consejos para el ensayo

- Cada uno dice primero la idea principal de su parte y después el detalle.
- Al mencionar los casos no ejecutados, basta una frase por caso: qué se quería probar y por qué no se alcanzó (tiempo del ciclo, riesgo RP2).
- Si el docente pregunta por la norma, las respuestas están en el plan (sección 2.3 para el tailoring y sección 4 para los riesgos).
