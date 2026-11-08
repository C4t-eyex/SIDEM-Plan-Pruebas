"""
TC-09 · Riesgo R08 · Condición CP-08 · Técnicas: valores límite y transición de estados.

5 intentos fallidos bloquean la cuenta; el 6.º, aunque traiga la clave
correcta, se rechaza; pasados 300 s se vuelve a permitir.

Tarda unos 6 minutos porque espera el desbloqueo real. Mientras corre, el
bloqueo también aplica a la IP, así que este archivo va de último y se puede
saltar con:  pytest -m "not lento"
"""
import time

import pytest

from conftest import PASSWORD, nueva_sesion

CUENTA = "revisor.pr@sidem.test"
BLOQUEO_S = 300


def intentar(password):
    with nueva_sesion() as c:
        return c.post("/auth/login", json={"email": CUENTA, "password": password}).status_code


@pytest.mark.lento
def test_bloqueo_y_desbloqueo():
    estados = []
    inicio = time.monotonic()
    for _ in range(5):
        estados.append(intentar("clave-equivocada"))
    assert estados == [401] * 5

    # 6.º intento con la clave correcta: bloqueado
    assert intentar(PASSWORD) == 429

    # Poco antes de cumplirse los 300 s sigue bloqueado
    time.sleep(max(0, inicio + BLOQUEO_S - 15 - time.monotonic()))
    assert intentar(PASSWORD) == 429

    # Pasados los 300 s, los fallos salen de la ventana y se permite
    time.sleep(max(0, inicio + BLOQUEO_S + 20 - time.monotonic()))
    assert intentar(PASSWORD) == 200
