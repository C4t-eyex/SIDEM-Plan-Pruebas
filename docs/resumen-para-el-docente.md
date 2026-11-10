# Resumen para la revisión con el docente

**Proyecto:** plan y ejecución de pruebas de SIDEM según ISO/IEC/IEEE 29119-3.
**Equipo:** Marcos Duque Jaramillo, Sebastián Díaz Jiménez, Nicolás Castaño Durango y Julián Ramírez Molina.
**Docente:** Roberto José Calderón Bermejo.
**Fecha:** 08/11/2026. **Entrega y exposición:** martes 17/11/2026.

Este documento resume en qué va el trabajo y qué queremos revisar con usted. El detalle está en los documentos que se enlazan.

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
| 5 | Las dudas que tenemos sobre el formato y el alcance. | [`preguntas-para-el-profe.md`](preguntas-para-el-profe.md) |

## 3. Cómo vamos

| Fase | Contenido | Estado |
|---|---|---|
| 1 | Plan de pruebas y organización de documentos | Listo para revisión (v0.3) |
| 2 | Demo de SIDEM con Docker y datos ficticios | Lista |
| 3 | Ejecución de las pruebas, defectos y evidencias | En curso: automáticas ejecutadas, manuales pendientes |
| 4 | Informe de cierre y exposición | Pendiente |

**Primera ejecución automática (08/11/2026):** 19 pruebas sobre 7 casos. 16 pasan y 3 fallan. Los fallos corresponden a defectos de SIDEM, no a errores de la prueba.

**Defectos registrados:** 5 (1 alto, 2 medios y 2 bajos). El más importante es que un líder de departamento sin departamento asignado puede ver las métricas de toda la institución. Se registró todo lo que no coincide con lo esperado en el plan, aunque en algún caso pueda ser una decisión de diseño de SIDEM.

**Cambios al plan por lo que se encontró:** al revisar el sistema real, dos casos del Taller 5 no coincidían con su funcionamiento (TC-01 y TC-03) y se ajustaron. El historial está en la sección 1.4 del plan.

## 4. Qué falta y quién lo hace

| Integrante | Casos | Pendiente |
|---|---|---|
| Marcos | TC-01, TC-02 | Ejecución manual en el navegador y mantener la demo. |
| Sebastián | TC-07, TC-04 | Ejecución manual de TC-04 y mantener las pruebas automáticas. |
| Nicolás | TC-03, TC-08 | Ejecución manual y revisión de los datos de prueba. |
| Julián | TC-05, TC-09, TC-06 | Ejecución manual de TC-05 y TC-06, y redactar el informe de cierre. |

Las hojas para la ejecución manual están en [`ejecucion-manual.md`](ejecucion-manual.md). Después vienen el retest de los defectos y el informe de cierre (15/11 y 16/11, según el cronograma).

## 5. Lo que necesitamos que nos confirme

Las preguntas completas están en [`preguntas-para-el-profe.md`](preguntas-para-el-profe.md). Las principales:

1. Si el formato en Markdown dentro de un repositorio sirve como entrega.
2. Si el tailoring que hicimos (documentos que juntamos u omitimos) es aceptable.
3. Si en la exposición se espera una demo en vivo o basta con las evidencias.
