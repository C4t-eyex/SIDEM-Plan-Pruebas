# Resumen para la revisión con el docente

**Proyecto:** plan y ejecución de pruebas de SIDEM según ISO/IEC/IEEE 29119-3.
**Equipo:** Marcos Duque Jaramillo, Sebastián Díaz Jiménez, Nicolás Cataño Durango y Julián Ramírez Molina.
**Docente:** Roberto José Calderón Bermejo.
**Fecha:** 08/11/2026, actualizado el 17/11/2026. **Entrega y exposición:** martes 17/11/2026.

Este documento resume el trabajo y cómo cerró. El detalle está en los documentos que se enlazan.

## 1. Qué es SIDEM y qué se prueba

SIDEM es el sistema que hace seguimiento a los cursos virtuales de los docentes en Moodle. Cada curso se revisa con unos criterios, y el sistema calcula un porcentaje y un color de semáforo (verde, amarillo o rojo).

Las pruebas se enfocan en lo que más riesgo tiene: quién puede ver y modificar qué (permisos por rol y por departamento), el cálculo del semáforo, que lo registrado quede en el curso correcto, el informe en Excel y el inicio y cierre de sesión.

## 2. Qué le vamos a mostrar

| Orden | Qué | Dónde |
|---|---|---|
| 1 | El plan de pruebas con las 8 secciones pedidas, el tailoring y la matriz de riesgos. | [`plan-de-pruebas.md`](plan-de-pruebas.md) |
| 2 | La trazabilidad: cada riesgo tiene su condición y su caso de prueba. | Plan, secciones 4 y 5 |
| 3 | La demo de SIDEM con datos ficticios, funcionando en el computador. | [`demo/README.md`](../demo/README.md) |
| 4 | La primera ejecución de las pruebas automáticas y los defectos encontrados. | [`defectos.md`](defectos.md), [`evidencias/pytest/`](../evidencias/pytest/) |
| 5 | Las preguntas al docente sobre formato y alcance, con sus respuestas. | [`preguntas-para-el-profe.md`](preguntas-para-el-profe.md) |

## 3. Cómo vamos

| Fase | Contenido | Estado |
|---|---|---|
| 1 | Plan de pruebas y organización de documentos | Listo (v1.0, con las respuestas del docente) |
| 2 | Demo de SIDEM con Docker y datos ficticios | Lista, con imágenes para el retest |
| 3 | Ejecución de las pruebas, defectos y evidencias | Lista: los 9 casos ejecutados, 5 defectos corregidos y cerrados con el retest |
| 4 | Informe de cierre y exposición | Lista: informe de cierre v1.0 y presentación unida |

**Primera ronda (08 y 12/11/2026):** 19 pruebas automáticas sobre 7 casos; 16 pasan y 3 fallan por defectos de SIDEM, no por errores de la prueba. Los 9 casos se ejecutaron también a mano, con capturas en [`evidencias/`](../evidencias/README.md).

**Defectos registrados:** 5 (1 alto, 2 medios y 2 bajos). El más importante es que un líder de departamento sin departamento asignado podía ver las métricas de toda la institución.

**Correcciones y retest (16/11/2026):** cada defecto tiene su corrección en [`demo/correcciones/`](../demo/correcciones/), con una prueba automática. En el retest, con la base en UTC, pasan las 19 pruebas y los 5 defectos quedan cerrados ([`retest.md`](retest.md)).

**Cambios al plan por lo que se encontró:** al revisar el sistema real, dos casos del Taller 5 no coincidían con su funcionamiento (TC-01 y TC-03) y se ajustaron. El historial está en la sección 1.4 del plan.

## 4. Cierre

- **Informe de cierre v1.0** ([`informe-de-cierre.md`](informe-de-cierre.md)): los 9 casos ejecutados y pasando después del retest, 0 defectos abiertos y todos los criterios de finalización del plan cumplidos. Lo completaron Marcos, como encargado de organizar la exposición, y Nicolás.
- **Issues #1 a #5** cerrados en GitHub con el resultado del retest.
- **Presentación unida** para el 17/11 ([`exposicion/README.md`](../exposicion/README.md)), con el antes y después de cada defecto y las láminas de retest y cierre.

## 5. Lo que confirmó el docente (16/11)

Las respuestas completas están en [`preguntas-para-el-profe.md`](preguntas-para-el-profe.md). Las principales:

1. El trabajo queda en el repositorio y al final se entrega en PDF (LaTeX o Markdown, da igual).
2. El tailoring es aceptable. Se citan cláusulas de la norma solo si apoyan la exposición.
3. La exposición dura de 20 a 30 minutos y muestra el aplicativo antes y después de las correcciones, con el video de la demo.
