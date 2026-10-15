import tkinter as tk
from tkinter import ttk, messagebox
from Models.login_model import User
from Views.home_view import DashboardVentana
from Views import theme


class LoginVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Acceso al Sistema")
        self._centrar(380, 500)
        self.root.resizable(False, False)

        theme.aplicar_tema(self.root)
        self._icono = theme.aplicar_icono(self.root)  # conservar la referencia

        self._crear_interfaz()

    def _centrar(self, ancho, alto):
        x = (self.root.winfo_screenwidth() - ancho) // 2
        y = max((self.root.winfo_screenheight() - alto) // 3, 0)
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")

    def _crear_interfaz(self):
        # Ícono grande arriba del título (reducido a ~96 px)
        if self._icono is not None:
            factor = max(self._icono.width() // 96, 1)
            self._logo = self._icono.subsample(factor, factor)
            ttk.Label(self.root, image=self._logo).pack(pady=(30, 5))

        ttk.Label(self.root, text="Iniciar Sesión", style="Title.TLabel").pack()
        ttk.Label(self.root, text="Ingresa tus credenciales para continuar",
                  style="Muted.TLabel", font=("Helvetica", 10)).pack(pady=(2, 20))

        ttk.Label(self.root, text="Usuario:", font=("Helvetica", 11)).pack(
            anchor="w", padx=40, pady=(5, 2))
        self.entry_usuario = ttk.Entry(self.root, font=("Helvetica", 12))
        self.entry_usuario.pack(fill="x", padx=40)

        ttk.Label(self.root, text="Contraseña:", font=("Helvetica", 11)).pack(
            anchor="w", padx=40, pady=(15, 2))
        self.entry_pass = ttk.Entry(self.root, font=("Helvetica", 12), show="*")
        self.entry_pass.pack(fill="x", padx=40)

        btn_ingresar = ttk.Button(
            self.root,
            text="Entrar",
            style="Accent.TButton",
            cursor="hand2",
            command=self._validar_login,
        )
        btn_ingresar.pack(fill="x", padx=40, pady=30)

        self.entry_usuario.focus_set()
        # Permite iniciar sesión presionando Enter
        self.root.bind("<Return>", lambda event: self._validar_login())

    def _validar_login(self):
        usuario_texto = self.entry_usuario.get().strip()
        pass_texto = self.entry_pass.get()

        if not usuario_texto or not pass_texto:
            messagebox.showwarning("Campos Vacíos", "Por favor ingresa usuario y contraseña.")
            return

        usuario_obj = User(usuario_texto, pass_texto)
        datos_usuario = usuario_obj.auth()

        if datos_usuario is None:
            messagebox.showerror(
                "Error de Conexión",
                "No se pudo consultar la base de datos.\n"
                "Verifica que MySQL esté encendido y que Controller/config.py sea correcto."
            )
        elif len(datos_usuario) > 0:
            nombre_usuario = datos_usuario[0].get("nombre", "Usuario")
            messagebox.showinfo("Bienvenido", f"¡Hola {nombre_usuario}! Acceso concedido.")
            self._abrir_dashboard(nombre_usuario)
        else:
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")

    def _abrir_dashboard(self, nombre_completo):
        # Reutiliza la misma ventana: limpia el login y muestra el panel
        self.root.unbind("<Return>")
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.resizable(True, True)
        DashboardVentana(self.root, nombre_completo)
