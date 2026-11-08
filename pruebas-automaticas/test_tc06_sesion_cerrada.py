"""
TC-06 (complemento automático) · Riesgo R09 · Condición CP-09.

TC-06 se ejecuta a mano en el navegador (botón "Atrás"). Esta prueba revisa
lo mismo desde la API: después de cerrar sesión, la cookie que se tenía
antes no debería seguir sirviendo.
"""
from conftest import iniciar_sesion, nueva_sesion


def test_sesion_cerrada_no_se_reutiliza():
    cliente = iniciar_sesion("consulta@sidem.test")
    token = cliente.cookies.get("access_token")
    assert cliente.get("/auth/me").status_code == 200

    assert cliente.post("/auth/logout").status_code == 200
    assert cliente.get("/auth/me").status_code == 401  # el navegador ya no tiene la cookie
    cliente.close()

    # Alguien que copió la cookie antes del cierre intenta usarla
    with nueva_sesion() as otro:
        otro.cookies.set("access_token", token)
        assert otro.get("/auth/me").status_code == 401
