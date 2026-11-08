# Registro de defectos

Defectos encontrados al montar la demo y al ejecutar los casos de prueba. Se registra todo lo que no coincide con lo esperado en el plan, aunque en SIDEM haya sido una decisión de diseño, para que sirva en este trabajo y para corregirlo después en SIDEM. Cada uno tiene también su issue en GitHub, creado con la plantilla `.github/ISSUE_TEMPLATE/defecto.md`.

Versión de SIDEM probada: commit `77f71b2`. Entorno: demo con Docker (AMB-01) y datos DAT-01.

| ID | Caso | Riesgo | Severidad | Resumen | Estado |
|---|---|---|---|---|---|
| DEF-01 | TC-02 | R02 | Alta | El líder de departamento sin departamento asignado ve las métricas de toda la institución. | Abierto |
| DEF-02 | TC-06 | R09 | Media | La cookie de sesión sigue sirviendo después de cerrar sesión. | Abierto |
| DEF-03 | TC-09 | R08 | Media | El bloqueo de login depende de la zona horaria de PostgreSQL; con UTC no se activa. | Abierto |
| DEF-04 | TC-02 | R01 | Baja | Un rol personalizado con permiso de ver el seguimiento no ve ningún curso. | Abierto |
| DEF-05 | - | - | Baja | `sql/db.sql` falla al instalar SIDEM en una base nueva. | Abierto |

---

## DEF-01 - Líder sin departamento ve todas las métricas

- **Caso:** TC-02 · **Riesgo:** R02 · **Severidad:** Alta
- **Detectado:** 08/11/2026, corrida automática (`test_tc02_permisos_rol.py::test_lider_sin_departamento_no_ve_metricas`).

**Pasos:**
1. Iniciar sesión como `lider.sindep@sidem.test` (líder de departamento sin departamento).
2. Consultar `GET /dashboard/stats/?periodo=2026-2&revision_numero=1` o abrir **Métricas**.

**Esperado:** no ve ningún curso (`total_cursos = 0`).
**Obtenido:** ve los 6 cursos, de Sistemas Digitales y de Producción.

**Nota del equipo:** en SIDEM este comportamiento se parece al del líder académico, que sí puede ver todo. Aun así se registra como defecto porque contradice la condición CP-02: un usuario sin departamento no debería ver cursos.

**Causa probable:** `get_departamentos_permitidos()` devuelve una lista vacía, y en `services/dashboard_service.py` la condición `if dept_lista:` trata la lista vacía como "sin filtro". La pantalla de Seguimiento sí lo bloquea bien.

**Evidencia:** `evidencias/pytest/ejecucion_2026-11-08.txt`.

## DEF-02 - La sesión cerrada se puede reutilizar

- **Caso:** TC-06 (complemento automático) · **Riesgo:** R09 · **Severidad:** Media
- **Detectado:** 08/11/2026, corrida automática (`test_tc06_sesion_cerrada.py`).

**Pasos:**
1. Iniciar sesión como `consulta@sidem.test` y copiar la cookie `access_token`.
2. Cerrar sesión.
3. Hacer `GET /auth/me` con la cookie copiada.

**Esperado:** 401, la sesión ya no es válida.
**Obtenido:** 200, devuelve los datos del usuario.

**Causa probable:** `logout()` en `routes/auth.py` solo le pide al navegador que borre la cookie. El token sigue siendo válido en el servidor hasta que vence.

**Evidencia:** `evidencias/pytest/ejecucion_2026-11-08.txt`.

## DEF-03 - El bloqueo de login depende de la zona horaria de la base

- **Caso:** TC-09 · **Riesgo:** R08 · **Severidad:** Media
- **Detectado:** 08/11/2026, primera corrida de `test_tc09_bloqueo_login.py`, con la base de la demo en UTC.

**Pasos:**
1. Base PostgreSQL con zona horaria UTC (la que trae la imagen oficial de Docker).
2. Hacer 5 intentos fallidos con `revisor.pr@sidem.test`.
3. Intentar entrar con la contraseña correcta.

**Esperado:** 429, cuenta bloqueada 300 s.
**Obtenido:** 200, entra sin bloqueo.

**Causa probable:** la columna `log_actividad.fecha` tiene como valor por defecto `CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'`. Eso da una hora sin zona que PostgreSQL vuelve a interpretar con su propia zona. Con UTC queda 5 horas atrás y el conteo de intentos de los últimos 300 s siempre da 0.

**Nota:** con la base en `America/Bogota` el bloqueo funciona y TC-09 pasa. El defecto aparece solo si la base de producción no está en esa zona, así que falta confirmarlo allí.

**Evidencia:** `evidencias/pytest/ejecucion_2026-11-08.txt` (corrida con la base corregida) y los registros de `log_actividad` de la primera corrida, con fecha 14:08 cuando en UTC eran las 19:08.

## DEF-04 - Rol personalizado con permiso de ver no ve cursos

- **Caso:** TC-02 · **Riesgo:** R01 · **Severidad:** Baja
- **Detectado:** 08/11/2026, corrida automática (`test_tc02_permisos_rol.py::test_consulta_puede_ver_el_seguimiento`).

**Pasos:**
1. Iniciar sesión como `consulta@sidem.test` (rol personalizado con seguimiento en "vista").
2. Abrir **Seguimiento**, revisión 1.

**Esperado:** ve los 6 cursos, sin poder guardar.
**Obtenido:** no ve ningún curso. La parte de "no puede guardar" sí funciona.

**Causa probable:** `get_departamentos_permitidos()` en `services/auth_service.py` solo reconoce los roles de siempre (superadmin, admin, revisor, lider y lider_departamento). Cualquier otro rol recibe una lista vacía de departamentos, aunque en la matriz de permisos tenga acceso al módulo.

**Evidencia:** `evidencias/pytest/ejecucion_2026-11-08.txt`.

## DEF-05 - El esquema oficial falla en una base nueva

- **Caso:** ninguno (apareció al montar la demo) · **Severidad:** Baja
- **Detectado:** 08/11/2026, al crear la base de la demo.

**Pasos:**
1. Crear una base PostgreSQL vacía.
2. Ejecutar `sql/db.sql` completo, deteniéndose en el primer error.

**Esperado:** el esquema se crea completo.
**Obtenido:** `ERROR: column "estado_seguimiento" does not exist`, en la migración de `seguimientos_estudiantes` (línea 593 aprox.).

**Causa probable:** la migración supone que la columna ya existe de una versión anterior. En una instalación nueva no está.

**Nota:** el módulo de estudiantes está fuera del alcance, pero el error afecta a cualquiera que instale SIDEM desde cero. La demo lo rodea cargando el archivo sin detenerse y completando con `verificar_schema.py --aplicar`.
