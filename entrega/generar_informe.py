"""Genera el informe final en LaTeX (entrega/Informe_final_SIDEM.tex) y lo compila a PDF.

Arma un solo documento con lo que está en el repositorio:
  Parte I   Plan de pruebas            (docs/plan-de-pruebas.md)
  Parte II  Ejecución                  (docs/ejecucion-manual.md, pruebas-automaticas/README.md, evidencias/README.md)
  Parte III Defectos y correcciones    (docs/defectos.md, figuras antes/después, demo/correcciones/README.md, docs/retest.md)
  Parte IV  Informe de cierre          (docs/informe-de-cierre.md)
  Anexos    Preguntas al docente, bitácora y antecedentes

Los Markdown se convierten con un conversor propio (solo el subconjunto que usa el repo:
títulos, párrafos, listas, tablas, citas, bloques de código, negrita, cursiva, código y enlaces).

Uso (desde la raíz del repo):  python entrega/generar_informe.py
Requiere: MiKTeX o TeX Live con xelatex y latexmk, y Pillow para las figuras.
"""
import re
import subprocess
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
ENTREGA = RAIZ / "entrega"
FIGURAS = ENTREGA / "figuras"
NOMBRE = "Informe_final_SIDEM"


# ── Conversión de texto en línea ─────────────────────────────────────────────
def escapar(t: str) -> str:
    """Escapa los caracteres especiales de LaTeX."""
    rep = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
           "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(rep.get(c, c) for c in t)


def codigo(t: str) -> str:
    """Código en línea que puede partirse en / _ - . = para no salirse de las tablas."""
    salida = ""
    for i, c in enumerate(t):
        salida += escapar(c)
        # No partir después del último carácter (ej. "ERROR:") ni entre puntos seguidos (ej. "0001-...")
        if c in "/_-.=,:" and i < len(t) - 1 and t[i + 1] != ".":
            salida += r"\allowbreak{}"
    return r"\code{" + salida + "}"


def en_linea(t: str) -> str:
    """Convierte negrita, cursiva, código y enlaces de una línea de Markdown."""
    piezas = []

    def guardar(latex: str) -> str:
        piezas.append(latex)
        return f"\x00{len(piezas) - 1}\x00"

    # Código primero: su contenido no se interpreta
    t = re.sub(r"`([^`]+)`", lambda m: guardar(codigo(m.group(1))), t)

    # Enlaces: externos con \href; a archivos del repo, solo el texto
    def enlace(m):
        cuerpo = escapar_con_marcas(m.group(1))
        url = m.group(2)
        if url.startswith("http"):
            return guardar(r"\href{" + url.replace("%", r"\%").replace("#", r"\#") + "}{" + cuerpo + "}")
        return guardar(cuerpo)

    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", enlace, t)
    t = escapar_con_marcas(t)
    # Los enlaces pueden contener código: se resuelve hasta que no queden marcadores
    while "\x00" in t:
        t = re.sub(r"\x00(\d+)\x00", lambda m: piezas[int(m.group(1))], t)
    return t


def escapar_con_marcas(t: str) -> str:
    """Escapa el texto respetando los marcadores \x00n\x00 y convierte ** y *."""
    partes = re.split(r"(\x00\d+\x00)", t)
    salida = "".join(p if re.fullmatch(r"\x00\d+\x00", p) else escapar(p) for p in partes)
    salida = re.sub(r"\b(\d{5}-\d)\b", r"\\mbox{\1}", salida)  # no partir "29119-3"
    salida = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", salida)
    salida = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\\emph{\1}", salida)
    return salida


# ── Tablas ──────────────────────────────────────────────────────────────────
def celdas(linea: str) -> list[str]:
    linea = linea.strip()
    if linea.startswith("|"):
        linea = linea[1:]
    if linea.endswith("|"):
        linea = linea[:-1]
    # No partir en | dentro de código
    partes, actual, en_codigo = [], "", False
    for c in linea:
        if c == "`":
            en_codigo = not en_codigo
        if c == "|" and not en_codigo:
            partes.append(actual.strip())
            actual = ""
        else:
            actual += c
    partes.append(actual.strip())
    return partes


def tabla(lineas: list[str]) -> str:
    filas = [celdas(l) for l in lineas if not re.match(r"^\|\s*:?-{2,}", l.strip())]
    n = max(len(f) for f in filas)
    filas = [f + [""] * (n - len(f)) for f in filas]
    tam = r"\small" if n <= 4 else (r"\footnotesize" if n <= 6 else r"\scriptsize")
    # Anchos en pulgadas: cada columna recibe al menos lo que ocupa su palabra más larga (o el título en
    # negrita), para que no se partan "DEF-01" ni se salgan los encabezados; el resto del ancho se reparte
    # según el largo promedio del texto de cada columna.
    ancho_letra = {r"\small": 10, r"\footnotesize": 9, r"\scriptsize": 8}[tam] * 0.56 / 72
    total, relleno = 6.46, 12 / 72  # ancho del texto (A4 con márgenes de 2,3 cm) y separación entre columnas

    def palabras(celda: str) -> list[str]:
        trozos = []
        for i_parte, parte in enumerate(celda.split("`")):
            # Dentro de código se parte en / _ = , : (los nombres con . o - se cuentan enteros); fuera, en espacios
            trozos += re.split(r"[/_=,:]", parte) if i_parte % 2 else parte.split()
        return trozos or [""]

    minimos, deseados = [], []
    for i in range(n):
        largo_max = max((min(len(p), 16) + 1) * (1.12 if k == 0 else 1.0)
                        for k, f in enumerate(filas) for p in palabras(f[i]))
        minimos.append(largo_max * ancho_letra + relleno)
        promedio = sum(len(f[i].replace("`", "")) for f in filas[1:]) / max(1, len(filas) - 1)
        deseados.append(min(promedio, 60) * ancho_letra + relleno)
    if sum(minimos) >= total:
        anchos = [m * total / sum(minimos) for m in minimos]
    else:
        holgura = [max(d - m, 0.05) for d, m in zip(deseados, minimos)]
        sobra = total - sum(minimos)
        anchos = [m + sobra * h / sum(holgura) for m, h in zip(minimos, holgura)]
    promedio_x = (total - n * relleno) / n
    pesos = [(a - relleno) / promedio_x for a in anchos]
    spec = "".join(r">{\hsize=%.3f\hsize\raggedright\arraybackslash}X" % p for p in pesos)
    cab = " & ".join(r"\textbf{" + en_linea(c) + "}" for c in filas[0]) + r" \\"
    cuerpo = "\n".join(" & ".join(en_linea(c) for c in f) + r" \\ \hline" for f in filas[1:])
    # Altura estimada (en puntos): renglones de la celda más alta de cada fila
    puntos = {r"\small": 10, r"\footnotesize": 9, r"\scriptsize": 8}[tam] * 1.2 * 1.35
    alto = sum(puntos * max(1, max(-(-len(c.replace("`", "")) * ancho_letra // max(a - relleno, 0.2))
                                    for c, a in zip(f, anchos))) + 4 for f in filas)
    if alto < 170:
        # Tabla corta (menos de ~6 cm): no se parte entre páginas y se queda junto al texto que la presenta
        # La primera línea (%ALTO=...) la usa markdown() para que el párrafo que presenta la tabla reserve su altura
        return (f"%ALTO={int(alto)}\n\\par\\noindent\\begin{{minipage}}{{\\linewidth}}{tam}\n\\begin{{tabularx}}{{\\linewidth}}{{{spec}}}\n"
                "\\hline\\rowcolor{cabecera}\n" + cab + " \\hline\n" + cuerpo + "\n\\end{tabularx}\\end{minipage}\\par\n")
    # Tabla larga: puede partirse. \Needspace hace el salto ANTES de que empiece la tabla si al pie no caben
    # el encabezado y un par de filas (así el encabezado no queda solo ni se repite)
    encabezado = "\\hline\\rowcolor{cabecera}\n" + cab + " \\hline\n"
    return (f"\\par\\Needspace{{8\\baselineskip}}{{{tam}\n\\begin{{xltabular}}{{\\linewidth}}{{{spec}}}\n"
            + encabezado + "\\endfirsthead\n" + encabezado + "\\endhead\n" + cuerpo + "\n\\end{xltabular}}\n")


# ── Bloques ─────────────────────────────────────────────────────────────────
def markdown(texto: str, nivel_base: int = 0, saltar_h1: bool = True) -> str:
    """Convierte un documento Markdown. nivel_base desplaza los títulos (## -> sección)."""
    lineas = texto.splitlines()
    out, i = [], 0
    comandos = ["chapter", "section", "subsection", "subsubsection", "paragraph"]
    while i < len(lineas):
        l = lineas[i]
        s = l.strip()
        if not s or s == "---":
            i += 1
            continue
        # Bloque de código (puede venir sangrado dentro de una lista)
        if s.startswith("```"):
            cuerpo = []
            sangria = len(l) - len(l.lstrip())
            i += 1
            while i < len(lineas) and not lineas[i].strip().startswith("```"):
                cuerpo.append(lineas[i][sangria:] if lineas[i][:sangria].strip() == "" else lineas[i])
                i += 1
            i += 1
            out.append("\\begin{lstlisting}\n" + "\n".join(cuerpo) + "\n\\end{lstlisting}")
            continue
        # Títulos
        m = re.match(r"^(#{1,4})\s+(.*)", s)
        if m:
            nivel = len(m.group(1))
            if nivel == 1 and saltar_h1:
                i += 1
                continue
            cmd = comandos[min(nivel - 1 + nivel_base, len(comandos) - 1)]  # ## -> sección, ### -> subsección
            titulo = en_linea(m.group(2))
            corto = re.sub(r"\\(code|textbf|emph)\{", "{", titulo)
            # \Needspace evita que el título quede solo al final de la página
            espacio = "" if cmd == "chapter" else "\\Needspace{7\\baselineskip}"
            out.append(f"{espacio}\\{cmd}*{{{titulo}}}\\addcontentsline{{toc}}{{{cmd}}}{{{corto}}}")
            i += 1
            continue
        # Tabla
        if s.startswith("|"):
            bloque = []
            while i < len(lineas) and lineas[i].strip().startswith("|"):
                bloque.append(lineas[i])
                i += 1
            tex = tabla(bloque)
            m_alto = re.match(r"%ALTO=(\d+)", tex)
            # Lo que presenta la tabla (un título y/o un párrafo "...:") reserva el alto de la tabla corta,
            # o unos renglones si es larga, para no quedar solo al pie de la página
            # (la tabla larga pide además 8 renglones propios con \Needspace, por eso la reserva es mayor)
            reserva = int(m_alto.group(1)) + 45 if m_alto else 150
            for atras in (1, 2):
                if len(out) >= atras and out[-atras].startswith("\\Needspace{"):
                    resto = re.sub(r"^\\Needspace\{[^}]*\}", "", out[-atras])
                    out[-atras] = f"\\Needspace{{{reserva + 40 * (atras - 1)}pt}}" + resto
                else:
                    break
            out.append(tex)
            continue
        # Cita
        if s.startswith(">"):
            bloque = []
            while i < len(lineas) and lineas[i].strip().startswith(">"):
                bloque.append(re.sub(r"^\s*>\s?", "", lineas[i]))
                i += 1
            out.append("\\begin{nota}\n" + markdown("\n".join(bloque), nivel_base, False) + "\n\\end{nota}")
            continue
        # Listas
        m_num = re.match(r"^(\d+)\.\s+", s)
        if s.startswith("- ") or s.startswith("* ") or m_num:
            numerada = bool(m_num)
            entorno = "enumerate" if numerada else "itemize"
            inicio = f"[start={m_num.group(1)}]" if numerada and m_num.group(1) != "1" else ""
            items = []
            while i < len(lineas):
                t = lineas[i].strip()
                es_item = (re.match(r"^\d+\.\s+", t) if numerada else (t.startswith("- ") or t.startswith("* ")))
                if es_item:
                    items.append(re.sub(r"^(\d+\.|[-*])\s+", "", t))
                elif t and not t.startswith("```") and not t.startswith("|") and items and lineas[i].startswith("   "):
                    items[-1] += " " + t  # continuación sangrada
                else:
                    break
                i += 1
            out.append(f"\\begin{{{entorno}}}{inicio}\n" + "\n".join("\\item " + en_linea(x) for x in items) + f"\n\\end{{{entorno}}}")
            continue
        # Párrafo: líneas seguidas hasta un bloque distinto
        bloque = []
        while i < len(lineas):
            t = lineas[i].strip()
            if not t or t.startswith(("#", "|", ">", "```", "- ", "* ")) or re.match(r"^\d+\.\s+", t) or t == "---":
                break
            bloque.append(t)
            i += 1
        parrafo = en_linea(" ".join(bloque))
        # Un párrafo que presenta lo que sigue ("Riesgos del producto:") no se queda solo al pie de página
        termina_en_dos_puntos = bloque[-1].rstrip("*_ ").endswith(":")  # también "**Finalización:**"
        out.append(("\\Needspace{6\\baselineskip}" if termina_en_dos_puntos else "") + parrafo + "\n")
    return "\n\n".join(out)


def leer(ruta: str) -> str:
    return (RAIZ / ruta).read_text(encoding="utf-8")


# ── Figuras de antes y después ──────────────────────────────────────────────
def figuras() -> str:
    FIGURAS.mkdir(exist_ok=True)
    gif = RAIZ / "exposicion" / "gif"
    img = RAIZ / "exposicion" / "img"
    fuentes = {
        "def01-antes": gif / "DEF-01_antes_lider_sin_departamento_ve_todo.gif",
        "def01-despues": gif / "DEF-01_despues_lider_sin_departamento_no_ve_cursos.gif",
        "def02-antes": gif / "DEF-02_antes_sesion_cerrada_reutilizable.gif",
        "def02-despues": gif / "DEF-02_despues_sesion_cerrada_no_se_reutiliza.gif",
        "def04-antes": img / "DEF-04_antes_consulta_sin_cursos.png",
        "def04-despues": img / "DEF-04_despues_consulta_ve_6_cursos.png",
    }
    for nombre, origen in fuentes.items():
        # De los GIF se toma el primer cuadro, que es el resultado final de la grabación
        Image.open(origen).convert("RGB").save(FIGURAS / f"{nombre}.png")
    pares = [
        ("def01", "DEF-01. El líder sin departamento (\\code{lider.sindep@sidem.test}) en Métricas, revisión 1",
         "Antes: ve los 6 cursos de la institución.", "Después: 0 cursos y «Sin datos para los filtros seleccionados»."),
        ("def02", "DEF-02. Petición a \\code{/auth/me} con la cookie copiada antes de cerrar sesión",
         "Antes: responde 200 con los datos del usuario.", "Después: responde 401 «Sesión expirada»."),
        ("def04", "DEF-04. El usuario de consulta (\\code{consulta@sidem.test}) en Seguimiento, revisión 1",
         "Antes: no ve ningún curso.", "Después: con alcance «Todos» ve los 6 cursos."),
    ]
    bloques = ["\\section*{Evidencia visual: antes y después}\\addcontentsline{toc}{section}{Evidencia visual: antes y después}",
               "Capturas de la demo con la versión \\code{77f71b2} (antes) y con las correcciones (después). "
               "Las de DEF-01 y DEF-02 son el cuadro final de las grabaciones que se muestran en la exposición "
               "(\\code{exposicion/gif/}); las de DEF-04 salen de \\code{evidencias/}. DEF-03 y DEF-05 se ven en la "
               "salida de las pruebas y del log de la base, descrita en el registro de defectos."]
    for clave, titulo, antes, despues in pares:
        bloques.append(
            "\\begin{figure}[H]\\centering\n"
            f"\\begin{{minipage}}[t]{{0.485\\linewidth}}\\centering\\includegraphics[width=\\linewidth,height=5.2cm,keepaspectratio]{{figuras/{clave}-antes.png}}\\\\[2pt]{{\\small\\color{{rojo}}\\textbf{{{antes}}}}}\\end{{minipage}}\\hfill\n"
            f"\\begin{{minipage}}[t]{{0.485\\linewidth}}\\centering\\includegraphics[width=\\linewidth,height=5.2cm,keepaspectratio]{{figuras/{clave}-despues.png}}\\\\[2pt]{{\\small\\color{{verde}}\\textbf{{{despues}}}}}\\end{{minipage}}\n"
            f"\\caption{{{titulo}.}}\\end{{figure}}")
    return "\n\n".join(bloques)


# ── Documento ───────────────────────────────────────────────────────────────
PREAMBULO = r"""\documentclass[11pt,a4paper,oneside]{report}
\usepackage{fontspec}
\setmainfont{Cambria}
\setsansfont{Segoe UI}
\setmonofont{Consolas}[Scale=0.9]
\usepackage[spanish,es-noshorthands]{babel}
\usepackage[margin=2.3cm,headheight=15pt]{geometry}
\usepackage[table]{xcolor}
\usepackage{xltabular}
\usepackage{array}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{graphicx}
\usepackage{float}
\usepackage{caption}
\usepackage{needspace}
\usepackage{ragged2e}
\usepackage{listings}
\usepackage[most]{tcolorbox}
\usepackage[hidelinks]{hyperref}

% Paleta de SIDEM (la misma de la aplicación y de la presentación)
\definecolor{azul}{HTML}{2563EB}
\definecolor{tinta}{HTML}{1E293B}
\definecolor{gris}{HTML}{64748B}
\definecolor{borde}{HTML}{CBD5E1}
\definecolor{fondo}{HTML}{F0F4F8}
\definecolor{cabecera}{HTML}{E2E8F0}
\definecolor{verde}{HTML}{16A34A}
\definecolor{ambar}{HTML}{D97706}
\definecolor{rojo}{HTML}{DC2626}
\arrayrulecolor{borde}

\hypersetup{pdftitle={Informe final de pruebas - SIDEM},pdfauthor={Equipo SIDEM}}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\color{gris}\sffamily\small Informe final de pruebas · SIDEM}
\fancyhead[R]{\color{gris}\sffamily\small ISO/IEC/IEEE 29119-3}
\fancyfoot[C]{\color{gris}\sffamily\small\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\color{gris}\sffamily\small\thepage}\renewcommand{\headrulewidth}{0pt}}

\titleformat{\part}[display]{\centering\sffamily\color{azul}}{}{0pt}{\Huge\bfseries}
\titleformat{\chapter}[block]{\sffamily\color{tinta}\huge\bfseries}{}{0pt}{}[\vspace{2pt}{\color{azul}\titlerule[1.2pt]}]
\titleformat{\section}{\sffamily\color{azul}\Large\bfseries}{}{0pt}{}
\titleformat{\subsection}{\sffamily\color{tinta}\large\bfseries}{}{0pt}{}
\titleformat{\subsubsection}{\sffamily\color{tinta}\normalsize\bfseries}{}{0pt}{}
\titlespacing*{\chapter}{0pt}{0pt}{14pt}
\titlespacing*{\section}{0pt}{14pt}{5pt}
\titlespacing*{\subsection}{0pt}{10pt}{4pt}

\setlist[itemize]{leftmargin=1.3em,itemsep=2pt,topsep=3pt}
\setlist[enumerate]{leftmargin=1.6em,itemsep=2pt,topsep=3pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
% Texto alineado a la izquierda (con guiones): evita los huecos que deja el justificado con rutas largas
\AtBeginDocument{\RaggedRight\setlength{\parskip}{5pt}}
\renewcommand{\arraystretch}{1.35}
\captionsetup{font={small,sf},labelfont={bf,color=azul}}

% \leavevmode evita que \color abra una línea vacía al inicio de una celda de tabla
\newcommand{\code}[1]{\leavevmode{\ttfamily\color{tinta}#1}}
\newtcolorbox{nota}{enhanced,breakable,colback=fondo,colframe=azul,boxrule=0pt,leftrule=2.5pt,arc=0pt,
  left=8pt,right=8pt,top=4pt,bottom=4pt,before skip=6pt,after skip=6pt}
\lstset{basicstyle=\ttfamily\footnotesize,breaklines=true,columns=fullflexible,keepspaces=true,
  backgroundcolor=\color{fondo},frame=single,rulecolor=\color{borde},xleftmargin=4pt,xrightmargin=4pt,
  framesep=5pt,upquote=true,extendedchars=true}
\setcounter{tocdepth}{1}
\setlength{\emergencystretch}{3em}
"""

PORTADA = r"""
\begin{titlepage}
\sffamily
\vspace*{1.2cm}
{\color{verde}\rule{0.9cm}{0.9cm}}\hspace{6pt}{\color{ambar}\rule{0.9cm}{0.9cm}}\hspace{6pt}{\color{rojo}\rule{0.9cm}{0.9cm}}\par
\vspace{1.4cm}
{\color{azul}\large\bfseries PRUEBAS DE SOFTWARE 2026-2 · ISO/IEC/IEEE 29119-3}\par
\vspace{0.4cm}
{\color{tinta}\fontsize{32}{38}\selectfont\bfseries Informe final de pruebas\\[4pt] de SIDEM}\par
\vspace{0.5cm}
{\color{gris}\Large Plan, ejecución, defectos, correcciones y cierre}\par
\vspace{0.3cm}
{\color{gris}\large Sistema de seguimiento a docentes en Moodle}\par
\vfill
{\color{tinta}\large\bfseries Equipo}\par\vspace{4pt}
{\color{tinta}\large Marcos Duque Jaramillo\\ Sebastián Díaz Jiménez\\ Nicolás Cataño Durango\\ Julián Ramírez Molina}\par
\vspace{0.8cm}
{\color{tinta}\large\bfseries Docente}\par\vspace{4pt}
{\color{tinta}\large Roberto José Calderón Bermejo}\par
\vspace{0.8cm}
{\color{gris}17 de noviembre de 2026 · Repositorio: \href{https://github.com/C4t-eyex/SIDEM-Plan-Pruebas}{github.com/C4t-eyex/SIDEM-Plan-Pruebas}}\par
\end{titlepage}
"""

INTRO = r"""
\chapter*{Introducción}\addcontentsline{toc}{chapter}{Introducción}
Este informe reúne el trabajo final del curso: un plan de pruebas según la norma ISO/IEC/IEEE \mbox{29119-3}, adaptado (\emph{tailoring}) a un ciclo de 9 días, y su ejecución sobre SIDEM, el sistema de seguimiento a docentes en Moodle. Se probó la versión \code{77f71b2} en una demo con Docker y datos ficticios, sin usar la base de producción.

\begin{nota}
\textbf{Resultado.} Los 9 casos planeados (TC-01 a TC-09) se ejecutaron. La primera ronda de pruebas automáticas dio 16 de 19 y encontró, junto con la ejecución manual y el montaje de la demo, 5 defectos (1 alto, 2 medios y 2 bajos). Los 5 se corrigieron con parches sobre la versión probada y en el retest del 16/11/2026 pasan las 19 pruebas. Se cumplen todos los criterios de finalización del plan.
\end{nota}

\textbf{Cómo está organizado.}
\begin{itemize}
\item \textbf{Parte I. Plan de pruebas:} el plan completo en las 8 secciones pedidas (versión 1.0).
\item \textbf{Parte II. Ejecución:} las hojas de ejecución manual con lo obtenido, las pruebas automáticas y el índice de evidencias.
\item \textbf{Parte III. Defectos, correcciones y retest:} el registro de defectos, la evidencia visual del antes y el después, las correcciones y el retest.
\item \textbf{Parte IV. Informe de cierre:} el \emph{Test Completion Report} (versión 1.0).
\item \textbf{Anexos:} preguntas al docente, bitácora de avances y antecedentes (Actividades 1 y 2, matriz de riesgos y Talleres 4 y 5).
\end{itemize}

Todo el material, incluidas las capturas, las salidas de pytest y los parches, está en el repositorio del equipo. Las rutas de archivo que aparecen en el texto son rutas dentro de ese repositorio.
"""


def capitulo(titulo: str, ruta: str) -> str:
    return f"\\chapter*{{{titulo}}}\\addcontentsline{{toc}}{{chapter}}{{{titulo}}}\n\n" + markdown(leer(ruta))


def parte(titulo: str) -> str:
    # titlesec ya agrega \part* al índice; no se agrega otra entrada
    return f"\\part*{{{titulo}}}\n"


TITULOS_ANTECEDENTES = [
    "C.1 Actividad 1. Alcance preliminar",
    "C.2 Actividad 2. Objeto de prueba y condiciones",
    "C.3 Matriz de riesgos",
    "C.4 Taller 4. Estrategia de pruebas",
    "C.5 Taller 5. Casos, procedimientos, datos y entorno",
]


def documento() -> str:
    antecedentes = sorted((RAIZ / "docs" / "antecedentes").glob("*.md"))
    assert len(antecedentes) == len(TITULOS_ANTECEDENTES), "Hay antecedentes sin título en TITULOS_ANTECEDENTES"
    cuerpo = [
        PREAMBULO, "\\begin{document}", PORTADA,
        "\\tableofcontents\\clearpage", INTRO,
        parte("Parte I. Plan de pruebas"),
        capitulo("Plan de pruebas", "docs/plan-de-pruebas.md"),
        parte("Parte II. Ejecución"),
        capitulo("Ejecución manual", "docs/ejecucion-manual.md"),
        capitulo("Pruebas automáticas", "pruebas-automaticas/README.md"),
        capitulo("Evidencias", "evidencias/README.md"),
        parte("Parte III. Defectos, correcciones y retest"),
        capitulo("Registro de defectos", "docs/defectos.md") + "\n\n" + figuras(),
        capitulo("Correcciones", "demo/correcciones/README.md"),
        capitulo("Retest", "docs/retest.md"),
        parte("Parte IV. Informe de cierre"),
        capitulo("Informe de cierre", "docs/informe-de-cierre.md"),
        parte("Anexos"),
        capitulo("Anexo A. Preguntas al docente", "docs/preguntas-para-el-profe.md"),
        capitulo("Anexo B. Bitácora de avances", "docs/avances.md"),
        "\\chapter*{Anexo C. Antecedentes}\\addcontentsline{toc}{chapter}{Anexo C. Antecedentes}\n"
        "Resumen de las entregas previas que dieron origen al plan. Los originales están en la carpeta "
        + codigo("entregables-previos/") + " del repositorio.\n\n"
        + "\n\n".join(f"\\section*{{{t}}}\\addcontentsline{{toc}}{{section}}{{{t}}}\n\n"
                      + markdown(a.read_text(encoding="utf-8"), nivel_base=1)
                      for t, a in zip(TITULOS_ANTECEDENTES, antecedentes)),
        "\\end{document}",
    ]
    return "\n\n".join(cuerpo)


def main() -> None:
    tex = ENTREGA / f"{NOMBRE}.tex"
    tex.write_text(documento(), encoding="utf-8")
    print("LaTeX generado:", tex)
    r = subprocess.run(["latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error", f"{NOMBRE}.tex"],
                       cwd=ENTREGA, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(r.stdout[-4000:])
        raise SystemExit("Falló la compilación")
    subprocess.run(["latexmk", "-c", f"{NOMBRE}.tex"], cwd=ENTREGA, capture_output=True)
    print("PDF generado:", ENTREGA / f"{NOMBRE}.pdf")


if __name__ == "__main__":
    main()
