from fastapi import APIRouter, Depends, HTTPException, status
from models.Usuario import Usuario, UsuarioDB
from models.Programa import Programa
from models.Admin_functions import Admin_functions
from models.Asignatura import Asignatura
from models.Semestre import Semestre
from routes.usuarios import autenticar_usuario, buscar_usuario,conexion
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



@router.post("/registrar/usuario", status_code=status.HTTP_201_CREATED)
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
    
async def buscar_usuario_id(id_usuario:int):
    cursor = conexion.cursor()
    cursor.execute("select * from usuarios where id_usuario= %s;", (id_usuario,))
    usuario = cursor.fetchone()
    cursor.close()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuario no encontrado")
    resultado = Usuario(
        id_usuario=usuario[0],
        nombre=usuario[1],
        apellido=usuario[2],
        email=usuario[3],
        fecha_registro=str(usuario[5]),
        id_programa=usuario[6],
        id_rol=usuario[7],
        activo=usuario[8]
    )
    return resultado
        

@router.put("/asignar/profesor/{id_profesor}/asignatura/{id_asignatura}", status_code=status.HTTP_202_ACCEPTED)
async def asignar_profesor(id_profesor:int,id_asignatura:int, usuario: Usuario = Depends(autenticar_usuario)):
    usuario_admin(usuario.id_rol)
    profesor = await buscar_usuario_id(id_profesor)
    if profesor.id_rol != "PROF":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no es profesor"
        )
    Admin_functions.asignar_profesor_asignatura(id_profesor,id_asignatura)
    return {
        "mensaje": "Profesor asignado correctamente"
    }
    
@router.put("/avilitar/asignatura/{id_asignatura}")
async def avalitar_asignatura(id_asignatura: int, usuario: Usuario = Depends(autenticar_usuario)):
    usuario_admin(usuario.id_rol)
    Admin_functions.avilitar_asignatura(id_asignatura=id_asignatura)
    return {
        "mensaje": "Asignatura avalitada correctamente"
    }
    
@router.get('/programas')
def lista_programas(usuario: Usuario = Depends(autenticar_usuario)):
    usuario_admin(usuario.id_rol)
    return Admin_functions.listar_programas()

@router.get('/programa/profesores/{id_programa}')
def lista_profesores_programa(id_programa: int, usuario : Usuario = Depends(autenticar_usuario)):
    usuario_admin(usuario.id_rol)
    return Admin_functions.listar_profesores_programa(id_programa)

@router.get('/programa/estudiantes/{id_programa}')
def lista_profesores_programa(id_programa: int, usuario : Usuario = Depends(autenticar_usuario)):
    usuario_admin(usuario.id_rol)
    return Admin_functions.listar_estudiantes_programa(id_programa)


@router.get('/programa/asignaturas/{id_programa}')
def listar_asignaturas_programa(id_programa: int, usuario : Usuario = Depends(autenticar_usuario)):
    usuario_admin(usuario.id_rol)
    return Admin_functions.listar_asignaturas_programa(id_programa=id_programa)

@router.get('/programa/asignaturas/{id_programa}/todas')
def listar_asignaturas_programa(id_programa: int, usuario : Usuario = Depends(autenticar_usuario)):
    usuario_admin(usuario.id_rol)
    return Admin_functions.listar_asignaturas_programa_todas(id_programa=id_programa)

@router.get('/profesor/asignaturas/{id_profesor}')
def listar_asignaturas_programa(id_profesor: int, usuario : Usuario = Depends(autenticar_usuario)):
    usuario_admin(usuario.id_rol)
    return Admin_functions.listar_asignaturas_profesor(idProfesor=id_profesor)

