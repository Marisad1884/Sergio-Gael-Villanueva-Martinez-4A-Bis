import tkinter as tk
from tkinter import messagebox

from models.conexion import Conexion
from models.user_model import UserModel
from views.login_view import LoginView
from controllers.auth_controller import Authentication


class System:
    def __init__(self):
        self.root = tk.Tk()

        self.modelo = UserModel()
        self.vista = LoginView(self.root)
        self.controlador = Authentication(self.modelo, self.vista)

        self.verificar_conexion()

    def verificar_conexion(self):
        conexion = Conexion().conectar()

        if conexion is None:
            print("No se pudo conectar con MySQL.")
            messagebox.showwarning(
                "Sin conexión a la base de datos",
                "No se pudo conectar con MySQL.\n\n"
                "Verifica que el servidor esté encendido, que ejecutaste "
                "models/schema.sql y que usuario/contraseña en "
                "models/conexion.py sean correctos.",
                parent=self.root
            )
        else:
            print("Conexión con MySQL exitosa.")
            conexion.close()

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = System()
    app.start()
