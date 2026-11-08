#!/bin/sh
# Descarga SIDEM en la versión fijada para las pruebas (commit 77f71b2) dentro de demo/sidem.
# Requiere acceso al repositorio privado de SIDEM (pedirlo al líder de pruebas).
set -e
COMMIT=77f71b2
DESTINO="$(dirname "$0")/sidem"
[ -d "$DESTINO" ] || git clone --quiet https://github.com/C4t-eyex/Seguimiento-docentes-Moodle.git "$DESTINO"
git -C "$DESTINO" fetch --quiet origin
git -C "$DESTINO" checkout --quiet "$COMMIT"
echo "SIDEM listo en la versión $COMMIT. Ahora: docker compose up --build"