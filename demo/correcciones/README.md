# Correcciones de los defectos (sobre el commit 77f71b2)

Cada archivo `.patch` corrige un defecto de `docs/defectos.md` sobre la versión de SIDEM que se probó (`77f71b2`). Los cambios se ven completos en cada archivo: qué líneas se quitan (`-`) y cuáles se agregan (`+`), junto con la prueba automática que demuestra la corrección.

| Parche | Defecto | Qué se cambió | Prueba nueva |
|---|---|---|---|
| `0001-...` | DEF-01 (alta) | En `services/dashboard_service.py`, `if dept_lista:` pasa a `if dept_lista is not None:`. La lista vacía significa "ningún departamento", no "todos". | `test_lista_vacia_de_departamentos_no_ve_ningun_curso` |
| `0002-...` | DEF-04 | `get_departamentos_permitidos()` deja de devolver una lista vacía a los roles personalizados. **Pendiente de ajuste** (ver abajo). | `test_rol_personalizado_ve_departamentos_segun_asignacion` |
| `0003-...` | DEF-02 | `logout()` invalida el token en el servidor con `password_changed_at`, el mismo mecanismo de "forzar logout". Cierra todas las sesiones del usuario. | `TestLogout` en `test_auth.py` |
| `0004-...` | DEF-03 | La fecha de `log_actividad` la pone la aplicación en UTC, no la base. `db.sql` sin `AT TIME ZONE`. | `test_log_service.py` |
| `0005-...` | DEF-05 | En `db.sql`, el backfill de `estado_seguimiento` solo corre si la columna vieja existe. | Se instaló `db.sql` en un PostgreSQL vacío: antes fallaba en la línea 597, ahora termina sin errores. |

Con los 5 parches aplicados pasan las 647 pruebas automáticas de SIDEM.

## Pendiente: sugerencia de Nicolás (issues #1 y #4)

El equipo prefiere que el alcance sea explícito: al crear o editar un usuario, el departamento es obligatorio y existe la opción **"Todos"**. Un rol personalizado o un líder sin departamento asignado no ve ningún curso. El parche `0002` se ajustará cuando Julián y Sebastián den su opinión en los issues.

## Cómo se usan

Los aplica el líder al reconstruir las imágenes de la demo (ver `demo/README.md`):

```
git am demo/correcciones/*.patch
```
