from fastapi import APIRouter, Depends, HTTPException, status
from models.Usuario import Usuario, UsuarioDB
from models.Programa import Programa
from models.Admin_functions import Admin_functions
from models.Asignatura import Asignatura
from models.Semestre import Semestre
from routes.usuarios import autenticar_usuario, conexion, crypt
from mysql.connector import IntegrityError

router = APIRouter(
    prefix="/admin",
    tags=["administrador"]
)

def usuario_admin(rol: str):
    if not rol == "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no autorizado para hacer esta accion",
            headers={
                "WWW-authenticate": "Bearer"
            }
        )
#  ============================
#         CRUDS ADMIN
#  ============================



@router.post("/registrar/estudiante", status_code=status.HTTP_201_CREATED)
async def registrar_usuario(nuevo_usuario: UsuarioDB, usuario: Usuario = Depends(autenticar_usuario)):
    usuario_admin(usuario.id_rol)
    Admin_functions.crear_usuario(nuevo_usuario)
    return {
        "mensaje": "Usuario creado correctamente"
    }

@router.post("/registrar/programa", status_code=status.HTTP_201_CREATED)
async def registrar_programa(programa: Programa, usuario: Usuario = Depends(autenticar_usuario)):
    usuario_admin(usuario.id_rol)
    Admin_functions.crear_programa(programa)
    
    return {
        "mensaje": "Programa creado correctamente"
    }
    
@router.post("/registrar/asignatura", status_code=status.HTTP_201_CREATED)
async def registrar_asignatura(asignatura: Asignatura, usuario: Usuario = Depends(autenticar_usuario)):
    usuario_admin(usuario.id_rol)
    Admin_functions.crear_asignatura(asignatura)
    return {
        "mensaje": "Asignatura creado correctamente"
    }

@router.post("/registrar/semestre", status_code=status.HTTP_201_CREATED)
async def registrar_semestre(semestre: Semestre, usuario: Usuario = Depends(autenticar_usuario)):
    usuario_admin(usuario.id_rol)
    Admin_functions.crear_semestre(semestre)
    return {
        "mensaje": "Semestre creado correctamente"
    }
    
@router.put("/eliminar/usuario/{id}", status_code=status.HTTP_202_ACCEPTED)
async def eliminar_usuario(id, usuario: Usuario = Depends(autenticar_usuario)):
    usuario_admin(usuario.id_rol)
    Admin_functions.dar_de_baja_usuario(id)
    return {
        "mensaje": "Usuario eliminado correctamente"
    }
    
@router.put("/activar/usuario/{id}", status_code=status.HTTP_202_ACCEPTED)
async def activar_usuario(id, usuario: Usuario = Depends(autenticar_usuario)):
    usuario_admin(usuario.id_rol)
    Admin_functions.activar_usuario(id)
    return {
        "mensaje": "Usuario activado correctamente"
    }