from fastapi import HTTPException, status
from routes.usuarios import conexion
from mysql.connector import IntegrityError
from models.Semestre import Semestre
from models.Notas import Notas
from models.Asignatura import Asignatura


class estudiantes_functions:
    def matricular_asignatura(id_estudiante, id_asignatura):
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "INSERT INTO notas (id_estudiante,id_semestre,id_asignatura) SELECT %s, MAX(id_semestre), %s FROM semestres;",
                (id_estudiante,id_asignatura)
            )
            conexion.commit()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: {e}"
            )
    def semestres_estudiantes(id_estudiante: int):
        semestres = []
        cursor = conexion.cursor()
        try:
            cursor.execute(
                """SELECT DISTINCT s.id_semestre, s.nombre, s.fecha_inicio, s.fecha_fin FROM semestres s 
                JOIN notas n ON s.id_semestre=n.id_semestre WHERE n.id_estudiante=%s ORDER BY s.id_semestre DESC;""", (id_estudiante,)
            )
            resultado = cursor.fetchall()
            cursor.close()
            
            for semestre in resultado:
                semestres.append(
                    Semestre(
                        id_semestre=semestre[0],
                        nombre=semestre[1],
                        fecha_inicio=str(semestre[2]),
                        fecha_fin=str(semestre[3])
                    )
                )
            return semestres


        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: {e}"
            )

    def notas_semestres_estudiantes(id_semestre: int,id_estudiante: int):
        notas = []
        cursor = conexion.cursor()
        try:
            cursor.execute(
                """SELECT * FROM notas n 
                JOIN asignaturas a ON n.id_asignatura=a.id_asignatura 
                WHERE n.id_semestre=%s AND n.id_estudiante=%s;""", (id_semestre,id_estudiante)
            )
            resultado = cursor.fetchall()
            cursor.close()
            
            for nota in resultado:
                notas.append(
                    Notas(
                        asignatura=nota[-3],
                        nota1=nota[3],
                        nota2=nota[4],
                        nota3=nota[5],
                        nota_final=nota[6],
                        asistencia1=nota[7],
                        asistencia2=nota[8],
                        asistencia3=nota[9],
                    )
                )
            return notas


        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: {e}"
            )

    def asignaturas_matriculadas(id_estudiante: int):
        asignaturas = []
        cursor = conexion.cursor()
        try:
            cursor.execute(
                """SELECT * FROM notas n 
                JOIN asignaturas a ON n.id_asignatura=a.id_asignatura 
                WHERE n.id_estudiante=%s AND n.id_semestre=(SELECT MAX(id_semestre) FROM semestres);""", (id_estudiante,)
            )
            resultado = cursor.fetchall()
            cursor.close()
            
            for asignatura in resultado:
                asignaturas.append(
                    Asignatura(
                        id_asignatura=asignatura[-5],
                        codigo=asignatura[-4],
                        nombre=asignatura[-3],
                        creditos=asignatura[-2],
                        id_programa=asignatura[-1]
                    )
                )
            return asignaturas


        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: {e}"
            )