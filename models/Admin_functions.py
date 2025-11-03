from fastapi import HTTPException, status
from routes.usuarios import conexion, crypt
from models.Usuario import UsuarioDB
from mysql.connector import IntegrityError
from models.Programa import Programa
from models.Asignatura import Asignatura
from models.Semestre import Semestre
from datetime import datetime


excepcion_campos = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Campo no admitido"
    )
class Admin_functions:
    # =================================
    #           CREACIONES
    # =================================
    
        
    def crear_usuario(nuevo_usuario: UsuarioDB):
        if not nuevo_usuario.id_usuario:
            raise excepcion_campos

        if not nuevo_usuario.nombre:
            raise excepcion_campos

        if not nuevo_usuario.apellido:
            raise excepcion_campos

        if not nuevo_usuario.email or "@ulibre.edu.co" not in nuevo_usuario.email:
            raise excepcion_campos

        if nuevo_usuario.id_programa and nuevo_usuario.id_rol == "ADMIN":
            raise excepcion_campos

        if not nuevo_usuario.activo:
            # el usuario debe estar activo
            raise excepcion_campos

        nuevo_usuario.password = nuevo_usuario.password or "12345"
        try:
            cursor = conexion.cursor()
            peticion = """
            INSERT INTO usuarios (
                id_usuario,
                nombre_usuario,
                apellido_usuario,
                email_usuario,
                password_hash,
                fecha_registro,
                id_programa,
                id_rol,
                activo
                )
            VALUES (%s,%s,%s,%s,%s,NOW(),%s,%s,%s);
            """ 
            cursor.execute(
                peticion, (
                    nuevo_usuario.id_usuario,
                    nuevo_usuario.nombre,
                    nuevo_usuario.apellido,
                    nuevo_usuario.email,
                    crypt.hash(nuevo_usuario.password),
                    nuevo_usuario.id_programa,
                    nuevo_usuario.id_rol,
                    True
                    )
            )
            conexion.commit()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: {e}"
            )
            
    def crear_programa(programa: Programa):
        try:
            cursor = conexion.cursor()
            peticion = """
            INSERT INTO programas (
                nombre_programa,
                descripcion_programa
                ) VALUES (%s,%s)
            """
            cursor.execute(
                peticion,
                (programa.nombre, programa.descripcion)
            )
            conexion.commit()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: {e}"
            )
            
    def crear_asignatura(asignatura: Asignatura):
        try:
            cursor = conexion.cursor()
            peticion = """
            INSERT INTO asignaturas (
                codigo,
                nombre,
                creditos,
                id_programa
                ) VALUES (%s,%s,%s,%s)
            """
            cursor.execute(
                peticion,
                (asignatura.codigo,asignatura.nombre,asignatura.creditos,asignatura.id_programa)
            )
            conexion.commit()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: {e}"
            )
    def crear_semestre(semestre: Semestre):
        try:
            cursor = conexion.cursor()
            peticion = """
            INSERT INTO semestres (
                nombre,
                fecha_inicio,
                fecha_fin
                ) VALUES (%s,%s,%s)
            """
            cursor.execute(
                peticion,
                (semestre.nombre, semestre.fecha_inicio, semestre.fecha_fin)
            )
            conexion.commit()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: {e}"
            )
    # ===============================
    #         ELIMINAR USUARIO
    # ===============================
    
    def dar_de_baja_usuario(id_usuario: int):
        try:
            cursor = conexion.cursor()
            peticion = """
            UPDATE usuarios SET activo=0 WHERE id_usuario=%s;
            """
            cursor.execute(peticion,(id_usuario,))
            conexion.commit()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: {e}"
            )
            
    # ===============================
    #         ACTIVAR USUARIO
    # ===============================
    def activar_usuario(id_usuario: int):
        try:
            cursor = conexion.cursor()
            peticion = """
            UPDATE usuarios SET activo=1 WHERE id_usuario=%s;
            """
            cursor.execute(peticion,(id_usuario,))
            conexion.commit()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: {e}"
            )
    
    def asignar_profesor_asignatura(id_profesor: int, id_asignatura: int, id_semestre: int):
        try:
            cursor = conexion.cursor()
            peticion = """
            UPDATE semestres_asignaturas SET id_profesor=%s WHERE id_semestre=%s AND id_asignatura=%s;
            """
            cursor.execute(peticion,(id_profesor,id_semestre, id_asignatura))
            conexion.commit()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: {e}"
            )
            
    def avilitar_asignatura(id_asignatura):
        try:
            cursor = conexion.cursor()
            cursor.execute(
                """
                INSERT INTO semestres_asignaturas (id_semestre, id_asignatura)
                VALUES (
                (SELECT MAX(id_semestre) FROM semestres), 2);
                """
            )
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error {e}"
            )