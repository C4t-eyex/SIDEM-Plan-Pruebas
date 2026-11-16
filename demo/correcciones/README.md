# Correcciones de los defectos (sobre el commit 77f71b2)

Cada archivo `.patch` corrige un defecto de `docs/defectos.md` sobre la versión de SIDEM que se probó (`77f71b2`). Los cambios se ven completos en cada archivo: qué líneas se quitan (`-`) y cuáles se agregan (`+`), junto con la prueba automática que demuestra la corrección.

| Parche | Defecto | Qué se cambió | Prueba nueva |
|---|---|---|---|
| `0001-...` | DEF-01 (alta) | En `services/dashboard_service.py`, `if dept_lista:` pasa a `if dept_lista is not None:`. La lista vacía significa "ningún departamento", no "todos". | `test_lista_vacia_de_departamentos_no_ve_ningun_curso` |
| `0002-...` | DEF-04 (y DEF-01) | Alcance explícito, como acordó el equipo en los issues #1 y #4. El líder de departamento y los roles personalizados se limitan por el departamento asignado: con **"Todos"** ven todos, con departamentos solo esos y sin ninguno asignado no ven ningún curso. Al crear o editar el usuario el departamento es obligatorio para esos roles, y el formulario de usuarios ofrece la opción "Todos". | `test_rol_personalizado_ve_departamentos_segun_asignacion`, `test_crear_rol_personalizado_exige_departamento_o_todos`, `test_actualizar_a_rol_personalizado_sin_departamento_se_rechaza` |
| `0003-...` | DEF-02 | `logout()` invalida el token en el servidor con `password_changed_at`, el mismo mecanismo de "forzar logout". Cierra todas las sesiones del usuario. | `TestLogout` en `test_auth.py` |
| `0004-...` | DEF-03 | La fecha de `log_actividad` la pone la aplicación en UTC, no la base. `db.sql` sin `AT TIME ZONE`. | `test_log_service.py` |
| `0005-...` | DEF-05 | En `db.sql`, el backfill de `estado_seguimiento` solo corre si la columna vieja existe. | Se instaló `db.sql` en un PostgreSQL vacío: antes fallaba en la línea 597, ahora termina sin errores. |

Con los 5 parches aplicados pasan las 649 pruebas automáticas de SIDEM.

En la demo, `seed_demo.py` le asigna "Todos" a `consulta@sidem.test`, para que TC-02 pruebe un rol personalizado que debe ver el seguimiento completo. `lider.sindep@sidem.test` sigue sin departamento para probar que no ve nada. El seed solo crea los usuarios que faltan, así que hay que partir de una base nueva.

## Cómo se usan

Los aplica el líder al reconstruir las imágenes de la demo (ver `demo/README.md`):

```
git am demo/correcciones/*.patch
```
