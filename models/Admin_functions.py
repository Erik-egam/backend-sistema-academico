from fastapi import HTTPException, status
from routes.usuarios import conexion, crypt
from models.Usuario import UsuarioDB, Usuario
from mysql.connector import IntegrityError
from models.Programa import Programa, InfoPrograma
from models.Asignatura import Asignatura
from models.Semestre import Semestre


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
                (asignatura.codigo, asignatura.nombre,
                asignatura.creditos, asignatura.id_programa)
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
            cursor.execute(peticion, (id_usuario,))
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
            cursor.execute(peticion, (id_usuario,))
            conexion.commit()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: {e}"
            )

    def asignar_profesor_asignatura(id_profesor: int, id_asignatura: int):
        try:
            cursor = conexion.cursor()
            peticion = """
            UPDATE semestres_asignaturas SET id_profesor=%s WHERE id_semestre=(SELECT MAX(id_semestre) from semestres) AND id_asignatura=%s;
            """
            cursor.execute(peticion, (id_profesor, id_asignatura))
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
                (SELECT MAX(id_semestre) FROM semestres), %s);
                """,(id_asignatura,)
            )
            conexion.commit()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error {e}"
            )

    def listar_programas():
        listaProgramas = []
        try:
            cursor = conexion.cursor()
            cursor.execute(
                """
                select * from programas;
                """
            )
            programas = cursor.fetchall()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error {e}"
            )
        for programa in programas:
            # print(programa)
            listaProgramas.append(
                InfoPrograma(
                    id=programa[0],
                    nombre=programa[1],
                    descripcion=programa[2],
                )
            )
        return listaProgramas

    def listar_profesores_programa(id_programa):
        lista_profesores = []
        try:
            cursor = conexion.cursor()
            cursor.execute(
                """
                select * from usuarios WHERE id_rol='PROF' AND id_programa=%s;
                """, (id_programa,)
            )
            profesores = cursor.fetchall()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error {e}"
            )
        for profesor in profesores:
            # print(programa)
            lista_profesores.append(
                Usuario(
                    id_usuario=profesor[0],
                    nombre=profesor[1],
                    apellido=profesor[2],
                    email=profesor[3],
                    fecha_registro=str(profesor[5]),
                    id_programa=int(profesor[6]),
                    id_rol=profesor[7],
                    activo=profesor[8],
                )

            )
        return lista_profesores

    def listar_estudiantes_programa(id_programa):
        lista_estudiantes = []
        try:
            cursor = conexion.cursor()
            cursor.execute(
                """
                select * from usuarios WHERE id_rol='EST' AND id_programa=%s;
                """, (id_programa,)
            )
            estudiantes = cursor.fetchall()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error {e}"
            )
        for estudiante in estudiantes:
            # print(programa)
            lista_estudiantes.append(
                Usuario(
                    id_usuario=estudiante[0],
                    nombre=estudiante[1],
                    apellido=estudiante[2],
                    email=estudiante[3],
                    fecha_registro=str(estudiante[5]),
                    id_programa=int(estudiante[6]),
                    id_rol=estudiante[7],
                    activo=estudiante[8],
                )

            )
        return lista_estudiantes

    def listar_asignaturas_programa(id_programa):
        lista_asignaturas = []
        try:
            cursor = conexion.cursor()
            cursor.execute(
                """
                SELECT * FROM semestres_asignaturas sa 
                JOIN asignaturas a on sa.id_asignatura=a.id_asignatura 
                WHERE id_semestre = (SELECT MAX(id_semestre) FROM semestres) AND id_programa=%s;                
                """, (id_programa,)
            )
            asignaturas = cursor.fetchall()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error {e}"
            )
        for asignatura in asignaturas:
            # print(programa)
            lista_asignaturas.append(
                Asignatura(
                    id_asignatura=asignatura[1],
                    codigo=asignatura[4],
                    nombre=asignatura[5],
                    creditos=asignatura[6],
                    id_programa=asignatura[7]
                )
            )
        return lista_asignaturas
    
    def listar_asignaturas_programa_todas(id_programa):
        lista_asignaturas = []
        try:
            cursor = conexion.cursor()
            cursor.execute(
                """
                SELECT * FROM asignaturas Where id_programa=%s;                
                """, (id_programa,)
            )
            asignaturas = cursor.fetchall()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error {e}"
            )
        for asignatura in asignaturas:
            # print(programa)
            lista_asignaturas.append(
                Asignatura(
                    id_asignatura=asignatura[0],
                    codigo=asignatura[1],
                    nombre=asignatura[2],
                    creditos=int(asignatura[3]),
                    id_programa=int(asignatura[4])
                )
            )
        return lista_asignaturas


    def listar_asignaturas_profesor(idProfesor):
        lista_asignaturas = []
        try:
            cursor = conexion.cursor()
            cursor.execute(
                """
                SELECT * FROM semestres_asignaturas sa 
                JOIN asignaturas a on sa.id_asignatura=a.id_asignatura 
                WHERE id_semestre = (SELECT MAX(id_semestre) FROM semestres) AND id_profesor=%s;                
                """, (idProfesor,)
            )
            asignaturas = cursor.fetchall()
            cursor.close()
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error {e}"
            )
        for asignatura in asignaturas:
            # print(programa)
            lista_asignaturas.append(
                Asignatura(
                    id_asignatura=asignatura[1],
                    codigo=asignatura[4],
                    nombre=asignatura[5],
                    creditos=asignatura[6],
                    id_programa=asignatura[7]
                )
            )
        return lista_asignaturas
