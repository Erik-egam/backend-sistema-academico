from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jose import JWTError, jwt, ExpiredSignatureError

from datetime import datetime, timedelta

from passlib.context import CryptContext

from models.config import crear_conexion
from models.Usuario import Usuario, UsuarioDB


router = APIRouter(
    prefix="admin",
    tags=["administrador"]
)
#  ============================
#         CRUDS ADMIN
#  ============================

@router.post("/registrar")
async def registrar_usuario(user: Usuario):
    return {
        "data": Usuario
    }