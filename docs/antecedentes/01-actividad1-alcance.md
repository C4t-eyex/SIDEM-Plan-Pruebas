> **Antecedente:** Actividad 1 del curso (septiembre 2026). Se conserva como se entregó. Los ajustes posteriores están en `../plan-de-pruebas.md`.

# Plan de Pruebas - SIDEM

## 1. Identificacion del sistema

**Nombre del sistema:** SIDEM (Sistema de Seguimiento de Docentes en Moodle)

**Descripcion breve:** Aplicacion web (FastAPI + PostgreSQL, con lectura sobre la base de datos de Moodle) que permite a coordinadores academicos verificar el cumplimiento de criterios de acompanamiento docente (foros, Google Meet, grabaciones, tiempos de respuesta, tareas, agenda, grupos colaborativos) en cursos de Moodle, mostrando un tablero con semaforo (verde/amarillo/rojo) por curso y por periodo de revision.

## 2. Metodologia de desarrollo

**Enfoque:** Agil (iterativo e incremental, tipo Kanban), no tradicional por fases.

**Justificacion:** El historial de control de versiones muestra entregas pequenas y frecuentes por funcionalidad (por ejemplo: nombre de marca configurable, paginacion del registro de mensajeria, exportacion por departamento, permisos por encargado), cada una probada y desplegada de forma independiente en vez de agruparse en fases secuenciales de analisis-diseno-construccion-pruebas. No existe una fase unica de "requisitos cerrados" ni entregas por hitos largos; el sistema crece por incrementos funcionales priorizados segun necesidad, lo cual corresponde a un ciclo agil de iteraciones cortas con retroalimentacion continua.

## 3. Titulo y objetivo general

**Titulo de la propuesta:** Plan de pruebas de software para el modulo de Seguimiento y Metricas del sistema SIDEM

**Preguntas guia:**
- El sistema funciona correctamente para lo que fue disenado?
- Que partes del sistema son mas importantes de probar?
- Que puede fallar y que tan grave seria?
- El sistema es facil de usar para quien lo revise?

**Que se va a probar y evaluar:** El modulo de seguimiento docente (evaluacion de criterios por curso y periodo de revision), el calculo y visualizacion de metricas/semaforo en el dashboard, y el modulo de gestion de usuarios (creacion, roles, permisos).

**Por que se realizan las pruebas:** Para verificar que el sistema evalua correctamente el cumplimiento de los criterios institucionales, que las metricas mostradas al usuario son confiables para la toma de decisiones academicas, y que el control de acceso por rol funciona sin fugas de informacion entre departamentos.

**Modulo/version que abarca:** Version de pruebas del sistema (rama `main` actual), limitada a los modulos de Seguimiento, Metricas/Dashboard y Gestion de usuarios.

**Objetivo general:** Elaborar y ejecutar un plan de pruebas que permita validar la correccion funcional, la seguridad de acceso por roles y la confiabilidad de las metricas del modulo de Seguimiento de SIDEM, mediante la participacion de companeros como revisores en una version habilitada para pruebas.

## 4. Alcance preliminar

### 4.1 Elementos incluidos (modulos y funcionalidades)
- Modulo de Seguimiento docente: visualizacion de cursos, criterios por revision (semanas 2, 6, 11 y 15), estados y observaciones.
- Modulo de Metricas / Dashboard: calculo del semaforo (verde/amarillo/rojo) por curso y por revision.
- Modulo de Gestion de usuarios: creacion de usuarios, asignacion de roles (admin, revisor, lider, lider_departamento), autenticacion (login/logout).

### 4.2 Elementos excluidos y razon
- **Seguimiento a estudiantes:** el sistema esta orientado exclusivamente al seguimiento de docentes, no existe modulo de seguimiento a estudiantes.
- **Actividad directa en Moodle:** las pruebas no cubren la plataforma Moodle en si (creacion de cursos, foros, tareas dentro de Moodle), solo la lectura/verificacion que SIDEM hace sobre esos datos.
- **Modulo de importacion (carga de Excel):** queda fuera del alcance de esta ronda de pruebas porque depende de un servidor en ejecucion autoconsumiendo sus propios endpoints (patron self-calling HTTP) y de archivos externos, lo que lo hace mas complejo de habilitar para una version de pruebas con companeros; se probara en una fase posterior.

Por ahora, el alcance queda limitado a: **Seguimiento**, **Metricas/Dashboard** y **Gestion de usuarios**.
