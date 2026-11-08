# SIDEM - Plan y ejecución de pruebas de software

Trabajo final del curso **Pruebas de Software (2026-2)**. Aplica la norma **ISO/IEC/IEEE 29119-3** al sistema **SIDEM** (Sistema de Seguimiento de Docentes en Moodle).

**Equipo:** Marcos Duque Jaramillo · Sebastián Díaz Jiménez · Nicolás Castaño Durango · Julián Ramírez Molina
**Entrega y exposición:** ≈ 28/11/2026

## Por dónde empezar

| Documento | Para qué |
|---|---|
| [`docs/plan-de-pruebas.md`](docs/plan-de-pruebas.md) | **Documento principal.** Plan completo en las 8 secciones pedidas. |
| [`docs/resumen-para-el-docente.md`](docs/resumen-para-el-docente.md) | **Para la reunión con el docente.** Qué se muestra, cómo vamos y qué falta. |
| [`docs/preguntas-para-el-profe.md`](docs/preguntas-para-el-profe.md) | Dudas para validar con el docente. |
| [`docs/avances.md`](docs/avances.md) | Bitácora de avances y hallazgos. |
| [`docs/defectos.md`](docs/defectos.md) | Defectos encontrados en la ejecución. |
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
entregables-previos/  Fuentes LaTeX de los talleres y script de la matriz
demo/                 Copia de demostración de SIDEM con datos ficticios (fase 2)
pruebas-automaticas/  Pruebas con pytest contra la demostración (fase 3)
evidencias/           Capturas y resultados de la ejecución (fase 3)
.github/              Plantilla para reportar defectos
```

## Fases

| Fase | Contenido | Estado |
|---|---|---|
| 1 | Organizar documentos y plan para revisión con el docente | Lista para revisión |
| 2 | Demo de SIDEM con Docker y datos ficticios ([`demo/README.md`](demo/README.md)) | Lista |
| 3 | Ejecución real (manual + automática), defectos y evidencias | En curso: automáticas ejecutadas, manuales pendientes |
| 4 | Informe de cierre y exposición | Pendiente |

> La versión de SIDEM bajo prueba es el commit `77f71b2`. No se usan datos reales.
