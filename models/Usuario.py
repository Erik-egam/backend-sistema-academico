from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id_usuario: Optional[int] = None
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[str] = None
    fecha_registro: Optional[str] = None
    id_programa: Optional[int] = None
    id_rol: Optional[str] = 'EST'
    activo: Optional[bool] = True

class UsuarioDB(Usuario):
    password: Optional[str] = None