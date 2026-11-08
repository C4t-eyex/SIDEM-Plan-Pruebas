# Descarga SIDEM en la versión fijada para las pruebas (commit 77f71b2) dentro de demo/sidem.
# Requiere acceso al repositorio privado de SIDEM (pedirlo al líder de pruebas).
$ErrorActionPreference = "Stop"
$commit  = "77f71b2"
$destino = Join-Path $PSScriptRoot "sidem"
if (-not (Test-Path $destino)) {
    git clone --quiet https://github.com/C4t-eyex/Seguimiento-docentes-Moodle.git $destino
}
git -C $destino fetch --quiet origin
git -C $destino checkout --quiet $commit
Write-Host "SIDEM listo en la versión $commit. Ahora: docker compose up --build"