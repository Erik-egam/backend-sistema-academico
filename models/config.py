import mysql.connector
from mysql.connector import Error

class ConfiguracionBaseDeDatos:
    HOST = "localhost"
    USER = "root"
    PASSWORD = ""
    DATABASE = "sistema_academico"
    
def crear_conexion():
    conexion = None
    try:
        conexion = mysql.connector.connect(
            host=ConfiguracionBaseDeDatos.HOST,
            user=ConfiguracionBaseDeDatos.USER,
            password=ConfiguracionBaseDeDatos.PASSWORD,
            database=ConfiguracionBaseDeDatos.DATABASE
        )
        print("✅ conexion a la Base de datos Exitosa")
    except Error as e:
        print(f"❌ Error: {e}")
    return conexion