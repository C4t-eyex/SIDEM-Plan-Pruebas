#!/bin/sh
# Carga el esquema oficial de SIDEM sin detenerse en errores.
# db.sql (commit 77f71b2) falla en una base nueva en la migracion de seguimientos_estudiantes
# (columna estado_seguimiento inexistente); ver hallazgo HAL-01 en docs/avances.md.
# Lo que quede pendiente lo completa verificar_schema.py --aplicar al arrancar la app.
psql -v ON_ERROR_STOP=0 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -q -f /sidem-sql/db.sql
