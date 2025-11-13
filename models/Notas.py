from pydantic import BaseModel
from typing import Optional

class Notas(BaseModel):
    asignatura: Optional[str] = None
    nota1: float
    asistencia1: Optional[int] = None
    nota2: float
    asistencia2: Optional[int] = None
    nota3: float
    asistencia3: Optional[int] = None
    nota_final: Optional[float] = None