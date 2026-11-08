"""
TC-01 · Riesgo R01 · Condición CP-01 · Técnica: tabla de decisión.

El líder de Sistemas Digitales no debe ver las métricas de Producción
ni modificar un seguimiento.
"""
from conftest import PERIODO, cursos_revision


def test_lider_ve_solo_su_departamento(sesion):
    lider = sesion("lider.sd@sidem.test")
    r = lider.get("/dashboard/stats/", params={"periodo": PERIODO, "revision_numero": 1})
    assert r.status_code == 200
    departamentos = {c["departamento"] for c in r.json()["docentes"]}
    assert departamentos == {"Sistemas Digitales"}


def test_lider_no_puede_pedir_metricas_de_otro_departamento(sesion):
    lider = sesion("lider.sd@sidem.test")
    r = lider.get("/dashboard/stats/",
                  params={"periodo": PERIODO, "revision_numero": 1, "departamento": "Producción"})
    assert r.status_code == 403


def test_lider_no_puede_modificar_seguimiento(sesion):
    admin = sesion("admin@sidem.test")
    curso = next(c for c in cursos_revision(admin, 1) if c["departamento"] == "Producción")
    antes = {k["criterio_id"]: k["cumplido"] for k in curso["criterios"]}

    lider = sesion("lider.sd@sidem.test")
    cambio = {"criterios": [{"criterio_id": 1, "cumplido": not antes[1], "observaciones": "TC-01"}]}
    r = lider.put(f"/revisiones/actualizar_criterios/{curso['curso_id']}/1", json=cambio)
    assert r.status_code == 403

    # El administrador confirma que el dato no cambió
    despues = next(c for c in cursos_revision(admin, 1) if c["curso_id"] == curso["curso_id"])
    assert {k["criterio_id"]: k["cumplido"] for k in despues["criterios"]} == antes
