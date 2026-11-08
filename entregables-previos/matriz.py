from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER

OUT = "/tmp/outputs/Matriz_de_riesgos_SIDEM.pdf"

AZUL = colors.HexColor("#1F3A5F")
GRIS = colors.HexColor("#F2F4F7")
LINEA = colors.HexColor("#B8C2CC")
VERDE = colors.HexColor("#C8E6C9")
AMAR = colors.HexColor("#FFE9A8")
ROJO = colors.HexColor("#F4B6B6")

ss = getSampleStyleSheet()
H1 = ParagraphStyle("h1", parent=ss["Title"], fontName="Helvetica-Bold", fontSize=18, textColor=AZUL, spaceAfter=4)
SUB = ParagraphStyle("sub", parent=ss["Normal"], fontSize=10.5, textColor=colors.HexColor("#4A5568"), alignment=TA_CENTER, spaceAfter=12)
H2 = ParagraphStyle("h2", parent=ss["Heading2"], fontName="Helvetica-Bold", fontSize=12.5, textColor=AZUL, spaceBefore=10, spaceAfter=6)
P = ParagraphStyle("p", parent=ss["Normal"], fontSize=10, leading=14, spaceAfter=6)
C = ParagraphStyle("c", parent=ss["Normal"], fontSize=8.8, leading=11.2)
CC = ParagraphStyle("cc", parent=C, alignment=TA_CENTER)
CH = ParagraphStyle("ch", parent=C, fontName="Helvetica-Bold", textColor=colors.white, alignment=TA_CENTER)


def nivel(p, i):
    v = p * i
    if v >= 6:
        return v, "Alto", ROJO
    if v >= 3:
        return v, "Medio", AMAR
    return v, "Bajo", VERDE


# ID, riesgo, causa/consecuencia, funcionalidad, P, I, tratamiento
producto = [
    ("R01", "Un usuario puede ver o modificar información que su rol no le permite.",
     "Permisos mal configurados o mal aplicados. Se exponen o alteran datos de seguimiento.",
     "F02", 2, 3, "Probar cada rol intentando acciones no permitidas y verificar que el sistema las bloquee."),
    ("R02", "Un usuario ve cursos o docentes de un departamento que no le corresponde.",
     "El filtro por departamento no se aplica en todas las pantallas.",
     "F02", 2, 3, "Probar con usuarios de distintos departamentos y con un usuario sin departamento asignado."),
    ("R03", "Los criterios u observaciones se guardan en el curso o la revisión equivocados.",
     "Error al asociar el registro. Los resultados del docente quedan alterados.",
     "F03", 2, 3, "Registrar datos, volver a consultarlos y confirmar que aparecen en el curso y la revisión correctos."),
    ("R04", "El semáforo muestra un color que no corresponde al porcentaje de cumplimiento.",
     "Error en el cálculo o en los límites (80 % y 50 %). Los líderes toman decisiones equivocadas.",
     "F04", 2, 3, "Probar cursos con porcentajes justo en los límites y verificar el color asignado."),
    ("R05", "Se pierde información registrada al editar o al recargar la página.",
     "Falla al guardar. El revisor debe repetir el trabajo.",
     "F03", 2, 2, "Editar criterios y observaciones, recargar la página y comprobar que los cambios se conservan."),
    ("R06", "Las métricas no coinciden con lo que se registró en el seguimiento.",
     "Datos duplicados, cursos que no deberían contarse o filtros mal aplicados.",
     "F05", 2, 2, "Comparar los totales del panel con un conteo manual de una muestra de cursos."),
    ("R07", "El informe exportado no coincide con lo que muestra el sistema.",
     "Columnas o filtros distintos entre la pantalla y el archivo.",
     "F06", 2, 2, "Exportar con distintos filtros y comparar el archivo con la información en pantalla."),
    ("R08", "Alguien logra entrar con credenciales incorrectas o por intentos repetidos.",
     "Falta de control en el inicio de sesión.",
     "F01", 1, 3, "Probar contraseñas incorrectas, intentos repetidos y verificar el bloqueo temporal."),
    ("R09", "La sesión sigue activa después de cambiar la contraseña o de cerrar sesión.",
     "La sesión no se invalida correctamente.",
     "F01", 1, 2, "Cerrar sesión o cambiar la contraseña y verificar que la sesión anterior ya no funciona."),
    ("R10", "El sistema se vuelve lento con muchos cursos registrados.",
     "Consultas pesadas en el listado o en las métricas.",
     "F03, F05", 1, 2, "Medir el tiempo de carga del listado y del panel con un volumen alto de cursos."),
]

proyecto = [
    ("RP1", "No contar con datos de prueba suficientes o representativos.",
     2, 2, "Preparar con anticipación un conjunto de cursos, usuarios y roles de prueba."),
    ("RP2", "Tiempo limitado del equipo para ejecutar todas las pruebas.",
     2, 2, "Ejecutar primero las pruebas de los riesgos de nivel alto."),
    ("RP3", "Cambios en el sistema durante el periodo de pruebas.",
     1, 2, "Fijar una versión del sistema para probar y registrar cualquier cambio."),
]


def footer(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica", 8)
    canv.setFillColor(colors.HexColor("#718096"))
    canv.drawString(1.5 * cm, 1 * cm, "Matriz de riesgos SIDEM | ISO/IEC/IEEE 29119-3")
    canv.drawRightString(landscape(A4)[0] - 1.5 * cm, 1 * cm, f"Página {doc.page}")
    canv.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=landscape(A4), leftMargin=1.5 * cm, rightMargin=1.5 * cm,
                        topMargin=1.4 * cm, bottomMargin=1.6 * cm,
                        title="Matriz de riesgos SIDEM", author="Equipo SIDEM")
W = landscape(A4)[0] - 3 * cm
s = []

s.append(Paragraph("Matriz de riesgos del plan de pruebas", H1))
s.append(Paragraph("Sistema SIDEM (Seguimiento a docentes) | Norma ISO/IEC/IEEE 29119-3", SUB))

info = Table([
    [Paragraph("<b>Sistema</b>", C), Paragraph("SIDEM, seguimiento a docentes", C),
     Paragraph("<b>Fecha</b>", C), Paragraph("07/10/2026", C)],
    [Paragraph("<b>Integrantes</b>", C),
     Paragraph("Marcos Duque Jaramillo, Sebastián Díaz Jiménez, Nicolás Castaño Durango, Julián Ramírez Molina", C),
     Paragraph("<b>Alcance</b>", C), Paragraph("Funcionalidades F01 a F06", C)],
], colWidths=[2.6 * cm, W * 0.55, 2.2 * cm, None])
info.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 0.5, LINEA), ("BACKGROUND", (0, 0), (0, -1), GRIS),
    ("BACKGROUND", (2, 0), (2, -1), GRIS), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
s.append(info)

s.append(Paragraph("1. Propósito", H2))
s.append(Paragraph(
    "Esta matriz identifica qué puede salir mal en SIDEM, qué tan probable es y qué tanto afectaría. "
    "Con esa información se decide qué probar primero y con más cuidado, como propone la norma "
    "ISO/IEC/IEEE 29119-3 para el registro de riesgos del plan de pruebas. Se consideran las "
    "funcionalidades definidas en la Actividad 2:", P))
func = [["ID", "Funcionalidad", "ID", "Funcionalidad"],
        ["F01", "Inicio de sesión", "F04", "Semáforo de cumplimiento"],
        ["F02", "Gestión de usuarios y roles", "F05", "Panel de métricas"],
        ["F03", "Registro del seguimiento a docentes", "F06", "Exportación de informes"]]
ft = Table([[Paragraph(x, CH if r == 0 else C) for x in row] for r, row in enumerate(func)],
           colWidths=[1.3 * cm, 7 * cm, 1.3 * cm, 7 * cm], hAlign="LEFT")
ft.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), AZUL), ("GRID", (0, 0), (-1, -1), 0.5, LINEA),
                        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
s.append(ft)

s.append(Paragraph("2. Escalas de valoración", H2))
s.append(Paragraph(
    "Cada riesgo se califica con dos valores de 1 a 3. El nivel de riesgo es el resultado de multiplicar "
    "la probabilidad por el impacto.", P))
esc = [["Valor", "Probabilidad (qué tan posible es que pase)", "Impacto (qué tanto afecta si pasa)"],
       ["1 Baja", "Es poco probable que ocurra.", "Molestia menor; el trabajo puede continuar."],
       ["2 Media", "Puede ocurrir en algunas situaciones.", "Afecta el trabajo o la calidad de la información."],
       ["3 Alta", "Es muy probable que ocurra.", "Expone información o lleva a decisiones equivocadas."]]
et = Table([[Paragraph(x, CH if r == 0 else C) for x in row] for r, row in enumerate(esc)],
           colWidths=[2.4 * cm, (W - 2.4 * cm) / 2, (W - 2.4 * cm) / 2])
et.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), AZUL), ("GRID", (0, 0), (-1, -1), 0.5, LINEA),
                        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
s.append(et)
s.append(Spacer(1, 8))
niv = [["Nivel", "Resultado", "Qué significa"],
       ["Bajo", "1 a 2", "Se prueba si queda tiempo."],
       ["Medio", "3 a 4", "Se prueba en el ciclo normal de pruebas."],
       ["Alto", "6 a 9", "Se prueba primero y con más casos."]]
nt = Table([[Paragraph(x, CH if r == 0 else C) for x in row] for r, row in enumerate(niv)],
           colWidths=[2.4 * cm, 2.6 * cm, 9 * cm], hAlign="LEFT")
nt.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), AZUL), ("GRID", (0, 0), (-1, -1), 0.5, LINEA),
                        ("BACKGROUND", (0, 1), (0, 1), VERDE), ("BACKGROUND", (0, 2), (0, 2), AMAR),
                        ("BACKGROUND", (0, 3), (0, 3), ROJO),
                        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
s.append(nt)

s.append(PageBreak())
s.append(Paragraph("3. Riesgos del producto", H2))
s.append(Paragraph("Riesgos relacionados con fallas del sistema, ordenados de mayor a menor nivel.", P))
hdr = ["ID", "Riesgo", "Causa o consecuencia", "Func.", "P", "I", "Nivel", "Cómo se aborda en las pruebas"]
rows = [[Paragraph(h, CH) for h in hdr]]
style = [("BACKGROUND", (0, 0), (-1, 0), AZUL), ("GRID", (0, 0), (-1, -1), 0.5, LINEA),
         ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
         ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]
orden = sorted(producto, key=lambda r: -(r[4] * r[5]))
for k, (rid, r, c, f, p, i, t) in enumerate(orden, start=1):
    v, n, col = nivel(p, i)
    rows.append([Paragraph(f"<b>{rid}</b>", CC), Paragraph(r, C), Paragraph(c, C), Paragraph(f, CC),
                 Paragraph(str(p), CC), Paragraph(str(i), CC), Paragraph(f"<b>{n}</b> ({v})", CC), Paragraph(t, C)])
    style.append(("BACKGROUND", (6, k), (6, k), col))
cw = [1.2, 6.0, 5.6, 1.5, 0.8, 0.8, 1.9]
cw = [x * cm for x in cw]
cw.append(W - sum(cw))
pt = Table(rows, colWidths=cw, repeatRows=1)
pt.setStyle(TableStyle(style))
s.append(pt)

s.append(PageBreak())
s.append(Paragraph("4. Riesgos del proyecto", H2))
s.append(Paragraph("Riesgos que pueden afectar la ejecución del plan de pruebas, no el sistema en sí.", P))
rows = [[Paragraph(h, CH) for h in ["ID", "Riesgo", "P", "I", "Nivel", "Cómo se maneja"]]]
style = [("BACKGROUND", (0, 0), (-1, 0), AZUL), ("GRID", (0, 0), (-1, -1), 0.5, LINEA),
         ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
         ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]
for k, (rid, r, p, i, t) in enumerate(proyecto, start=1):
    v, n, col = nivel(p, i)
    rows.append([Paragraph(f"<b>{rid}</b>", CC), Paragraph(r, C), Paragraph(str(p), CC), Paragraph(str(i), CC),
                 Paragraph(f"<b>{n}</b> ({v})", CC), Paragraph(t, C)])
    style.append(("BACKGROUND", (4, k), (4, k), col))
cw = [x * cm for x in [1.2, 8.5, 0.8, 0.8, 1.9]]
cw.append(W - sum(cw))
rt = Table(rows, colWidths=cw)
rt.setStyle(TableStyle(style))
s.append(rt)

# Mapa de calor
s.append(Paragraph("5. Mapa de calor", H2))
s.append(Paragraph("Ubicación de cada riesgo según su probabilidad e impacto.", P))
celdas = {}
for rid, _, _, _, p, i, _ in producto:
    celdas.setdefault((p, i), []).append(rid)
for rid, _, p, i, _ in proyecto:
    celdas.setdefault((p, i), []).append(rid)
etq = {1: "Baja (1)", 2: "Media (2)", 3: "Alta (3)"}
data = [[Paragraph("<b>Probabilidad</b>", CC), "", "", ""]]
for p in [3, 2, 1]:
    fila = [Paragraph(etq[p], CC)]
    for i in [1, 2, 3]:
        fila.append(Paragraph("<b>" + ", ".join(celdas.get((p, i), [])) + "</b>", CC))
    data.append(fila)
data.append([""] + [Paragraph(f"<b>Impacto {etq[i]}</b>", CC) for i in [1, 2, 3]])
hs = [("GRID", (0, 1), (-1, 3), 0.8, colors.white), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
      ("SPAN", (0, 0), (-1, 0))]
for r, p in enumerate([3, 2, 1], start=1):
    hs.append(("BACKGROUND", (0, r), (0, r), GRIS))
    for c, i in enumerate([1, 2, 3], start=1):
        hs.append(("BACKGROUND", (c, r), (c, r), nivel(p, i)[2]))
mapa = Table(data, colWidths=[3.2 * cm, 5 * cm, 5 * cm, 5 * cm],
             rowHeights=[0.8 * cm, 1.6 * cm, 1.6 * cm, 1.6 * cm, 0.8 * cm], hAlign="LEFT")
mapa.setStyle(TableStyle(hs))
s.append(KeepTogether([mapa]))

s.append(Paragraph("6. Conclusión", H2))
s.append(Paragraph(
    "Los riesgos de nivel alto se concentran en el control de acceso por roles (R01, R02), el registro "
    "del seguimiento (R03) y el cálculo del semáforo (R04). Esto coincide con la priorización de la "
    "Actividad 2, donde F02, F03 y F04 quedaron como los elementos prioritarios. Por eso, las pruebas "
    "empiezan por estas funcionalidades y continúan con los riesgos medios de las métricas, la "
    "exportación y la conservación de los datos.", P))

doc.build(s, onFirstPage=footer, onLaterPages=footer)
print("ok")
