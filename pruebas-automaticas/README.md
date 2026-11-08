# Pruebas automáticas

Pruebas con pytest que se ejecutan contra la demo de SIDEM (`demo/`) por HTTP, igual que el navegador: inician sesión con los usuarios ficticios y consultan la API.

## Cómo correrlas

```powershell
# 1. Demo arriba y en su estado inicial (desde demo/)
docker compose down -v
docker compose up -d

# 2. Dependencias (solo la primera vez, desde pruebas-automaticas/)
pip install -r requirements.txt

# 3. Todas las pruebas (unos 7 minutos, por la espera de TC-09)
python -m pytest --junitxml=..\evidencias\pytest\ejecucion_AAAA-MM-DD.xml

# Sin TC-09 (menos de 1 minuto)
python -m pytest -m "not lento"
```

TC-09 bloquea durante 5 minutos la IP de quien lo corre, así que va de último. Para repetirlo hay que esperar ese tiempo o reiniciar la demo.

## Qué cubre cada archivo

| Archivo | Caso | Riesgo | Qué revisa |
|---|---|---|---|
| `test_tc01_alcance_departamento.py` | TC-01 | R01 | El líder de Sistemas Digitales solo ve su departamento, no puede pedir Producción y no puede modificar un seguimiento. |
| `test_tc02_permisos_rol.py` | TC-02 | R01, R02 | El usuario de consulta ve sin guardar; el líder sin departamento no ve cursos. |
| `test_tc03_semaforo_limites.py` | TC-03 | R04 | Porcentaje y color de los 6 cursos (80, 77, 50, 47, 100 y 0 %) y el resumen del panel. |
| `test_tc05_exportar_excel.py` | TC-05 | R07 | El Excel filtrado por departamento tiene los mismos cursos y los mismos SI/NO que la pantalla. |
| `test_tc06_sesion_cerrada.py` | TC-06 (complemento) | R09 | Una cookie copiada antes de cerrar sesión ya no debería servir. |
| `test_tc07_criterios_revision.py` | TC-07 | R03 | Lo registrado en el curso A, revisión 2, no aparece en el curso B ni en la revisión 1. Al final deja el curso como estaba. |
| `test_tc09_bloqueo_login.py` | TC-09 | R08 | 5 fallos bloquean, el 6.º con la clave correcta se rechaza y a los 300 s se permite. |

TC-04, TC-08 y la parte de pantalla de los demás casos son manuales (`docs/ejecucion-manual.md`).

## Resultados

La salida de cada corrida se guarda en `evidencias/pytest/` (texto y XML). El resumen y los hallazgos quedan en `docs/avances.md` y `docs/defectos.md`.
