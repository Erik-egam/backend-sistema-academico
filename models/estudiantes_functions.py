from fastapi import HTTPException, status
from routes.usuarios import conexion, crypt
from models.Usuario import Usuario
from mysql.connector import IntegrityError
from models.Programa import Programa
from models.Asignatura import Asignatura
from models.Semestre import Semestre
from datetime import datetime
from models.Notas import Nota


class estudiantes_functions:
    def historico_notas(id_estudiate: int) -> list[Usuario]:
        cursor = conexion.cursor()
        try:
            cursor.execute(
                """
                SELECT * FROM notas n
                JOIN semestres s ON n.id_semestre=s.id_semestre
                JOIN asignaturas a ON n.id_asignatura=a.id_asignatura
                WHERE n.id_estudiante=%s ORDER BY n.id_semestre DESC;
                """,
                (id_estudiate,)
            )
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error {e}"
            )
        notas = cursor.fetchall()
        lista_notas = []
        for n in notas:
            lista_notas.append(
                Nota(
                    nota1=float(n[3]),
                    nota2=float(n[4]),
                    nota3=float(n[6]),
                    nota_final=float(n[7]),
                    asistencia1=int(n[8]),
                    asistencia2=int(n[9]),
                    asistencia3=int(n[10]),
                    semestre=str(n[11]),
                    asignatura=str(n[-3])
                )
            )
        return lista_notas
    def matricular_asignatura(id_estudiante, id_asignatura):
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "INSERT INTO notas (id_estudiante,id_semestre,id_asignatura) SELECT %s, MAX(id_semestre), %s FROM semestres;",
                (id_estudiante,id_asignatura)
            )
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: {e}"
            )