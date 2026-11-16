# SIDEM - Plan y ejecución de pruebas de software

Trabajo final del curso **Pruebas de Software (2026-2)**. Aplica la norma **ISO/IEC/IEEE 29119-3** al sistema **SIDEM** (Sistema de Seguimiento de Docentes en Moodle).

**Equipo:** Marcos Duque Jaramillo · Sebastián Díaz Jiménez · Nicolás Cataño Durango · Julián Ramírez Molina
**Entrega y exposición:** martes 17/11/2026

## Por dónde empezar

| Documento | Para qué |
|---|---|
| [`docs/plan-de-pruebas.md`](docs/plan-de-pruebas.md) | **Documento principal.** Plan completo en las 8 secciones pedidas. |
| [`entrega/Plan_de_Pruebas_SIDEM.pdf`](entrega/Plan_de_Pruebas_SIDEM.pdf) | **El plan en PDF para el docente** (plan completo + anexo de defectos). Se regenera con `python entrega/generar_pdf.py`. |
| [`docs/resumen-para-el-docente.md`](docs/resumen-para-el-docente.md) | **Para la reunión con el docente.** Qué se muestra, cómo vamos y qué falta. |
| [`docs/preguntas-para-el-profe.md`](docs/preguntas-para-el-profe.md) | Preguntas al docente y sus respuestas (16/11). |
| [`docs/avances.md`](docs/avances.md) | Bitácora de avances y hallazgos. |
| [`docs/defectos.md`](docs/defectos.md) | Defectos encontrados en la ejecución. |
| [`docs/retest.md`](docs/retest.md) | **Guía del retest** de los defectos corregidos (Sebastián) y qué actualizar después (Julián). |
| [`docs/informe-de-cierre.md`](docs/informe-de-cierre.md) | Informe de cierre (*Test Completion Report*), a cargo de Julián. |
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
entrega/              PDF del plan para el docente y el script que lo genera
entregables-previos/  Actividades 1 y 2 (escaneadas y en LaTeX), Talleres 4 y 5 y script de la matriz
demo/                 Copia de demostración de SIDEM con datos ficticios (fase 2)
pruebas-automaticas/  Pruebas con pytest contra la demostración (fase 3)
evidencias/           Capturas y resultados de la ejecución (fase 3)
exposicion/           Diapositivas de cada integrante y guía de la exposición final
.github/              Plantilla para reportar defectos
```

## Fases

| Fase | Contenido | Estado |
|---|---|---|
| 1 | Organizar documentos y plan para revisión con el docente | Lista; respuestas del docente incorporadas (plan v0.6) |
| 2 | Demo de SIDEM con Docker y datos ficticios ([`demo/README.md`](demo/README.md)) | Lista, con imágenes del retest |
| 3 | Ejecución real (manual + automática), defectos y evidencias | Lista: 5 defectos corregidos y cerrados con el retest del 16/11 (19 de 19, [`docs/retest.md`](docs/retest.md)) |
| 4 | Informe de cierre y exposición | En curso |

> La versión de SIDEM bajo prueba es el commit `77f71b2`. El retest usa ese commit más los parches de [`demo/correcciones/`](demo/correcciones/). No se usan datos reales.
