import tkinter as tk
from tkinter import messagebox


class LoginView:

    def __init__(self, root):
        self.root = root

        color_fondo = "#FDF2E9"
        color_titulo = "#A04000"

        self.root.title("Lab 8 - Acceso al sistema")

        self.root.geometry("460x400")

        self.root.configure(bg=color_fondo)

        self.root.resizable(False, False)

        self.titulo = tk.Label(
            root,
            text="BIENVENIDO",
            font=("Verdana", 22, "bold"),
            bg=color_fondo,
            fg=color_titulo
        )
        self.titulo.pack(pady=20)

        self.lbl_email = tk.Label(
            root,
            text="Correo electrónico:",
            font=("Verdana", 11, "bold"),
            bg=color_fondo,
            fg="#4A235A"
        )
        self.lbl_email.pack()

        self.entry_email = tk.Entry(
            root,
            width=38,
            font=("Verdana", 11),
            relief="solid",
            bd=1
        )
        self.entry_email.pack(pady=5)

        self.lbl_password = tk.Label(
            root,
            text="Contraseña:",
            font=("Verdana", 11, "bold"),
            bg=color_fondo,
            fg="#4A235A"
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            root,
            width=38,
            font=("Verdana", 11),
            show="*",
            relief="solid",
            bd=1
        )
        self.entry_password.pack(pady=5)

        self.btn_login = tk.Button(
            root,
            text="Iniciar sesión",
            width=24,
            bg="#CA6F1E",
            fg="white",
            font=("Verdana", 11, "bold"),
            cursor="hand2"
        )
        self.btn_login.pack(pady=15)

        self.btn_register = tk.Button(
            root,
            text="¿No tienes cuenta? Regístrate",
            width=28,
            bg="#117A65",
            fg="white",
            font=("Verdana", 10),
            cursor="hand2"
        )
        self.btn_register.pack()

    def obtener_datos(self):
        email = self.entry_email.get().strip()
        password = self.entry_password.get()

        return email, password

    def limpiar_campos(self):
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.root)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.root)
