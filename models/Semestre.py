from pydantic import BaseModel
from typing import Optional

class Semestre(BaseModel):
    nombre: str
    fecha_inicio: str
    fecha_fin: str