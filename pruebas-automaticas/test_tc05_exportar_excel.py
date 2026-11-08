"""
TC-05 · Riesgo R07 · Condición CP-07 · Técnica: clases de equivalencia.

El Excel exportado con el filtro de un departamento debe tener los mismos
cursos y los mismos resultados de la revisión 1 que la pantalla de Seguimiento.
"""
from io import BytesIO

import pytest
from openpyxl import load_workbook

from conftest import PERIODO, cursos_revision

# Distribución de la plantilla de SIDEM (routes/exports.py y criterios_config.REVISION_COLS)
FILA_INICIO = 4
COL_DEPARTAMENTO = 5
COL_CURSO = 7
COLS_REVISION_1 = [10, 11, 12, 13, 14, 15]


def leer_excel(contenido: bytes) -> dict:
    hoja = load_workbook(BytesIO(contenido)).active
    filas = {}
    for fila in range(FILA_INICIO, hoja.max_row + 1):
        curso = hoja.cell(row=fila, column=COL_CURSO).value
        if not curso:
            continue
        filas[curso] = {
            "departamento": hoja.cell(row=fila, column=COL_DEPARTAMENTO).value,
            "revision_1": [hoja.cell(row=fila, column=c).value for c in COLS_REVISION_1],
        }
    return filas


@pytest.mark.parametrize("departamento", ["Sistemas Digitales", "Producción"])
def test_excel_coincide_con_pantalla(sesion, departamento):
    revisor = sesion("revisor.sd@sidem.test")
    r = revisor.get("/exportar-excel/", params={"periodo": PERIODO, "departamento": departamento})
    assert r.status_code == 200, r.text
    excel = leer_excel(r.content)

    pantalla = cursos_revision(revisor, 1, departamento=departamento)
    assert set(excel) == {c["nombre_curso"] for c in pantalla}
    for curso in pantalla:
        fila = excel[curso["nombre_curso"]]
        assert fila["departamento"] == departamento
        assert fila["revision_1"] == ["SI" if k["cumplido"] else "NO" for k in curso["criterios"]]
