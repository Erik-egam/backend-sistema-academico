from pydantic import BaseModel
from typing import Optional

class Nota(BaseModel):
    semestre: str
    asignatura: str
    nota1: float
    asistencia1: Optional[int] = None
    nota2: float
    asistencia2: Optional[int] = None
    nota3: float
    asistencia3: Optional[int] = None
    nota_final: Optional[float]