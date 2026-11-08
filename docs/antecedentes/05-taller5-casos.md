> **Antecedente:** Taller 5, Especificación y procedimientos de prueba (cláusulas 7.2 a 7.6). Fuente LaTeX en `entregables-previos/Taller5_SIDEM.tex`.

# Taller 5 — Casos, procedimientos, datos y entorno

## Caso piloto TC-01 (P1)

- **Conjunto de características (7.2.4):** CC-01, Gestión de usuarios y roles (F02), control de acceso por rol y departamento.
- **Condición (7.2.5):** CP-01, un usuario solo puede modificar el seguimiento de los cursos de su propio departamento.
- **Precondiciones:** usuario con rol Líder de departamento de Sistemas Digitales con sesión iniciada; curso de Producción con revisión abierta.
- **Pasos:** 1) Ingresar al módulo de seguimiento. 2) Abrir el curso de Producción. 3) Modificar un criterio y una observación. 4) Guardar.
- **Resultado esperado:** acceso denegado; al consultar con un administrador, los datos conservan sus valores originales.

## Matriz de casos

| ID | Prioridad | Condición | Precondiciones | Entradas | Resultado esperado |
|---|---|---|---|---|---|
| TC-01 | P1 | Un usuario no modifica cursos de otro departamento (R01). | Líder de Sistemas Digitales; curso de Producción con revisión abierta. | Editar un criterio y guardar. | Acceso denegado; los datos no cambian. |
| TC-02 | P1 | Cada rol accede solo a lo que su permiso y departamento le permiten (R01). | Usuario de solo consulta y usuario sin departamento. | Abrir el listado e intentar guardar. | El de consulta ve sin guardar; el sin departamento no ve cursos. |
| TC-03 | P1 | El semáforo cambia en 50 % y 80 % (R04). | Cuatro cursos con 10 criterios evaluados. | 4, 5, 7 y 8 cumplidos. | Rojo, amarillo, amarillo, verde. |
| TC-04 | P2 | La información se conserva al guardar y recargar (R05). | Revisor con un curso asignado. | Marcar criterios, observación, guardar, recargar. | Todo se muestra igual. |
| TC-05 | P2 | El informe exportado coincide con la pantalla (R07). | Revisión con cursos de dos departamentos. | Exportar filtrado por Sistemas Digitales. | Mismos cursos, criterios y colores. |
| TC-06 | P3 | Una sesión cerrada no se reutiliza (R09). | Usuario con sesión iniciada. | Cerrar sesión y usar "Atrás". | Redirige al login sin mostrar información. |

> Con 10 criterios no se puede obtener 49 % ni 79 %; por eso se usan 40/50/70/80 % como valores a cada lado de los límites.

## Procedimientos

- **PROC-01 (P1):** TC-01 → TC-02 → TC-03. Preparación: iniciar SIDEM en AMB-01, cargar DAT-01, cerrar sesiones, limpiar caché. Cierre: restaurar la BD y cerrar sesiones.
- **PROC-02 (P2):** TC-04 → TC-05. Cierre: eliminar los archivos exportados y restaurar la BD.
- **PROC-03 (P3):** TC-06.

## Datos (7.5) y entorno (7.6)

- **DAT-01:** 4 usuarios (administrador, revisor, líder de Sistemas Digitales, usuario sin departamento); 6 cursos (3 de Sistemas Digitales, 3 de Producción); 10 criterios en la revisión 1, con 4, 5, 7 y 8 cumplidos. Reinicio desde respaldo antes de cada ciclo.
- **AMB-01:** servidor de pruebas separado de producción; SIDEM en la versión fijada (Python 3, FastAPI, PostgreSQL); Google Chrome; sin conexión a Moodle.

**Pendiente cerrado en el plan final:** versión fijada = commit `77f71b2` de SIDEM.
