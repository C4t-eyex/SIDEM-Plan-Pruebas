# Evidencias (fase 3)

Convención de nombres: `TC-XX_AAAA-MM-DD_<integrante>.png`. Si un caso tiene varias capturas, se agrega al final el paso o la vista (`_paso1-...`, `_SD`, `_PR`). Los reportes de pytest se guardan en `evidencias/pytest/`.

## Índice por caso

| Caso | Quién | Resultado manual | Archivos |
|---|---|---|---|
| TC-01 | Marcos | Pasa (4 de 4) | `TC-01_2026-11-12_Marcos_paso1-solo-SD.png`, `_paso2-forzar-PR.png`, `_paso3-sin-seguimiento.png`, `_paso4-logistica-admin.png` |
| TC-02 | Marcos | Falla (DEF-01 y DEF-04) | `TC-02_2026-11-12_Marcos_paso1-consulta-sin-cursos.png`, `_paso3-sindep-ve-todo.png`. Captura previa del 08/11: `TC-02_2026-11-08_Marcos.jpg` |
| TC-03 | Nicolás | Pasa (7 de 7) | `TC-03_2026-11-12_Nicolas.png` |
| TC-04 | Sebastián | Pendiente | - |
| TC-05 | Julián | Pasa | `TC-05_2026-11-12_Julian_pantalla-SD.png`, `_pantalla-PR.png`, `_dialogo-SD.png`, `_SD.xlsx`, `_PR.xlsx` |
| TC-06 | Julián | Pasa (parte del navegador) | `TC-06_2026-11-12_Julian_paso1-con-sesion.png` a `_paso4-recarga.png` |
| TC-07 | Sebastián | Pendiente | - |
| TC-08 | Nicolás | Pasa (3 de 3) | `TC-08_2026-11-12_Nicolas_todos.png`, `_SD.png`, `_PR.png` |
| TC-09 | Julián (revisión) | Pasa en pytest | `pytest/ejecucion_2026-11-08.txt`, `pytest/ejecucion_2026-11-12_Sebastian.txt` |

## Corridas de pytest

| Archivo | Quién | Resultado |
|---|---|---|
| `pytest/ejecucion_2026-11-08.txt` y `.xml` | Equipo | 19 pruebas: 16 pasan, 3 fallan (DEF-01, DEF-02, DEF-04) |
| `pytest/ejecucion_2026-11-12_Sebastian.txt` y `.xml` | Sebastián | 19 pruebas: 16 pasan, 3 fallan (los mismos) |
