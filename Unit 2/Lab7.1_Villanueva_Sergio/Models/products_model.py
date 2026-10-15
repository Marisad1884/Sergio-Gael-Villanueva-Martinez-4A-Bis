from Controller.database_connection import Database_connection


class Product:
    def __init__(self, id=None, nombre=None, precio=None, stock=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.db = Database_connection()

    def get_products(self):
        """Devuelve la lista de productos (diccionarios) o None si hubo un error."""
        query = (
            "SELECT id_product, nombre, precio, stock "
            "FROM products ORDER BY id_product"
        )
        return self.db.ejecutar_consulta(query)

    def save(self):
        """Inserta este producto en la base de datos. Devuelve True/False."""
        query = "INSERT INTO products (nombre, precio, stock) VALUES (%s, %s, %s)"
        return self.db.ejecutar_comando(query, (self.nombre, self.precio, self.stock))
