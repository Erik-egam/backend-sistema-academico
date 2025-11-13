from pydantic import BaseModel
from typing import Optional

class Nota(BaseModel):
    asignatura: str
    nota1: float
    asistencia1: Optional[int] = 0
    nota2: float
    asistencia2: Optional[int] = 0
    nota3: float
    asistencia3: Optional[int] = 0
    nota_final: Optional[float] = 0.0