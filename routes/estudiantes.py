from fastapi import APIRouter, Depends, HTTPException, status
from models.Usuario import Usuario
from models.estudiantes_functions import estudiantes_functions
from models.Admin_functions import Admin_functions
from routes.usuarios import autenticar_usuario

router = APIRouter(
    prefix="/estudiante",
    tags=["Estudiante"]
)

def usuario_estuadiante(rol: str):
    if not rol == "EST":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no autorizado para hacer esta accion",
            headers={
                "WWW-authenticate": "Bearer"
            }
        )

@router.get("/semestres")
async def historico_semestres(usuario: Usuario = Depends(autenticar_usuario)):
    usuario_estuadiante(usuario.id_rol)
    return estudiantes_functions.semestres_estudiantes(usuario.id_usuario)

@router.get("/semestres/notas/{id_semestre}")
async def historico_semestres(id_semestre: int,usuario: Usuario = Depends(autenticar_usuario)):
    usuario_estuadiante(usuario.id_rol)
    return estudiantes_functions.notas_semestres_estudiantes(id_semestre,usuario.id_usuario)

@router.put("/matricular/{id_asignatura}")
async def matricular_asignatura(id_asignatura: int, usuario: Usuario = Depends(autenticar_usuario)):
    usuario_estuadiante(usuario.id_rol)
    estudiantes_functions.matricular_asignatura(usuario.id_usuario, id_asignatura)
    return {
        "mensaje": "matriculado en asignatura correctamente correctamente"
    }

@router.get("/asignaturas/matriculadas")
async def asignaturas_matriculadas(usuario: Usuario = Depends(autenticar_usuario)):
    usuario_estuadiante(usuario.id_rol)
    return estudiantes_functions.asignaturas_matriculadas(usuario.id_usuario)

@router.get("/asignaturas/disponibles")
async def asignaturas_matriculadas(usuario: Usuario = Depends(autenticar_usuario)):
    usuario_estuadiante(usuario.id_rol)
    return Admin_functions.listar_asignaturas_programa(usuario.id_programa)