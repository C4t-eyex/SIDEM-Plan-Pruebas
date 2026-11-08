"""
Genera el PDF del plan de pruebas para entregar al docente.

Junta el plan (docs/plan-de-pruebas.md) y, como anexo, el registro de
defectos (docs/defectos.md), y los imprime a PDF con Chrome sin ventana.

Uso (desde la raíz del repositorio):
    pip install markdown==3.7
    python entrega/generar_pdf.py
"""
import re
import subprocess
import sys
from pathlib import Path

import markdown

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "entrega" / "Plan_de_Pruebas_SIDEM.pdf"
CHROME = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome",
]

CSS = """
@page { size: Letter; margin: 2cm 1.8cm; }
body { font-family: 'Segoe UI', Arial, sans-serif; font-size: 10.5pt; color: #1f2937; line-height: 1.45; }
h1 { font-size: 20pt; color: #1e3a8a; border-bottom: 3px solid #1e3a8a; padding-bottom: 6px; }
h2 { font-size: 14pt; color: #1e3a8a; margin-top: 22px; border-bottom: 1px solid #cbd5e1; padding-bottom: 3px; }
h3 { font-size: 11.5pt; color: #334155; margin-top: 14px; }
table { border-collapse: collapse; width: 100%; margin: 8px 0 12px; font-size: 9pt; page-break-inside: auto; }
tr { page-break-inside: avoid; }
th { background: #1e3a8a; color: #fff; text-align: left; padding: 5px 6px; }
td { border: 1px solid #cbd5e1; padding: 4px 6px; vertical-align: top; }
tr:nth-child(even) td { background: #f1f5f9; }
code { font-family: Consolas, monospace; font-size: 8.5pt; background: #eef2f7; padding: 0 3px; border-radius: 3px; }
pre { background: #eef2f7; padding: 8px; font-size: 8.5pt; white-space: pre-wrap; }
blockquote { border-left: 4px solid #93c5fd; margin: 8px 0; padding: 4px 12px; color: #334155; background: #f8fafc; }
hr { border: none; border-top: 1px solid #cbd5e1; margin: 16px 0; }
.anexo { page-break-before: always; }
"""


def a_html(ruta: Path) -> str:
    texto = ruta.read_text(encoding="utf-8")
    # Los enlaces a otros archivos del repositorio no sirven dentro del PDF: se deja solo el texto
    texto = re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]+\)", r"\1", texto)
    return markdown.markdown(texto, extensions=["tables", "sane_lists"])


def main() -> None:
    plan = a_html(RAIZ / "docs" / "plan-de-pruebas.md")
    defectos = a_html(RAIZ / "docs" / "defectos.md").replace("<h1>", "<h1>Anexo A. ", 1)
    html = (f"<!doctype html><html lang='es'><head><meta charset='utf-8'><title>Plan de Pruebas SIDEM</title><style>{CSS}</style></head>"
            f"<body>{plan}<div class='anexo'>{defectos}</div></body></html>")
    temporal = RAIZ / "entrega" / "_plan.html"
    temporal.write_text(html, encoding="utf-8")

    chrome = next((c for c in CHROME if Path(c).exists()), None)
    if not chrome:
        sys.exit("No se encontró Chrome. Abra entrega/_plan.html en el navegador e imprima a PDF.")
    subprocess.run([chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={SALIDA}", temporal.as_uri()], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    temporal.unlink()
    print(f"PDF generado: {SALIDA}")


if __name__ == "__main__":
    main()
