from fastapi import APIRouter, Depends, HTTPException, status
from models.Usuario import Usuario
from models.profesor_functions import profesor_functions 
from routes.usuarios import autenticar_usuario
from models.Notas import Notas

router = APIRouter(
    prefix="/profesor",
    tags=["Profesor"]
)

def usuario_profesor(rol: str):
    if not rol == "PROF":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no autorizado para hacer esta accion",
            headers={
                "WWW-authenticate": "Bearer"
            }
        )
    
@router.get("/cursos")
def cursos_actuales(usuario: Usuario = Depends(autenticar_usuario)):
    usuario_profesor(usuario.id_rol)
    return profesor_functions.cursos_actuales(usuario.id_usuario)
    
@router.get("/estudiantes/asignatura/{id_asignatura}")
def estudiantes_curso(id_asignatura: int, usuario: Usuario = Depends(autenticar_usuario)):
    usuario_profesor(usuario.id_rol)
    return profesor_functions.estudiantes_curso(id_asignatura=id_asignatura)

@router.get("/notas/estudiante/{id_estudiante}/asignatura/{id_asignatura}")
async def notas_estudiante(id_estudiante: int, id_asignatura:int, usuario: Usuario = Depends(autenticar_usuario)):
    usuario_profesor(usuario.id_rol)
    return profesor_functions.notas_estudiante(id_estudiante, id_asignatura)

@router.post("/registar/notas/estudiante/{id_estudiante}/asignatura/{id_asignatura}")
async def notas_estudiante(id_estudiante: int, id_asignatura:int, notas: Notas, usuario: Usuario = Depends(autenticar_usuario)):
    usuario_profesor(usuario.id_rol)
    if not notas.asistencia1: notas.asistencia1 = 0
    if not notas.asistencia2: notas.asistencia2 = 0
    if not notas.asistencia3: notas.asistencia3 = 0
    notas.nota_final = notas.nota1 * 0.3 + notas.nota2 * 0.3 + notas.nota3 * 0.4
    return profesor_functions.registrar_notas(id_estudiante, id_asignatura, notas)