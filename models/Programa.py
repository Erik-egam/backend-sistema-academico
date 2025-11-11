from pydantic import BaseModel
from typing import Optional

class Programa(BaseModel):
    nombre: str
    descripcion: str

class InfoPrograma(Programa):
    id:int