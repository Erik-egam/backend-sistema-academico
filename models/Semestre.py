from pydantic import BaseModel
from typing import Optional

class Semestre(BaseModel):
    id_semestre: Optional[int] = None
    nombre: str
    fecha_inicio: str
    fecha_fin: str

