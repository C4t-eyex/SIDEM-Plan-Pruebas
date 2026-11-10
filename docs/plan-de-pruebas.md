# Plan de Pruebas de Software - SIDEM

> Basado en la norma ISO/IEC/IEEE 29119-3 (Documentación de pruebas), adaptada a un ciclo de 3 semanas.
> **Estado:** BORRADOR v0.4 - pendiente de revisión con el docente.

---

## 1. Información específica del documento

### 1.1 Identificador único del documento
`SIDEM-PP-2026-01` (Plan de Pruebas, versión 0.4)

### 1.2 Organización emisora y autores
- **Organización:** Equipo SIDEM - curso Pruebas de Software, 2026-2.
- **Autores:** Marcos Duque Jaramillo, Sebastián Díaz Jiménez, Nicolás Castaño Durango, Julián Ramírez Molina.

### 1.3 Autoridad de aprobación
Roberto José Calderón Bermejo, docente del curso de Pruebas de Software.

### 1.4 Historial de cambios y control de versiones

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 0.1 | 08/11/2026 | Equipo SIDEM | Primer borrador: consolida Actividades 1 y 2, matriz de riesgos y Talleres 4 y 5. |
| 0.2 | 08/11/2026 | Equipo SIDEM | Ajuste de TC-01, TC-03 y DAT-01 según el funcionamiento real de SIDEM, revisado al montar la demo. |
| 0.3 | 08/11/2026 | Equipo SIDEM | DAT-01 con revisión 2 y zona horaria de la base; complemento automático de TC-06. |
| 0.4 | 10/11/2026 | Equipo SIDEM | Casos identificados no ejecutados TC-10 a TC-17 (dos por integrante), según indicación del docente. |

El control de versiones del documento se lleva en este repositorio (historial de commits de Git).

---

## 2. Introducción y declaración de adaptación (Tailoring)

### 2.1 Alcance del documento
Este plan define qué se va a probar de SIDEM, por qué, cómo, con qué recursos y en qué tiempo. Cubre las pruebas funcionales, de control de acceso por roles y de confiabilidad de las métricas del **seguimiento a docentes**.

**Sistema bajo prueba.** SIDEM (Sistema de Seguimiento de Docentes en Moodle) es una aplicación web en Python (FastAPI) con base de datos PostgreSQL. Permite a los revisores evaluar criterios de acompañamiento docente por curso y por revisión del semestre. Además, muestra a los líderes académicos un semáforo de cumplimiento y un panel de métricas.

### 2.2 Referencias documentales

| ID | Documento |
|---|---|
| REF-01 | ISO/IEC/IEEE 29119-3:2021 - Software testing: Test documentation. |
| REF-02 | ISO/IEC/IEEE 29119-4 - Software testing: Test techniques. |
| REF-03 | Actividad 1: Alcance y metodología (`antecedentes/01-actividad1-alcance.md`). |
| REF-04 | Actividad 2: Objeto de prueba y condiciones (`antecedentes/02-actividad2-objeto-condiciones.md`). |
| REF-05 | Matriz de riesgos SIDEM (`antecedentes/03-matriz-de-riesgos.md`). |
| REF-06 | Taller 4: Estrategia de pruebas (`antecedentes/04-taller4-estrategia.md`). |
| REF-07 | Taller 5: Especificación de casos y procedimientos (`antecedentes/05-taller5-casos.md`). |
| REF-08 | Repositorio de SIDEM, en la versión fijada para pruebas (ver 3.1). |

### 2.3 Conformidad y adaptación (Tailoring)

**Declaración.** El proyecto aplica la norma ISO/IEC/IEEE 29119-3 con **conformidad adaptada (tailored conformance)**, no con conformidad completa.

**Justificación.** SIDEM es un sistema académico interno de **criticidad media**. Una falla no pone en riesgo vidas ni dinero, pero afecta las decisiones académicas y la confidencialidad de la información de los docentes. Además, el proyecto tiene una restricción fuerte: **3 semanas de duración** con un equipo de 4 estudiantes a tiempo parcial.

**Qué se conserva.** Se mantiene completo todo lo que da trazabilidad: el plan, el análisis de riesgos, la estrategia, las condiciones, los casos, los procedimientos, los datos, el entorno, los reportes de defectos y el informe de cierre.

**Qué se excluye o se simplifica, y qué riesgo se asume:**

| Elemento de la norma | Decisión | Justificación | Riesgo asumido |
|---|---|---|---|
| Documentación organizacional (política y estrategia organizacional de pruebas, cl. 6.2 y 6.3) | Excluido | No existe una organización de pruebas; el plan es de un solo proyecto. | Bajo. No hay otros proyectos que deban alinearse. |
| Especificaciones de diseño, casos y procedimientos como documentos separados | Consolidados en este plan y en `antecedentes/05` | Reduce la duplicación en un ciclo corto. | Bajo. La trazabilidad se conserva en la matriz 5.3. |
| Informes de estado periódicos (*test status report*) | Simplificados | Se reemplazan por la bitácora `avances.md` y el tablero del repositorio. | Medio. Hay menos visibilidad formal del avance; se mitiga con revisión semanal del equipo. |
| Reporte de incidentes formal (*incident report*) | Simplificado | Se usa una plantilla de *issue* en GitHub con los campos mínimos de la norma. | Bajo. Se conservan los campos esenciales. |
| Pruebas de rendimiento (R10) | Excluidas | La exposición del riesgo es baja (2) y no hay entorno de carga. | Bajo. Se acepta y queda documentado en 4.3. |
| Integración con Moodle y seguimiento a estudiantes | Excluidos | No hay una instancia de Moodle disponible; el módulo de estudiantes está en beta. | Medio. Los criterios automáticos que consultan Moodle no se validan en este ciclo. |

### 2.4 Glosario

| Término | Definición sencilla |
|---|---|
| Caso de prueba (TC) | Prueba concreta con precondiciones, pasos y resultado esperado. |
| Condición de prueba (CP) | Regla del sistema que se puede verificar. |
| Criterio | Aspecto del acompañamiento docente que se evalúa en un curso (por ejemplo, responder en el foro). |
| Defecto | Diferencia entre el resultado obtenido y el esperado. |
| Exposición al riesgo | Probabilidad × impacto. |
| Revisión | Cada uno de los 4 cortes del semestre en los que se evalúan los cursos. |
| Semáforo | Color del curso según el % de cumplimiento: verde ≥ 80 %, amarillo 50-79 %, rojo < 50 %. El % es ponderado: cada criterio tiene un peso (en la revisión 1 suman 30). |
| Tailoring | Adaptación justificada de la norma a las condiciones del proyecto. |

---

## 3. Contexto de las pruebas

### 3.1 Elementos de prueba (Test items)

| Elemento | Detalle |
|---|---|
| Sistema | SIDEM - API FastAPI + interfaz web (plantillas HTML). |
| Versión bajo prueba | Commit `77f71b2` de la rama `main` del repositorio de SIDEM. Se congela durante el ciclo (mitiga RP3). |
| Instancia de prueba | Copia de demostración con **datos ficticios**, levantada con Docker (ver 5.4). No se usa la base de producción. |

### 3.2 Alcance y exclusiones de las pruebas

**Funcionalidades en alcance** (definidas en la Actividad 2):

| ID | Funcionalidad | Actor principal |
|---|---|---|
| F01 | Inicio de sesión | Todos los usuarios |
| F02 | Gestión de usuarios y roles | Administrador |
| F03 | Registro del seguimiento a docentes | Revisor |
| F04 | Semáforo de cumplimiento | Líderes académicos |
| F05 | Panel de métricas | Líderes académicos, administrador |
| F06 | Exportación de informes | Revisor, líderes académicos |

**Exclusiones:**
- Seguimiento a estudiantes (módulo en beta).
- Verificación automática contra Moodle (no hay instancia disponible).
- Importación de seguimientos anteriores.
- Pruebas de rendimiento y carga (R10 aceptado).

### 3.3 Suposiciones y restricciones
- **S1.** La versión fijada de SIDEM no cambia durante el ciclo. Si se corrige un defecto, se registra el nuevo commit y se hace regresión.
- **S2.** Los datos ficticios representan los casos reales: varios departamentos, todos los roles y cursos con distintos porcentajes de cumplimiento.
- **R1.** Duración total de 3 semanas (09/11/2026 al 27/11/2026).
- **R2.** Equipo de 4 personas a tiempo parcial, unas 7,5 horas cada una.
- **R3.** No se puede usar información real de docentes, por confidencialidad.

### 3.4 Partes interesadas

| Parte interesada | Interés |
|---|---|
| Docente del curso (Roberto José Calderón Bermejo) | Evalúa el plan y su ejecución; aprueba el documento. |
| Equipo de pruebas (4 integrantes) | Diseña, ejecuta y reporta las pruebas. |
| Líderes académicos (usuarios de SIDEM) | Necesitan que las métricas y el semáforo sean confiables. |
| Revisores (usuarios de SIDEM) | Necesitan que lo que registran se guarde bien. |
| Desarrollador de SIDEM | Recibe los defectos y los corrige. |

---

## 4. Gestión de riesgos y matriz de exposición (RBT)

### 4.1 Identificación de riesgos

**Escalas.** La probabilidad y el impacto van de 1 (bajo) a 3 (alto). Exposición = P × I.

**Riesgos del producto:**

| ID | Riesgo | Causa / consecuencia | Funcionalidad | P | I |
|---|---|---|---|---|---|
| R01 | Un usuario puede ver o modificar información que su rol no le permite. | Permisos mal aplicados; se exponen o alteran datos. | F02 | 2 | 3 |
| R02 | Un usuario ve cursos o docentes de un departamento que no le corresponde. | El filtro por departamento no se aplica en todas las pantallas. | F02 | 2 | 3 |
| R03 | Los criterios u observaciones se guardan en el curso o la revisión equivocados. | Error al asociar el registro; resultados alterados. | F03 | 2 | 3 |
| R04 | El semáforo muestra un color que no corresponde al porcentaje. | Error en el cálculo o en los límites (80 % y 50 %). | F04 | 2 | 3 |
| R05 | Se pierde información registrada al editar o recargar. | Falla al guardar; el revisor repite el trabajo. | F03 | 2 | 2 |
| R06 | Las métricas no coinciden con lo registrado. | Duplicados o filtros mal aplicados. | F05 | 2 | 2 |
| R07 | El informe exportado no coincide con lo que muestra el sistema. | Columnas o filtros distintos. | F06 | 2 | 2 |
| R08 | Alguien entra con credenciales incorrectas o por fuerza bruta. | Falta de control en el inicio de sesión. | F01 | 1 | 3 |
| R09 | La sesión sigue activa tras cerrar sesión o cambiar la contraseña. | La sesión no se invalida. | F01 | 1 | 2 |
| R10 | El sistema se vuelve lento con muchos cursos. | Consultas pesadas en el listado o en las métricas. | F03, F05 | 1 | 2 |

**Riesgos del proyecto:**

| ID | Riesgo | P | I |
|---|---|---|---|
| RP1 | No contar con datos de prueba suficientes o representativos. | 2 | 2 |
| RP2 | Tiempo limitado del equipo para ejecutar todas las pruebas. | 2 | 2 |
| RP3 | Cambios en el sistema durante el periodo de pruebas. | 1 | 2 |

### 4.2 Matriz de análisis de riesgos

**Niveles de exposición:** Crítico = 9 · Alto = 6 · Medio = 3-4 · Bajo = 1-2.

| Probabilidad \ Impacto | 1 Bajo | 2 Medio | 3 Alto |
|---|---|---|---|
| **3 Alta** | | | |
| **2 Media** | | R05, R06, R07, RP1, RP2 *(Medio, 4)* | R01, R02, R03, R04 *(Alto, 6)* |
| **1 Baja** | | R09, R10, RP3 *(Bajo, 2)* | R08 *(Medio, 3)* |

| ID | Exposición | Nivel |
|---|---|---|
| R01, R02, R03, R04 | 6 | Alto |
| R05, R06, R07 | 4 | Medio |
| R08 | 3 | Medio |
| R09, R10 | 2 | Bajo |
| RP1, RP2 | 4 | Medio |
| RP3 | 2 | Bajo |

> Ningún riesgo llega a Crítico (9): el sistema es interno y una falla se puede corregir sin pérdidas irreversibles.

### 4.3 Tratamiento y mitigación

| ID | Nivel | Tratamiento | Prioridad |
|---|---|---|---|
| R01 | Alto | **Mitigar con pruebas** (obligatorio). | P1 |
| R02 | Alto | **Mitigar con pruebas** (obligatorio). | P1 |
| R03 | Alto | **Mitigar con pruebas** (obligatorio). | P1 |
| R04 | Alto | **Mitigar con pruebas** (obligatorio). | P1 |
| R05 | Medio | Mitigar con pruebas. | P2 |
| R06 | Medio | Mitigar con pruebas. | P2 |
| R07 | Medio | Mitigar con pruebas. | P2 |
| R08 | Medio | Mitigar con pruebas. | P2 |
| R09 | Bajo | Verificación ligera con lista de chequeo (decisión del Taller 4). | P3 |
| R10 | Bajo | **Aceptado sin pruebas**: no hay entorno de carga y la exposición es baja. | - |
| RP1 | Medio | Preparar un conjunto de datos ficticios versionado en el repositorio (DAT-01). | - |
| RP2 | Medio | Ejecutar primero los P1; si falta tiempo, se recortan los P3. | - |
| RP3 | Bajo | Congelar la versión (commit `77f71b2`) y registrar cualquier cambio. | - |

---

## 5. Estrategia de pruebas y derivación de casos

### 5.1 Derivación de condiciones de prueba

| Condición | Regla verificable | Riesgo |
|---|---|---|
| CP-01 | Un usuario solo modifica el seguimiento de cursos de su propio departamento. | R01 |
| CP-02 | Cada rol accede solo a lo que su permiso le permite; un usuario sin departamento no ve cursos. | R01, R02 |
| CP-03 | Lo registrado queda asociado al curso y a la revisión correctos. | R03 |
| CP-04 | El color del semáforo cambia exactamente en 50 % y 80 %. | R04 |
| CP-05 | La información se conserva al guardar y recargar. | R05 |
| CP-06 | Los totales del panel coinciden con lo registrado. | R06 |
| CP-07 | El informe exportado coincide con la pantalla para el mismo filtro. | R07 |
| CP-08 | Tras 5 intentos fallidos la cuenta se bloquea 300 s. | R08 |
| CP-09 | Una sesión cerrada no se puede reutilizar. | R09 |

### 5.2 Técnicas de diseño de pruebas (ISO/IEC/IEEE 29119-4)

| Técnica | Se aplica a | Por qué |
|---|---|---|
| Tablas de decisión | CP-01, CP-02 | El acceso depende de combinar el rol, la acción y el departamento. |
| Análisis de valores límite | CP-04, CP-08 | Los errores aparecen en los bordes (50 %, 80 %, 5.º intento). |
| Partición de clases de equivalencia | CP-03, CP-05, CP-06, CP-07 | Se agrupan los datos válidos e inválidos y se prueba un representante de cada grupo. |
| Transición de estados | CP-08, CP-09 | La sesión y la cuenta pasan por estados (activa → bloqueada → activa; iniciada → cerrada). |
| Lista de chequeo | CP-09 | El riesgo es bajo y no justifica casos detallados. |

**Tipo de ejecución:** cada caso se ejecuta de forma **manual** (interfaz, con capturas como evidencia) y, cuando aplica, **automática** (pytest contra la API de la copia de demostración).

### 5.3 Generación de casos de prueba y trazabilidad

| Caso | Descripción | Condición | Riesgo | Técnica | Prioridad | Ejecución |
|---|---|---|---|---|---|---|
| TC-01 | El líder de Sistemas Digitales intenta ver las métricas de Producción y modificar un seguimiento; el sistema lo impide en ambos casos. | CP-01 | R01 | Tabla de decisión | P1 | Manual + automática |
| TC-02 | Un usuario de solo consulta ve sin guardar; un líder sin departamento no ve cursos. | CP-02 | R01, R02 | Tabla de decisión | P1 | Manual + automática |
| TC-03 | Seis cursos de la revisión 1 con 80, 77, 50, 47, 100 y 0 % dan verde, amarillo, amarillo, rojo, verde y rojo. | CP-04 | R04 | Valores límite | P1 | Manual + automática |
| TC-07 | Registrar criterios en el curso A, revisión 2, y verificar que no aparecen en otro curso ni revisión. | CP-03 | R03 | Clases de equivalencia | P1 | Manual + automática |
| TC-04 | Los criterios y la observación se conservan al guardar y recargar. | CP-05 | R05 | Clases de equivalencia | P2 | Manual |
| TC-08 | Los totales del panel coinciden con un conteo manual de la muestra. | CP-06 | R06 | Clases de equivalencia | P2 | Manual |
| TC-05 | El Excel filtrado por departamento coincide con la pantalla. | CP-07 | R07 | Clases de equivalencia | P2 | Manual + automática |
| TC-09 | 5 intentos fallidos bloquean; el 6.º con clave correcta se rechaza; tras 300 s se permite. | CP-08 | R08 | Valores límite / estados | P2 | Automática |
| TC-06 | Tras cerrar sesión, "Atrás" del navegador redirige al login. | CP-09 | R09 | Lista de chequeo | P3 | Manual |

> TC-01 a TC-06 vienen del Taller 5. TC-07 a TC-09 se agregan para cubrir R03, R06 y R08, que en el Taller 5 no tenían caso.
>
> Al montar la demo se revisó cómo funciona SIDEM y hubo que ajustar dos casos del Taller 5:
> - **TC-01:** en SIDEM, el rol que se limita por departamento es el líder de departamento, y ese rol no tiene permiso para editar el seguimiento. Los revisores ven todos los departamentos. Por eso el caso ahora prueba al líder de departamento.
> - **TC-03:** el semáforo no cuenta criterios, sino que suma sus pesos. Los datos se rehicieron para caer justo en los límites con los pesos reales (80 % y 50 %, y 77 % y 47 % justo por debajo).

> - **TC-06:** además de la revisión manual en el navegador, se agregó una prueba automática que intenta reutilizar la cookie después de cerrar sesión, porque eso es lo que pide CP-09.

**Procedimientos:**
- **PROC-01 (P1):** TC-01 → TC-02 → TC-03 → TC-07.
- **PROC-02 (P2):** TC-04 → TC-08 → TC-05 → TC-09.
- **PROC-03 (P3):** TC-06.

Cada procedimiento empieza con la base de datos restaurada (DAT-01) y termina cerrando todas las sesiones.

**Casos identificados no ejecutados:** cada integrante propone dos casos adicionales sobre sus riesgos. Quedan registrados en el plan, pero no se ejecutan en esta ronda por el tiempo disponible (RP2): la estrategia basada en riesgos ejecuta primero TC-01 a TC-09. Pueden ejecutarse en una ronda posterior.

| Caso | Integrante | Descripción | Resultado esperado | Riesgo | Técnica | Estado |
|---|---|---|---|---|---|---|
| TC-10 | Sebastián | Dos revisores editan el mismo curso y revisión y guardan casi al mismo tiempo. | El sistema avisa del conflicto o conserva ambos cambios; no se pierde en silencio lo del primero. | R05 | Transición de estados | Identificado - no ejecutado |
| TC-11 | Sebastián | Guardar una observación en el límite de longitud, con tildes, ñ y `<script>alert(1)</script>`. | Se guarda completa en el curso correcto y se muestra como texto, sin ejecutar el script. | R05, R03 | Valores límite | Identificado - no ejecutado |
| TC-12 | Nicolás | Curso sin criterios evaluados (0 de 0) o con criterios "No aplica". | No hay error de división por cero ni sale verde por defecto; se muestra "sin datos" o el color definido. | R04 | Clase de equivalencia inválida | Identificado - no ejecutado |
| TC-13 | Nicolás | Curso con dos docentes o repetido en la revisión; cambiar el filtro de periodo. | El panel cuenta el curso una sola vez y los totales cambian según el filtro. | R06 | Clases de equivalencia | Identificado - no ejecutado |
| TC-14 | Julián | Sesión abierta en dos navegadores; cambiar la contraseña en uno. | La sesión del otro navegador deja de funcionar y pide login. | R09 | Transición de estados | Identificado - no ejecutado |
| TC-15 | Julián | Exportar un curso cuya observación empieza por `=` o `+` (ej. `=HYPERLINK(...)`) y lleva tildes. | En el Excel aparece como texto, no como fórmula; tildes y ñ correctas. | R07 | Clases de equivalencia | Identificado - no ejecutado |
| TC-16 | Marcos | El líder de Sistemas Digitales cambia el ID en la URL o en la API para abrir un curso de Producción. | Respuesta 403 o 404, sin datos de Producción. | R01, R02 | Tabla de decisión | Identificado - no ejecutado |
| TC-17 | Marcos | Un revisor intenta crear un usuario o subirse el rol a admin, desde la pantalla o con petición directa. | La acción se rechaza y el rol no cambia. | R01 | Tabla de decisión | Identificado - no ejecutado |

### 5.4 Requisitos de entorno y datos de prueba

**Entorno AMB-01:**
- SIDEM, commit `77f71b2`, levantado con Docker Compose (API + PostgreSQL) en el equipo del presentador.
- Sin conexión a Moodle ni a la base de producción.
- Navegador Google Chrome actualizado.
- Python 3 + pytest para las pruebas automáticas.

**Datos DAT-01 (ficticios, en `demo/seed_demo.py`):**
- 8 usuarios: superadmin, administrador, dos revisores, líder académico, líder de Sistemas Digitales, líder sin departamento y un usuario de solo consulta.
- 6 cursos: 3 de Sistemas Digitales y 3 de Producción, con docentes ficticios.
- Revisión 1 con sus 6 criterios. Los cumplidos dan 80, 77, 50, 47, 100 y 0 %.
- Revisión 2 en Programación Básica y Bases de Datos, sin criterios cumplidos (para TC-07).
- Base de datos con la zona horaria `America/Bogota`, igual que el servidor de SIDEM.
- Reinicio: `docker compose down -v` y `docker compose up` dejan la base en su estado inicial.

### 5.5 Criterios de suspensión y finalización

**Suspensión:**
- El entorno AMB-01 no levanta o la base no se puede restaurar.
- Aparece un defecto que bloquea el inicio de sesión (impide ejecutar el resto).

**Reanudación:** se corrige la causa, se registra el commit nuevo y se repite el procedimiento afectado.

**Finalización:**

| Módulos | Criterio |
|---|---|
| Críticos (F02, F03, F04) | 100 % de los casos P1 ejecutados; 100 % de las combinaciones de la tabla de decisión y de los valores límite; ningún defecto crítico o alto abierto. |
| Secundarios (F01, F05, F06) | 100 % de los casos diseñados ejecutados; ningún defecto crítico abierto; máximo 2 defectos menores abiertos. |

---

## 6. Actividades de prueba y estimaciones

### 6.1 Desglose de tareas y 6.2 Estimación de esfuerzo

| # | Actividad | Horas |
|---|---|---|
| 1 | Cerrar el plan y validarlo con el docente | 2 |
| 2 | Preparar el entorno de demostración y los datos ficticios (DAT-01) | 5 |
| 3 | Diseño detallado de casos (tablas de decisión, valores límite) | 5 |
| 4 | Automatizar los casos marcados como automáticos (pytest) | 4 |
| 5 | Ejecución del ciclo 1 y reporte de defectos con evidencia | 8 |
| 6 | Regresión y retest de defectos corregidos | 3 |
| 7 | Informe de cierre y preparación de la exposición | 3 |
| | **Total** | **30** (≈ 7,5 h por integrante) |

---

## 7. Personal

### 7.1 Roles y responsabilidades de prueba

El trabajo se reparte **por riesgo y módulo**: cada integrante es dueño de sus casos, los ejecuta, guarda la evidencia y reporta los defectos.

| Integrante | Rol adicional | Riesgos / casos a cargo | Casos identificados (no ejecutados) |
|---|---|---|---|
| Marcos Duque Jaramillo | Líder de pruebas; entorno de demostración | R01, R02 - TC-01, TC-02 | TC-16, TC-17 |
| Sebastián Díaz Jiménez | Automatización (pytest) | R03, R05 - TC-07, TC-04 | TC-10, TC-11 |
| Nicolás Castaño Durango | Datos de prueba (DAT-01) | R04, R06 - TC-03, TC-08 | TC-12, TC-13 |
| Julián Ramírez Molina | Informe de cierre | R07, R08, R09 - TC-05, TC-09, TC-06 | TC-14, TC-15 |

> *Reparto propuesto; el equipo lo confirma en la semana 1.*

---

## 8. Cronograma

### 8.1 Hitos y fechas de ejecución (ciclo de 3 semanas)

| Semana | Fechas | Actividades | Hito |
|---|---|---|---|
| 1 | 09/11 - 14/11 | Revisar el plan con el docente; ajustar; levantar el entorno de demostración y cargar DAT-01. | **H1:** plan aprobado y entorno listo. |
| 2 | 16/11 - 21/11 | Diseño detallado y automatización; ejecución de PROC-01 (P1) y PROC-02 (P2); reporte de defectos. | **H2:** ciclo 1 ejecutado. |
| 3 | 23/11 - 27/11 | Regresión y retest; PROC-03 (P3); informe de cierre; ensayo de la exposición. | **H3:** informe de cierre y exposición (≈ 28/11/2026). |
