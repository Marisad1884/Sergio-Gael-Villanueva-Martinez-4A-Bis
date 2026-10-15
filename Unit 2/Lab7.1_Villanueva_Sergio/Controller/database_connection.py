import mysql.connector
from mysql.connector import Error
from Controller.config import DB_config


class Database_connection:
    def __init__(self):
        self.config = DB_config

    def get_connection(self):
        try:
            conexion = mysql.connector.connect(**self.config)
            if conexion.is_connected():
                return conexion
        except Error as e:
            print(f"Error al conectar con MySQL: {e}")
        return None

    def ejecutar_consulta(self, query, params=()):
        """Ejecuta un SELECT y devuelve una lista de diccionarios.
        Devuelve None si hubo un error de conexión o de SQL."""
        conexion = self.get_connection()
        if not conexion:
            return None

        cursor = conexion.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"Error en la consulta SQL: {e}")
            return None
        finally:
            cursor.close()
            if conexion.is_connected():
                conexion.close()

    def ejecutar_comando(self, query, params=()):
        """Ejecuta un INSERT / UPDATE / DELETE y confirma la transacción.
        Devuelve True si todo salió bien, False si hubo un error."""
        conexion = self.get_connection()
        if not conexion:
            return False

        cursor = conexion.cursor()
        try:
            cursor.execute(query, params)
            conexion.commit()
            return True
        except Error as e:
            conexion.rollback()
            print(f"Error al ejecutar el comando SQL: {e}")
            return False
        finally:
            cursor.close()
            if conexion.is_connected():
                conexion.close()
