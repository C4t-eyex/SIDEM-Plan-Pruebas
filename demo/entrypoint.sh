#!/bin/sh
# Arranque de la demo: completa el esquema, carga los datos ficticios y levanta SIDEM.
set -e

echo "[demo] Esperando a PostgreSQL..."
python - <<'EOF'
import time
from sqlalchemy import text
from database import engine
for _ in range(30):
    try:
        with engine.connect() as c:
            c.execute(text("SELECT 1"))
        break
    except Exception:
        time.sleep(2)
else:
    raise SystemExit("[demo] PostgreSQL no respondió")
EOF

echo "[demo] Completando el esquema (verificar_schema --aplicar)..."
python scripts/verificar_schema.py --aplicar

echo "[demo] Cargando criterios y datos ficticios..."
python demo/seed_demo.py

echo "[demo] SIDEM disponible en http://localhost:${DEMO_PUERTO:-8090}"
exec uvicorn main:app --host 0.0.0.0 --port 5000
