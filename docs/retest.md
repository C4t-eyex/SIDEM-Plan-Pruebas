# Retest de los defectos corregidos

Guía para repetir las pruebas sobre SIDEM con las correcciones de DEF-01 a DEF-05. Lo ejecuta **Sebastián**; con el resultado, **Julián** actualiza el informe de cierre.

> **Hecho el 16/11/2026 por Sebastián:** 19 de 19 pruebas pasan y los 5 defectos quedan cerrados. Detalle en [`defectos.md`](defectos.md) y en `evidencias/pytest/ejecucion_2026-11-16_retest_Sebastian.txt`. Falta que Julián comente los issues #1 a #5 y actualice el informe de cierre.

## Qué cambió

- **Versión probada:** commit `77f71b2` más los parches `0001` a `0005` de [`demo/correcciones/`](../demo/correcciones/). Las imágenes de Docker se llaman `sidem-demo-app:77f71b2-correcciones` y `sidem-demo-db:77f71b2-correcciones`.
- **Base de datos en UTC.** En la primera ronda estaba en `America/Bogota` para que TC-09 pasara. Ahora queda en UTC para comprobar que DEF-03 está corregido.
- **Usuario `consulta@sidem.test`** con alcance "Todos" (DEF-04). `lider.sindep@sidem.test` sigue sin departamento (DEF-01).

| Defecto | Caso que lo comprueba | Resultado esperado en el retest |
|---|---|---|
| DEF-01 | TC-02 (`test_lider_sin_departamento_no_ve_metricas`) | El líder sin departamento ve 0 cursos. |
| DEF-02 | TC-06 (`test_sesion_cerrada_no_se_reutiliza`) | La cookie copiada antes de cerrar sesión da 401. |
| DEF-03 | TC-09 (`test_bloqueo_y_desbloqueo`) | El bloqueo funciona con la base en UTC. |
| DEF-04 | TC-02 (`test_consulta_puede_ver_el_seguimiento`) | El usuario de consulta ve los 6 cursos. |
| DEF-05 | Log de la base al crearla | `db.sql` termina sin líneas `ERROR`. |

## Pasos

1. **Descargar las imágenes.** Baja `sidem-demo-imagenes-77f71b2-correcciones.tar.gz` (unos 264 MB) de la [carpeta de Drive del equipo](https://drive.google.com/drive/folders/1i7nXTlf7k8DhToZPXx2Hm70bDSp-vvhp?usp=drive_link) (ya está subido) y cárgalo:

   ```powershell
   docker load -i sidem-demo-imagenes-77f71b2-correcciones.tar.gz
   ```

   Debe terminar con `Loaded image: sidem-demo-app:77f71b2-correcciones` y `Loaded image: sidem-demo-db:77f71b2-correcciones`.

2. **Actualizar el repositorio y levantar la demo desde cero** (desde `demo/`). El `down -v` borra la base de la demo anterior; es necesario porque el seed solo crea los usuarios que faltan.

   ```powershell
   git pull
   docker compose down -v
   docker compose up -d
   ```

3. **Comprobar DEF-05.** Debe responder `0`:

   ```powershell
   docker logs sidem-demo-db 2>&1 | Select-String "ERROR:" | Measure-Object | Select-Object -ExpandProperty Count
   ```

   Si quieres revisar la zona horaria: `docker exec sidem-demo-db psql -U sidem -d seguimiento_docentes -tAc "show timezone"` debe decir `UTC`.

4. **Correr las pruebas automáticas** (desde `pruebas-automaticas/`, unos 7 minutos):

   ```powershell
   python -m pytest -rA --junitxml=..\evidencias\pytest\ejecucion_AAAA-MM-DD_retest_Sebastian.xml | Tee-Object ..\evidencias\pytest\ejecucion_AAAA-MM-DD_retest_Sebastian.txt
   ```

   Resultado esperado: **19 pasan, 0 fallan**. En la primera ronda fallaban 3 (TC-02 ×2 por DEF-01 y DEF-04, y TC-06 por DEF-02).

5. **Repetir a mano lo que quieras mostrar** (opcional), con la hoja de [`ejecucion-manual.md`](ejecucion-manual.md). Por ejemplo, `lider.sindep@sidem.test` en Métricas debe ver "Sin datos".

## Qué registrar después

| Quién | Dónde | Qué |
|---|---|---|
| Sebastián | `evidencias/pytest/` | Los archivos `.txt` y `.xml` del paso 4. |
| Sebastián | [`defectos.md`](defectos.md) | Estado de cada defecto: "Cerrado (retest DD/11)" si pasa, o "Reabierto" con lo que se vio. |
| Sebastián | Issues #1 a #5 en GitHub | Comentario con el resultado; cerrar el issue si pasa. |
| Sebastián | [`avances.md`](avances.md) | Una fila con la corrida. |
| Julián | [`informe-de-cierre.md`](informe-de-cierre.md) | Sección de retest, estado final de los defectos y criterios de finalización. |

## Verificación previa

El 16/11/2026 Marcos armó las imágenes y las probó en una base nueva: `db.sql` cargó sin errores, la base quedó en UTC y las 19 pruebas pasaron. Esa corrida no reemplaza el retest; sirve para saber que la imagen está bien antes de entregarla.
