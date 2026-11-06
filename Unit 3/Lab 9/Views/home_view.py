import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class DashboardVentana:
    def __init__(self, root, nombre_usuario, controller):
        self.root = root
        self.controller = controller
        self.root.title("Panel Principal")
        self.root.geometry("700x460")

        lbl_mensaje = tk.Label(
            self.root,
            text=f"¡Bienvenido/a al Sistema!  Usuario activo: {nombre_usuario}",
            font=("Helvetica", 12),
        )
        lbl_mensaje.pack(pady=(15, 10))

        self._crear_controles_exportacion()
        self._crear_tabla()
        self._cargar_productos()

    def _crear_controles_exportacion(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill="x", padx=20, pady=(0, 10))

        ttk.Label(frame, text="Formato:").pack(side="left")

        self.combo_formato = ttk.Combobox(
            frame,
            values=self.controller.formatos_disponibles(),  # CSV, TXT, JSON, PDF
            state="readonly",
            width=10,
        )
        self.combo_formato.current(0)
        self.combo_formato.pack(side="left", padx=8)

        ttk.Button(
            frame, text="Exportar Reporte", command=self._exportar_reporte
        ).pack(side="left")

    def _crear_tabla(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        columnas = ("id", "nombre", "precio", "stock")
        self.tabla = ttk.Treeview(frame, columns=columnas, show="headings")
        for col, titulo, ancho, anchor in (
            ("id", "ID", 60, "center"),
            ("nombre", "Nombre", 330, "w"),
            ("precio", "Precio", 110, "e"),
            ("stock", "Stock", 80, "center"),
        ):
            self.tabla.heading(col, text=titulo)
            self.tabla.column(col, width=ancho, anchor=anchor)

        scroll = ttk.Scrollbar(frame, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

    def _cargar_productos(self):
        productos = self.controller.obtener_productos()
        if productos is None:
            messagebox.showerror(
                "Error de Conexión",
                "No se pudieron cargar los productos.\n"
                "Verifica que MySQL esté encendido y que la tabla 'productos' exista (login.sql).",
            )
            return

        self.tabla.delete(*self.tabla.get_children())
        for p in productos:
            self.tabla.insert(
                "", "end",
                values=(p["id_producto"], p["nombre"], f"${p['precio']}", p["stock"]),
            )

    def _exportar_reporte(self):
        formato = self.combo_formato.get()
        extension = self.controller.extension_de(formato)

        ruta = filedialog.asksaveasfilename(
            title=f"Guardar reporte {formato}",
            defaultextension=extension,
            initialfile=f"reporte_productos{extension}",
            filetypes=[(f"Archivo {formato}", f"*{extension}")],
        )
        if not ruta:  # el usuario canceló
            return

        exito, mensaje = self.controller.generar_reporte(formato, ruta)
        if exito:
            messagebox.showinfo("Exportación exitosa", mensaje)
        else:
            messagebox.showerror("Error al exportar", mensaje)
