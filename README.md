# SIDEM - Plan y ejecución de pruebas de software

Trabajo final del curso **Pruebas de Software (2026-2)**. Aplica la norma **ISO/IEC/IEEE 29119-3** al sistema **SIDEM** (Sistema de Seguimiento de Docentes en Moodle).

**Equipo:** Marcos Duque Jaramillo · Sebastián Díaz Jiménez · Nicolás Cataño Durango · Julián Ramírez Molina
**Entrega y exposición:** martes 17/11/2026

## Entrega final

| Entregable | Qué es |
|---|---|
| [`entrega/Informe_final_SIDEM.pdf`](entrega/Informe_final_SIDEM.pdf) | **Informe final en LaTeX** (61 páginas): plan, ejecución, defectos con su antes y después, correcciones, retest, informe de cierre y anexos. Fuente: [`entrega/Informe_final_SIDEM.tex`](entrega/Informe_final_SIDEM.tex). Se regenera desde los Markdown con `python entrega/generar_informe.py` (requiere MiKTeX o TeX Live). |
| [`exposicion/Exposicion_SIDEM.pptx`](exposicion/Exposicion_SIDEM.pptx) | **Presentación de la exposición** (20 láminas), también en [PDF](exposicion/Exposicion_SIDEM.pdf). Guía en [`exposicion/README.md`](exposicion/README.md). |

## Por dónde empezar

| Documento | Para qué |
|---|---|
| [`docs/plan-de-pruebas.md`](docs/plan-de-pruebas.md) | **Documento principal.** Plan completo en las 8 secciones pedidas. |
| [`entrega/Plan_de_Pruebas_SIDEM.pdf`](entrega/Plan_de_Pruebas_SIDEM.pdf) | El plan solo en PDF (plan completo + anexo de defectos). Se regenera con `python entrega/generar_pdf.py`. |
| [`docs/resumen-para-el-docente.md`](docs/resumen-para-el-docente.md) | **Para el docente.** Qué se muestra, cómo se hizo y cómo cerró. |
| [`docs/preguntas-para-el-profe.md`](docs/preguntas-para-el-profe.md) | Preguntas al docente y sus respuestas (16/11). |
| [`docs/avances.md`](docs/avances.md) | Bitácora de avances y hallazgos. |
| [`docs/defectos.md`](docs/defectos.md) | Defectos encontrados en la ejecución. |
| [`docs/retest.md`](docs/retest.md) | **Guía del retest** de los defectos corregidos y su resultado (19 de 19). |
| [`docs/informe-de-cierre.md`](docs/informe-de-cierre.md) | Informe de cierre (*Test Completion Report*), versión final 1.0. |
| [`docs/ejecucion-manual.md`](docs/ejecucion-manual.md) | Hojas para ejecutar los casos manuales. |
| [`docs/antecedentes/`](docs/antecedentes/) | Entregas previas (Actividades 1 y 2, matriz de riesgos, Talleres 4 y 5). |

## Cómo encaja todo

```
Actividad 1 (alcance) → Actividad 2 (funcionalidades F01-F06) → Matriz de riesgos (R01-R10)
   → Taller 4 (estrategia y técnicas) → Taller 5 (casos TC y procedimientos)
   → Plan final (trazabilidad riesgo → condición → caso) → Ejecución real → Informe de cierre
```

## Estructura del repositorio

```
docs/                 Plan, bitácora, preguntas y antecedentes
entrega/              Informe final (LaTeX y PDF), PDF del plan y los scripts que los generan
entregables-previos/  Actividades 1 y 2 (escaneadas y en LaTeX), Talleres 4 y 5 y script de la matriz
demo/                 Copia de demostración de SIDEM con datos ficticios (fase 2)
pruebas-automaticas/  Pruebas con pytest contra la demostración (fase 3)
evidencias/           Capturas y resultados de la ejecución (fase 3)
exposicion/           Presentación final (pptx y PDF), GIF del antes y después y guía de la exposición
.github/              Plantilla para reportar defectos
```

## Fases

| Fase | Contenido | Estado |
|---|---|---|
| 1 | Organizar documentos y plan para revisión con el docente | Lista; plan final v1.0 con las respuestas del docente |
| 2 | Demo de SIDEM con Docker y datos ficticios ([`demo/README.md`](demo/README.md)) | Lista, con imágenes del retest |
| 3 | Ejecución real (manual + automática), defectos y evidencias | Lista: 5 defectos corregidos y cerrados con el retest del 16/11 (19 de 19, [`docs/retest.md`](docs/retest.md)) |
| 4 | Informe de cierre, informe final y exposición | Lista: informe de cierre v1.0 (criterios de finalización cumplidos), informe final en LaTeX ([`entrega/`](entrega/Informe_final_SIDEM.pdf)) y presentación en [`exposicion/`](exposicion/README.md) |

> La versión de SIDEM bajo prueba es el commit `77f71b2`. El retest usa ese commit más los parches de [`demo/correcciones/`](demo/correcciones/). No se usan datos reales.
