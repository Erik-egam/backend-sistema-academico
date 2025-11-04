from fastapi import HTTPException, status
from routes.usuarios import conexion, crypt
from models.Usuario import Usuario
from mysql.connector import IntegrityError
from models.Programa import Programa
from models.Asignatura import Asignatura_actual
from models.Semestre import Semestre
from datetime import datetime
from models.Notas import Nota


class profesor_functions:
    def cursos_actuales(id_profesor: int):
        cursor = conexion.cursor()
        try:
            cursor.execute(
                """SELECT * FROM semestres_asignaturas sa
                JOIN asignaturas s ON sa.id_asignatura=s.id_asignatura
                JOIN programas p ON p.id_programa=s.id_programa 
                WHERE id_semestre=(SELECT MAX(id_semestre) FROM semestres) AND id_profesor=%s;""",
                (id_profesor,)
            )
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error {e}"
            )
        asignaturas = cursor.fetchall()
        lista_asignatura = []
        for asignatura in asignaturas:
            lista_asignatura.append(
                Asignatura_actual(
                    codigo=str(asignatura[4]),
                    nombre=str(asignatura[5]),
                    creditos=int(asignatura[6]),
                    id_programa=int(asignatura[7]),
                    programa=str(asignatura[8])
                )
            )
        return lista_asignatura