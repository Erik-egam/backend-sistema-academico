from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id_usuario: int
    nombre: str
    apellido: str
    email: str
    fecha_registro: str
    id_programa: Optional[int] = None
    id_rol: str
    activo: bool

class UsuarioDB(Usuario):
    password: str