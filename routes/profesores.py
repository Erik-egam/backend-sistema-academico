from fastapi import APIRouter, Depends, HTTPException, status
from models.Usuario import Usuario
from models.profesor_functions import profesor_functions 
from routes.usuarios import autenticar_usuario

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
    