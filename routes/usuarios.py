from dotenv import load_dotenv
import os

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jose import JWTError, jwt, ExpiredSignatureError

from datetime import datetime, timedelta

from passlib.context import CryptContext

from models.config import crear_conexion
from models.Usuario import Usuario, UsuarioDB

router = APIRouter(
    prefix="/users",
    tags=["endpoint's para usuarios"]
    )
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
crypt = CryptContext(schemes=["bcrypt"])

load_dotenv()

"""
CREA UN ARCHIVO .env PARA CARGAR SUS CONFICORACIONES SIN TENERLAS EXPUESTAS
TAMBIEN PUEDEN HACERLO EN LA CONFIGURACION DE LA BASE DE DATOS EN MI CASO NO
PORQUE ME DA PEREZA.
"""

SECRET_KEY= os.getenv('SECRET_KEY')
ALGORITHM= os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES= int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
conexion = crear_conexion()

async def buscar_usuario_db(email:str) -> UsuarioDB:
    cursor = conexion.cursor()
    cursor.execute("select * from usuarios where email_usuario= %s;", (email,))
    usuario = cursor.fetchone()
    cursor.close()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuario no encontrado")
    resultado = UsuarioDB(
        id_usuario=usuario[0],
        nombre=usuario[1],
        apellido=usuario[2],
        email=usuario[3],
        password=usuario[4],
        fecha_registro=str(usuario[5]),
        id_programa=usuario[6],
        id_rol=usuario[7],
        activo=usuario[8]
    )
    return resultado

async def buscar_usuario(email:str) -> UsuarioDB:
    cursor = conexion.cursor()
    cursor.execute("select * from usuarios where email_usuario= %s;", (email,))
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
    
    

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    usuario = await buscar_usuario_db(form.username)
    print(usuario.email)
    
    
    if not crypt.verify(form.password, usuario.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Contraseña incorrecta"
        )
        
    access_token = jwt.encode({
        "sub": usuario.email,
        "rol": usuario.id_rol,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}

async def autenticar_usuario(token: str = Depends(oauth2)) -> Usuario:
    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales invalidas",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )
    try:
        email = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
        if not email:
            raise exception
        
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El token ha expirado, inicia sesion nuevamente",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )
        
    except JWTError:
        raise exception
    
    usuario = await buscar_usuario(email=email)
    
    if not usuario.activo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario no esta activo"
        )
    return usuario 

@router.get("/me")
async def usuario_actual(usuario: Usuario = Depends(autenticar_usuario)):
    return usuario