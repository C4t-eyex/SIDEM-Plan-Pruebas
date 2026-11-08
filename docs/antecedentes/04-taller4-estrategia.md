> **Antecedente:** Taller 4, Estrategia de pruebas (13/10/2026). Fuente LaTeX en `entregables-previos/Taller4_SIDEM.tex`.

# Taller 4 — Estrategia de pruebas

## 3.1 Selección y priorización de riesgos

| ID | Módulo / Funcionalidad | Exposición | Prioridad | Nivel de prueba |
|---|---|---|---|---|
| R01 | F02 Gestión de usuarios y roles (acceso no permitido) | Alta (6) | P1 | Sistema |
| R04 | F04 Semáforo de cumplimiento (color incorrecto) | Alta (6) | P1 | Unitario y sistema |
| R09 | F01 Inicio de sesión (sesión activa tras cerrar sesión) | Baja (2) | P3 | Sistema |

## 3.2 Técnicas de diseño

- **R01 — Tablas de decisión.** El acceso depende de varias condiciones combinadas: el rol, la acción (consultar o modificar) y el departamento del curso (propio, ajeno o sin departamento). La tabla cubre todas las combinaciones, incluido el usuario sin departamento, que no debe ver ningún curso.
- **R04 — Valores límite** (complemento): puntos donde cambia el color (50 % y 80 %).
- **R09 — Lista de chequeo.** Exposición baja: cerrar sesión y volver atrás, cambiar la contraseña y reutilizar la sesión, dejar expirar la sesión.

## 3.3 Criterios de finalización y cobertura

- **Módulos críticos (F02, F03, F04):** 100 % de los requerimientos cubiertos; 100 % de las combinaciones de la tabla de decisión y de los valores límite; ningún defecto crítico o alto abierto; cada caso lo revisa un integrante distinto al que lo diseñó.
- **Módulos secundarios (F01, F05, F06):** al menos 80 % de los requerimientos; 100 % de los casos diseñados ejecutados; ningún defecto crítico abierto; máximo 2 defectos menores abiertos.

## 3.4 Estimación de esfuerzo

| Actividad | Horas |
|---|---|
| Diseño de casos de prueba | 8 |
| Preparación de entorno y datos | 4 |
| Ejecución (ciclo 1) y reporte de defectos | 10 |
| Regresión y retest | 5 |
| Informe de cierre | 3 |
| **Total** | **30** (≈ 7,5 h por integrante) |
