"""
TC-07 · Riesgo R03 · Condición CP-03 · Técnica: clases de equivalencia.

Lo que se registra en el curso A, revisión 2, queda solo ahí: no aparece en
el curso B (misma revisión) ni en la revisión 1 del curso A.
Al final se deja el curso A como estaba para poder repetir la prueba.
"""
import pytest

from conftest import cursos_revision

CURSO_A = "Programación Básica (DEMO)"
CURSO_B = "Bases de Datos (DEMO)"
MARCAS = {19: "TC-07 criterio 19", 20: "TC-07 criterio 20"}


def criterios(cliente, revision, nombre):
    curso = next(c for c in cursos_revision(cliente, revision) if c["nombre_curso"] == nombre)
    return curso["curso_id"], {k["criterio_id"]: (k["cumplido"], k["observaciones"]) for k in curso["criterios"]}


@pytest.fixture
def revisor(sesion):
    cliente = sesion("revisor.sd@sidem.test")
    id_a, original = criterios(cliente, 2, CURSO_A)
    yield cliente
    # Restaurar el curso A, revisión 2
    restaurar = [{"criterio_id": cid, "cumplido": c, "observaciones": o or ""}
                 for cid, (c, o) in original.items()]
    cliente.put(f"/revisiones/actualizar_criterios/{id_a}/2", json={"criterios": restaurar})


def test_registro_queda_en_el_curso_y_revision_correctos(revisor):
    id_a, a_r2_antes = criterios(revisor, 2, CURSO_A)
    _, b_r2_antes = criterios(revisor, 2, CURSO_B)
    _, a_r1_antes = criterios(revisor, 1, CURSO_A)

    cambio = [{"criterio_id": cid, "cumplido": True, "observaciones": obs} for cid, obs in MARCAS.items()]
    r = revisor.put(f"/revisiones/actualizar_criterios/{id_a}/2", json={"criterios": cambio})
    assert r.status_code == 200, r.text

    _, a_r2 = criterios(revisor, 2, CURSO_A)
    for cid, obs in MARCAS.items():
        assert a_r2[cid] == (True, obs)
    # Los criterios no tocados del curso A siguen igual
    assert {k: v for k, v in a_r2.items() if k not in MARCAS} == \
           {k: v for k, v in a_r2_antes.items() if k not in MARCAS}

    # El curso B y la revisión 1 del curso A no cambian
    assert criterios(revisor, 2, CURSO_B)[1] == b_r2_antes
    assert criterios(revisor, 1, CURSO_A)[1] == a_r1_antes
