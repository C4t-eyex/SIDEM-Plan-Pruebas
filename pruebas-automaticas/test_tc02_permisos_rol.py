"""
TC-02 · Riesgos R01 y R02 · Condición CP-02 · Técnica: tabla de decisión.

Un usuario de solo consulta ve el seguimiento pero no puede guardar.
Un líder de departamento sin departamento asignado no debe ver cursos.
"""
from conftest import PERIODO, cursos_revision


def test_consulta_puede_ver_el_seguimiento(sesion):
    consulta = sesion("consulta@sidem.test")
    cursos = cursos_revision(consulta, 1)
    assert len(cursos) == 6, f"El usuario de consulta ve {len(cursos)} cursos"


def test_consulta_no_puede_guardar(sesion):
    curso = cursos_revision(sesion("admin@sidem.test"), 1)[0]
    consulta = sesion("consulta@sidem.test")
    cambio = {"criterios": [{"criterio_id": 1, "cumplido": True, "observaciones": "TC-02"}]}
    r = consulta.put(f"/revisiones/actualizar_criterios/{curso['curso_id']}/1", json=cambio)
    assert r.status_code == 403


def test_lider_sin_departamento_no_ve_seguimiento(sesion):
    lider = sesion("lider.sindep@sidem.test")
    r = lider.get("/revisiones/obtener_revisiones/",
                  params={"revision_numero": 1, "periodo": PERIODO})
    assert r.status_code == 403


def test_lider_sin_departamento_no_ve_metricas(sesion):
    lider = sesion("lider.sindep@sidem.test")
    r = lider.get("/dashboard/stats/", params={"periodo": PERIODO, "revision_numero": 1})
    assert r.status_code == 200
    datos = r.json()
    assert datos["total_cursos"] == 0, (
        f"Ve {datos['total_cursos']} cursos de "
        f"{sorted({c['departamento'] for c in datos['docentes']})}"
    )
