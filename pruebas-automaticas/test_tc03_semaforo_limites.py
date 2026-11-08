"""
TC-03 · Riesgo R04 · Condición CP-04 · Técnica: valores límite.

El semáforo cambia de color exactamente en 80 % (verde) y 50 % (amarillo).
Los seis cursos de la demo quedan justo en los límites y a cada lado de ellos.
"""
import pytest

from conftest import PERIODO

ESPERADO = [
    ("Programación Básica (DEMO)", 80, "verde"),
    ("Bases de Datos (DEMO)", 77, "amarillo"),
    ("Redes I (DEMO)", 50, "amarillo"),
    ("Procesos Industriales (DEMO)", 47, "rojo"),
    ("Calidad (DEMO)", 100, "verde"),
    ("Logística (DEMO)", 0, "rojo"),
]


@pytest.fixture(scope="module")
def stats():
    from conftest import iniciar_sesion
    lider = iniciar_sesion("lider@sidem.test")
    r = lider.get("/dashboard/stats/", params={"periodo": PERIODO, "revision_numero": 1})
    lider.close()
    assert r.status_code == 200
    return {c["nombre_curso"]: c for c in r.json()["docentes"]}


@pytest.mark.parametrize("curso,pct,color", ESPERADO)
def test_color_segun_porcentaje(stats, curso, pct, color):
    assert stats[curso]["pct_cumplimiento"] == pct
    assert stats[curso]["semaforo"] == color


def test_resumen_del_panel(stats):
    # 2 verdes, 2 amarillos y 2 rojos
    colores = [c["semaforo"] for c in stats.values()]
    assert {k: colores.count(k) for k in ("verde", "amarillo", "rojo")} == {"verde": 2, "amarillo": 2, "rojo": 2}
