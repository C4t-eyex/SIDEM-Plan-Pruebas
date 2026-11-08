"""
Datos ficticios de la demo de SIDEM (conjunto DAT-01 del plan de pruebas).

Se ejecuta dentro del contenedor, desde la carpeta de SIDEM, y usa sus propios
modelos y servicios. Es idempotente: si los datos ya existen no los duplica.

Ningún dato corresponde a personas reales. Los correos usan el dominio
reservado .test, que no existe en internet.
"""
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SessionLocal
from models import Usuario, Role, PermisoRol, Curso, Revision, ResultadoRevision
from services.auth_service import hash_password
from services.permisos_service import sembrar_roles_legacy
from services.config_service import sembrar_configuraciones_iniciales
from services.etl_actividad import periodo_actual
from scripts.inicializar_criterios import inicializar_criterios

PASSWORD = os.getenv("DEMO_PASSWORD", "Demo-SIDEM-2026")
PERIODO = periodo_actual()

# ── Usuarios de prueba (uno por cada situación que piden los casos) ───────────
# (correo, nombre, rol, departamento)
USUARIOS = [
    ("superadmin@sidem.test",   "Superadmin Demo",               "superadmin",         None),
    ("admin@sidem.test",        "Administrador Demo",            "admin",              None),
    ("revisor.sd@sidem.test",   "Revisora Sistemas (ficticia)",  "revisor",            None),
    ("revisor.pr@sidem.test",   "Revisor Producción (ficticio)", "revisor",            None),
    ("lider@sidem.test",        "Líder Académico Demo",          "lider",              None),
    ("lider.sd@sidem.test",     "Líder Sistemas Digitales Demo", "lider_departamento", "Sistemas Digitales"),
    ("lider.sindep@sidem.test", "Líder sin Departamento Demo",   "lider_departamento", None),
    ("consulta@sidem.test",     "Usuario Solo Consulta Demo",    "consulta",           None),
]

# Rol personalizado de solo consulta: ve el seguimiento pero no puede guardar.
PERMISOS_CONSULTA = {"dashboard": "vista", "seguimiento": "vista", "metricas": "vista",
                     "metricas_docentes": "vista"}

# ── Cursos y resultados de la revisión 1 ─────────────────────────────────────
# Criterios de la revisión 1 y su peso (services/criterios_config.py):
#   1→5, 2→5, 3→7, 4→5, 6→6, 7→2  (total 30)
# El % del semáforo es ponderado: peso cumplido / peso evaluado.
# Los cumplidos se eligieron para caer justo en los límites de 80 % y 50 %.
CRITERIOS_R1 = [1, 2, 3, 4, 6, 7]

# (id_curso, departamento, prefijo, nombre, docente, encargado, criterios cumplidos, % esperado)
CURSOS = [
    (900101, "Sistemas Digitales", "SD", "Programación Básica (DEMO)",  ("Ana", "Ríos"),     "revisor.sd@sidem.test", [1, 2, 3, 4, 7],    80),   # verde (límite)
    (900102, "Sistemas Digitales", "SD", "Bases de Datos (DEMO)",       ("Bruno", "Mesa"),   "revisor.sd@sidem.test", [1, 2, 4, 6, 7],    77),   # amarillo (justo debajo)
    (900103, "Sistemas Digitales", "SD", "Redes I (DEMO)",              ("Carla", "Uribe"),  "revisor.sd@sidem.test", [1, 2, 4],          50),   # amarillo (límite)
    (900201, "Producción",         "PR", "Procesos Industriales (DEMO)", ("Diego", "Lara"),  "revisor.pr@sidem.test", [1, 3, 7],          47),   # rojo (justo debajo)
    (900202, "Producción",         "PR", "Calidad (DEMO)",              ("Elena", "Patiño"), "revisor.pr@sidem.test", CRITERIOS_R1,       100),  # verde
    (900203, "Producción",         "PR", "Logística (DEMO)",            ("Fabio", "Gil"),    "revisor.pr@sidem.test", [],                 0),    # rojo
]


def crear_usuarios(db) -> dict:
    """Crea los usuarios que falten y devuelve {correo: usuario}."""
    hash_ = hash_password(PASSWORD)
    resultado = {}
    for correo, nombre, rol, depto in USUARIOS:
        usuario = db.query(Usuario).filter(Usuario.email == correo).first()
        if not usuario:
            usuario = Usuario(nombre=nombre, email=correo, password=hash_, rol=rol,
                              departamento=depto, activo=True)
            db.add(usuario)
            db.commit()
            db.refresh(usuario)
        resultado[correo] = usuario
    return resultado


def crear_rol_consulta(db) -> None:
    if db.query(Role).filter(Role.nombre == "consulta").first():
        return
    rol = Role(nombre="consulta", protegido=False, color="#64748b")
    db.add(rol)
    db.commit()
    db.refresh(rol)
    for modulo, nivel in PERMISOS_CONSULTA.items():
        db.add(PermisoRol(rol_id=rol.id, modulo=modulo, nivel=nivel))
    db.commit()


def crear_cursos(db, usuarios: dict) -> None:
    for id_curso, depto, prefijo, nombre, (dn, da), encargado, cumplidos, _ in CURSOS:
        if db.query(Curso).filter(Curso.id_curso == id_curso, Curso.periodo == PERIODO).first():
            continue
        enc = usuarios[encargado]
        correo_docente = f"{dn.lower()}.{da.lower()}@docente.sidem.test"
        curso = Curso(id_curso=id_curso, periodo=PERIODO, grupo="G1", departamento=depto,
                      prefijo=prefijo, nombre_curso=nombre, docente_nombre=dn,
                      docente_apellido=da, docente_correo=correo_docente,
                      encargado_id=enc.id, tipo_seguimiento="virtualidad",
                      evaluacion_automatica=False)
        db.add(curso)
        db.commit()
        db.refresh(curso)
        revision = Revision(curso_id=curso.id, revision_numero=1, fecha_revision=date.today(),
                            encargado_id=enc.id, docente_nombre=dn, docente_apellido=da,
                            docente_correo=correo_docente, revisado=True)
        db.add(revision)
        db.commit()
        db.refresh(revision)
        for criterio_id in CRITERIOS_R1:
            db.add(ResultadoRevision(revision_id=revision.id, criterio_id=criterio_id,
                                     cumplido=criterio_id in cumplidos))
        db.commit()


def main() -> None:
    db = SessionLocal()
    try:
        inicializar_criterios(db)
        sembrar_roles_legacy(db)
        crear_rol_consulta(db)
        usuarios = crear_usuarios(db)
        sembrar_configuraciones_iniciales(db, usuarios["superadmin@sidem.test"].id)
        crear_cursos(db, usuarios)
        print(f"[demo] Datos listos: {len(USUARIOS)} usuarios, {len(CURSOS)} cursos, periodo {PERIODO}.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
