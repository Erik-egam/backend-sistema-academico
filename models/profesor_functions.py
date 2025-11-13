from fastapi import HTTPException, status
from routes.usuarios import conexion, crypt
from models.Usuario import Usuario
from mysql.connector import IntegrityError
from models.Programa import Programa
from models.Asignatura import Asignatura_actual
from models.Semestre import Semestre
from datetime import datetime
from models.Notas import Notas


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
                    id_asignatura=asignatura[3],
                    codigo=str(asignatura[4]),
                    nombre=str(asignatura[5]),
                    creditos=int(asignatura[6]),
                    id_programa=int(asignatura[7]),
                    programa=str(asignatura[8])
                )
            )
        return lista_asignatura

    def estudiantes_curso(id_asignatura: int):
        cursor = conexion.cursor()
        estudiantes = []
        try:
            cursor.execute(
                """
                SELECT 
                    u.id_usuario,
                    u.nombre_usuario,
                    u.apellido_usuario,
                    u.email_usuario,
                    u.id_rol,
                    u.activo
                    FROM notas n
                    JOIN usuarios u ON u.id_usuario = n.id_estudiante
                    JOIN asignaturas a ON a.id_asignatura = n.id_asignatura
                    JOIN semestres s ON s.id_semestre = n.id_semestre
                    WHERE n.id_semestre = (SELECT MAX(id_semestre) FROM semestres)
                    AND n.id_asignatura = %s;
                """,(id_asignatura,)
                )
            resultado = cursor.fetchall()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error {e}"
            )
        for estudiante in resultado:
            estudiantes.append(
                Usuario(
                    id_usuario=estudiante[0],
                    nombre=estudiante[1],
                    apellido=estudiante[2],
                    email=estudiante[3],
                    id_rol=estudiante[4],
                    activo=estudiante[5]
                )
            )
        return estudiantes

    def notas_estudiante(id_estudiante: int, id_asignatura:int):
        cursor = conexion.cursor()
        try:
            cursor.execute(
                """
                select * from notas where id_estudiante=%s AND id_asignatura=%s 
                AND id_semestre=(SELECT MAX(id_semestre) FROM semestres);
                """, (id_estudiante,id_asignatura)
            )
            notas = cursor.fetchone()
            return Notas(
                nota1=notas[3],
                nota2=notas[4],
                nota3=notas[5],
                nota_final=notas[6],
                asistencia1=notas[7],
                asistencia2=notas[8],
                asistencia3=notas[9]
            )
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: {e}"
            )
    def registrar_notas(id_estudiante: int, id_asignatura:int, notas: Notas):
        cursor = conexion.cursor()
        try:
            cursor.execute(
                """
                    UPDATE notas SET nota1=%s, nota2=%s, nota3=%s, asistencia1=%s, asistencia2=%s, asistencia3=%s, nota_final=%s
                    WHERE id_estudiante=%s AND id_asignatura=%s AND id_semestre=(SELECT MAX(id_semestre) FROM semestres);
                """ ,(
                    notas.nota1, notas.nota2, notas.nota3,
                    notas.asistencia1, notas.asistencia2, notas.asistencia3,
                    notas.nota_final,
                    id_estudiante, id_asignatura
                    )
            )
            conexion.commit()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: {e}"
            )