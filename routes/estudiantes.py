from fastapi import APIRouter, Depends, HTTPException, status
from models.Usuario import Usuario
from models.estudiantes_functions import estudiantes_functions
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

@router.get("/notas")
async def historico_notas(usuario: Usuario = Depends(autenticar_usuario)):
    usuario_estuadiante(usuario.id_rol)
    return estudiantes_functions.historico_notas(usuario.id_usuario)

@router.post("/matricular/{id_asignatura}")
async def matricular_asignatura(id_asignatura: int, usuario: Usuario = Depends(autenticar_usuario)):
    usuario_estuadiante(usuario.id_rol)
    estudiantes_functions.matricular_asignatura(id_asignatura=id_asignatura,id_estudiante=usuario.id_usuario)
    return {
        "mensaje": "matriculado en asignatura correctamente correctamente"
    }