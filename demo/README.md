# Demo de SIDEM con datos ficticios

Esta carpeta levanta una copia de SIDEM para hacer las pruebas y mostrarlas en clase. Usa la versión fijada en el plan (commit `77f71b2`) y una base de datos propia con datos inventados. No se conecta a Moodle ni a la base de producción.

Cada integrante puede montarla en su propio equipo y ejecutar sus casos sin afectar a los demás.

## Qué se necesita

- Docker Desktop encendido.
- Acceso a este repositorio (`SIDEM-Plan-Pruebas`) y a la carpeta de Drive del equipo. No hace falta el código de SIDEM: la aplicación y la base vienen en dos imágenes de Docker ya armadas (`sidem-demo-app:77f71b2` y `sidem-demo-db:77f71b2`), guardadas en un solo archivo.

## Cómo levantarla

**Solo la primera vez**, carga las imágenes en Docker:

1. Descarga `sidem-demo-imagenes-77f71b2.tar.gz` (unos 253 MB) desde la carpeta de Drive del equipo: https://drive.google.com/drive/folders/1i7nXTlf7k8DhToZPXx2Hm70bDSp-vvhp?usp=sharing. El acceso es solo para los integrantes; si no te deja entrar, pídele acceso a Marcos.
2. Con Docker Desktop abierto, en la carpeta donde quedó el archivo:

   ```powershell
   docker load -i sidem-demo-imagenes-77f71b2.tar.gz
   ```

   Debe terminar con `Loaded image: sidem-demo-app:77f71b2` y `Loaded image: sidem-demo-db:77f71b2`. Después puedes borrar el archivo.

**Para arrancar**, desde esta carpeta (`demo/`):

```powershell
docker compose up -d
```

Cuando termine (menos de un minuto), abre http://localhost:8090.

Si aparece `pull access denied` o `repository does not exist`, es que falta el paso de `docker load`.

## Usuarios de prueba

Todos usan la misma contraseña de demo: `Demo-SIDEM-2026` (se puede cambiar con la variable `DEMO_PASSWORD`).

| Correo | Rol | Para qué caso sirve |
|---|---|---|
| `superadmin@sidem.test` | superadmin | Configuración general |
| `admin@sidem.test` | admin | Revisar que los datos no cambiaron (TC-01) |
| `revisor.sd@sidem.test` | revisor (encargado de Sistemas Digitales) | Registro del seguimiento (TC-04, TC-07) |
| `revisor.pr@sidem.test` | revisor (encargado de Producción) | Registro del seguimiento |
| `lider@sidem.test` | líder académico | Métricas y semáforo (TC-03, TC-08) |
| `lider.sd@sidem.test` | líder de departamento, Sistemas Digitales | Alcance por departamento (TC-01) |
| `lider.sindep@sidem.test` | líder de departamento, sin departamento | Usuario sin departamento (TC-02) |
| `consulta@sidem.test` | consulta (rol creado para la demo) | Ver sin poder guardar (TC-02) |

## Cursos de prueba (revisión 1, periodo actual)

En la revisión 1 hay 6 criterios con pesos 5, 5, 7, 5, 6 y 2, que suman 30. El porcentaje es el peso cumplido sobre 30.

| Curso | Departamento | % | Color esperado |
|---|---|---|---|
| Programación Básica (DEMO) | Sistemas Digitales | 80 | Verde (justo en el límite) |
| Bases de Datos (DEMO) | Sistemas Digitales | 77 | Amarillo (justo debajo de 80) |
| Redes I (DEMO) | Sistemas Digitales | 50 | Amarillo (justo en el límite) |
| Procesos Industriales (DEMO) | Producción | 47 | Rojo (justo debajo de 50) |
| Calidad (DEMO) | Producción | 100 | Verde |
| Logística (DEMO) | Producción | 0 | Rojo |

## Volver al estado inicial

Antes de cada procedimiento (PROC-01, 02 y 03) conviene dejar la base como al principio:

```powershell
docker compose down -v
docker compose up -d
```

`down -v` borra solo la base de esta demo (el volumen `sidem-demo-datos`). No toca otros contenedores.

## Para apagarla

```powershell
docker compose down
```

## Archivos

| Archivo | Qué hace |
|---|---|
| `docker-compose.yml` | Define la base de datos y la aplicación usando las imágenes ya armadas. |
| `docker-compose.build.yml` | Solo para el líder: reconstruye las imágenes (ver abajo). |
| `preparar-demo.ps1` / `.sh` | Solo para el líder: descarga SIDEM en el commit `77f71b2` dentro de `demo/sidem/` (esa carpeta no se sube al repositorio). |
| `Dockerfile` | Arma la imagen de la aplicación con el código de SIDEM. |
| `Dockerfile.db` | Arma la imagen de la base con el esquema oficial de SIDEM. |
| `init-db.sh` | Carga el esquema oficial de SIDEM (`sql/db.sql`) al crear la base. |
| `entrypoint.sh` | Completa el esquema, carga los datos ficticios y arranca SIDEM. |
| `seed_demo.py` | Crea los usuarios, cursos y resultados de prueba (DAT-01). |

## Reconstruir las imágenes (solo el líder)

Requiere acceso al repositorio privado de SIDEM. Arma las imágenes, las guarda en el archivo comprimido y luego se sube ese archivo a la carpeta de Drive:

```powershell
.\preparar-demo.ps1
docker compose -f docker-compose.yml -f docker-compose.build.yml build
docker save sidem-demo-app:77f71b2 sidem-demo-db:77f71b2 | gzip > sidem-demo-imagenes-77f71b2.tar.gz   # en Git Bash
```

El archivo no va al repositorio: pesa más de los 100 MB que permite GitHub y contiene el código de SIDEM.

## Nota sobre el esquema

En una base nueva, `sql/db.sql` falla en la migración de `seguimientos_estudiantes`, porque usa una columna que todavía no existe. Ese módulo está fuera del alcance, así que `init-db.sh` carga el archivo sin detenerse y luego `verificar_schema.py --aplicar` completa lo que falte. Quedó anotado como hallazgo HAL-01 en `docs/avances.md`.
