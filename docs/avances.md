# Bitácora de avances

Registro de lo que se hace en el proyecto, del más reciente al más antiguo. Reemplaza los informes de estado formales (ver tailoring, sección 2.3 del plan).

| Fecha | Quién | Avance | Siguiente paso |
|---|---|---|---|
| 08/11/2026 | Equipo | Se monta la demo de SIDEM con Docker y datos ficticios (`demo/`). Al revisar el sistema se ajustan TC-01, TC-03 y DAT-01 en el plan (v0.2). Aparecen dos hallazgos (ver abajo). | Que cada integrante levante la demo en su equipo y revise sus casos. |
| 08/11/2026 | Equipo | Se crea el repositorio. Se consolidan Actividades 1 y 2, matriz de riesgos y Talleres 4 y 5. Primer borrador del plan (v0.1) con tailoring, trazabilidad y cronograma. | Revisar el plan con el docente (`preguntas-para-el-profe.md`). |
| 13/10/2026 | Equipo | Talleres 4 (estrategia) y 5 (casos y procedimientos). | — |
| — | Equipo | Matriz de riesgos R01–R10 y RP1–RP3. | — |
| 29/09/2026 | Equipo | Actividad 2 con coevaluación del equipo de RESTful Booker. | — |
| 22/09/2026 | Equipo | Actividad 1: alcance y metodología. | — |

## Hallazgos encontrados antes de la ejecución formal

Salieron al montar la demo. Se registran aquí para confirmarlos en la fase 3 con su caso de prueba y su evidencia.

| ID | Qué se observó | Dónde | Relación con el plan | Estado |
|---|---|---|---|---|
| HAL-01 | `sql/db.sql` no se puede ejecutar completo en una base nueva: la migración de `seguimientos_estudiantes` usa la columna `estado_seguimiento`, que en una instalación nueva no existe. | `sql/db.sql`, línea 593 aprox. | Fuera del alcance (módulo de estudiantes), pero afecta la instalación. | Observado. La demo lo rodea sin cambiar SIDEM. |
| HAL-02 | Un líder de departamento **sin departamento asignado** ve las estadísticas de todos los cursos. Se esperaba que no viera ninguno. | `services/dashboard_service.py`: `if dept_lista:` toma la lista vacía como "sin filtro". | Riesgo R02, caso TC-02. | Pendiente de ejecutar TC-02 y registrar el defecto con evidencia. |
