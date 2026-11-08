"""
Configuración común de las pruebas automáticas contra la demo de SIDEM.

Las pruebas hablan con la demo por HTTP, igual que lo haría el navegador:
inician sesión con los usuarios ficticios de demo/seed_demo.py y consultan la API.
Antes de correrlas, la demo debe estar arriba y recién reiniciada
(ver pruebas-automaticas/README.md).
"""
import os

import httpx
import pytest

URL_DEMO = os.getenv("SIDEM_URL", "http://localhost:8090")
PASSWORD = os.getenv("DEMO_PASSWORD", "Demo-SIDEM-2026")
PERIODO = os.getenv("SIDEM_PERIODO", "2026-2")


def nueva_sesion() -> httpx.Client:
    # SIDEM revisa el encabezado Origin en las peticiones que modifican datos (CSRF)
    return httpx.Client(base_url=URL_DEMO, headers={"Origin": URL_DEMO}, timeout=60)


def iniciar_sesion(correo: str, password: str = PASSWORD) -> httpx.Client:
    """Devuelve un cliente con la cookie de sesión del usuario ya puesta."""
    cliente = nueva_sesion()
    r = cliente.post("/auth/login", json={"email": correo, "password": password})
    assert r.status_code == 200, f"No se pudo iniciar sesión con {correo}: {r.status_code} {r.text}"
    return cliente


def cursos_revision(cliente: httpx.Client, revision: int, **filtros) -> list:
    """Cursos que la pantalla de Seguimiento muestra para una revisión."""
    r = cliente.get("/revisiones/obtener_revisiones/",
                    params={"revision_numero": revision, "periodo": PERIODO, "page_size": 9999, **filtros})
    assert r.status_code == 200, r.text
    return r.json()["data"]


@pytest.fixture(scope="session", autouse=True)
def demo_disponible():
    try:
        httpx.get(f"{URL_DEMO}/login", timeout=10)
    except httpx.HTTPError:
        pytest.exit(f"La demo no responde en {URL_DEMO}. Levántala con 'docker compose up -d' en demo/.")


@pytest.fixture
def sesion():
    """Fábrica de sesiones; cierra todas al terminar la prueba."""
    abiertas = []

    def _abrir(correo: str) -> httpx.Client:
        cliente = iniciar_sesion(correo)
        abiertas.append(cliente)
        return cliente

    yield _abrir
    for cliente in abiertas:
        cliente.close()
