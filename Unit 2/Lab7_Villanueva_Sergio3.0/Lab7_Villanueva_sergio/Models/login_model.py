import hashlib
from Controller.database_connection import Database_connection


class User:
    def __init__(self, username, passw):
        self.username = username
        self.password = passw
        self.db = Database_connection()

    @staticmethod
    def _hash(texto):
        return hashlib.sha256(texto.encode("utf-8")).hexdigest()

    def auth(self):
        query = (
            "SELECT id_user, username, nombre "
            "FROM users WHERE username = %s AND password = %s"
        )
        return self.db.ejecutar_consulta(
            query, (self.username, self._hash(self.password))
        )
