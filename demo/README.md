# Demo de SIDEM con datos ficticios

Esta carpeta levanta una copia de SIDEM para hacer las pruebas y mostrarlas en clase. Usa la versión fijada en el plan (commit `77f71b2`) y una base de datos propia con datos inventados. No se conecta a Moodle ni a la base de producción.

Cada integrante puede montarla en su propio equipo y ejecutar sus casos sin afectar a los demás.

## Qué se necesita

- Docker Desktop encendido.
- Git.
- Acceso al repositorio privado de SIDEM. Si no lo tienes, pídele a Marcos que te agregue.

## Cómo levantarla

Desde esta carpeta (`demo/`):

```powershell
# 1. Descarga SIDEM en la versión de las pruebas (solo la primera vez)
.\preparar-demo.ps1          # en Linux/Mac: sh preparar-demo.sh

# 2. Construye y arranca
docker compose up --build -d
```

Cuando termine, abre http://localhost:8090. La primera vez tarda unos minutos porque descarga las imágenes e instala las dependencias.

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
| `preparar-demo.ps1` / `.sh` | Descarga SIDEM en el commit `77f71b2` dentro de `demo/sidem/` (esa carpeta no se sube al repositorio). |
| `docker-compose.yml` | Define la base de datos y la aplicación. |
| `Dockerfile` | Arma la imagen de SIDEM. |
| `init-db.sh` | Carga el esquema oficial de SIDEM (`sql/db.sql`) al crear la base. |
| `entrypoint.sh` | Completa el esquema, carga los datos ficticios y arranca SIDEM. |
| `seed_demo.py` | Crea los usuarios, cursos y resultados de prueba (DAT-01). |

## Nota sobre el esquema

En una base nueva, `sql/db.sql` falla en la migración de `seguimientos_estudiantes`, porque usa una columna que todavía no existe. Ese módulo está fuera del alcance, así que `init-db.sh` carga el archivo sin detenerse y luego `verificar_schema.py --aplicar` completa lo que falte. Quedó anotado como hallazgo HAL-01 en `docs/avances.md`.
