from Controller.database_connection import Database_connection


class Product:
    def __init__(self):
        self.db = Database_connection()

    def get_all(self):
        """Devuelve todos los productos como lista de diccionarios,
        o None si hubo un error de conexión o de SQL."""
        query = (
            "SELECT id_producto, nombre, precio, stock "
            "FROM productos ORDER BY id_producto"
        )
        return self.db.ejecutar_consulta(query)
