import tkinter as tk
from tkinter import messagebox


class RegisterView:

    def __init__(self, root):
        self.ventana = tk.Toplevel(root)

        color_fondo = "#EBF5FB"
        color_titulo = "#1B4F72"

        self.ventana.title("Lab 8 - Registro de nuevo usuario")

        self.ventana.geometry("460x480")

        self.ventana.configure(bg=color_fondo)

        self.ventana.resizable(False, False)

        self.ventana.transient(root)
        self.ventana.grab_set()

        self.titulo = tk.Label(
            self.ventana,
            text="NUEVA CUENTA",
            font=("Verdana", 20, "bold"),
            bg=color_fondo,
            fg=color_titulo
        )
        self.titulo.pack(pady=18)

        self.lbl_nombre = tk.Label(
            self.ventana,
            text="Nombre completo:",
            bg=color_fondo,
            fg="#154360",
            font=("Verdana", 10, "bold")
        )
        self.lbl_nombre.pack()

        self.entry_nombre = tk.Entry(
            self.ventana,
            width=38,
            font=("Verdana", 10),
            relief="solid",
            bd=1
        )
        self.entry_nombre.pack(pady=4)

        self.lbl_email = tk.Label(
            self.ventana,
            text="Correo electrónico:",
            bg=color_fondo,
            fg="#154360",
            font=("Verdana", 10, "bold")
        )
        self.lbl_email.pack()

        self.entry_email = tk.Entry(
            self.ventana,
            width=38,
            font=("Verdana", 10),
            relief="solid",
            bd=1
        )
        self.entry_email.pack(pady=4)

        self.lbl_password = tk.Label(
            self.ventana,
            text="Contraseña:",
            bg=color_fondo,
            fg="#154360",
            font=("Verdana", 10, "bold")
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            self.ventana,
            width=38,
            show="*",
            font=("Verdana", 10),
            relief="solid",
            bd=1
        )
        self.entry_password.pack(pady=4)

        self.lbl_confirmar = tk.Label(
            self.ventana,
            text="Confirmar contraseña:",
            bg=color_fondo,
            fg="#154360",
            font=("Verdana", 10, "bold")
        )
        self.lbl_confirmar.pack()

        self.entry_confirmar = tk.Entry(
            self.ventana,
            width=38,
            show="*",
            font=("Verdana", 10),
            relief="solid",
            bd=1
        )
        self.entry_confirmar.pack(pady=4)

        self.btn_guardar = tk.Button(
            self.ventana,
            text="Guardar registro",
            width=24,
            bg="#2E86C1",
            fg="white",
            font=("Verdana", 10, "bold"),
            cursor="hand2"
        )
        self.btn_guardar.pack(pady=12)

        self.btn_cancelar = tk.Button(
            self.ventana,
            text="Cancelar",
            width=24,
            command=self.cerrar,
            cursor="hand2"
        )
        self.btn_cancelar.pack()

        self.entry_nombre.focus_set()

    def obtener_datos(self):
        nombre = self.entry_nombre.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get()
        confirmar = self.entry_confirmar.get()

        return nombre, email, password, confirmar

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(
                titulo,
                mensaje,
                parent=self.ventana
            )
        else:
            messagebox.showinfo(
                titulo,
                mensaje,
                parent=self.ventana
            )

    def cerrar(self):
        self.ventana.destroy()
