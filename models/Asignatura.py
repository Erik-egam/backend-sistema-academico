from pydantic import BaseModel
from typing import Optional

class Asignatura(BaseModel):
    codigo:str
    nombre: str
    creditos: int
    id_programa: int
    
class Asignatura_actual(Asignatura):
    programa: str