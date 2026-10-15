import tkinter as tk
from tkinter import ttk, messagebox
from Models.products_model import Product
from Views import theme


class DashboardVentana:
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.nombre_usuario = nombre_usuario
        self.root.title("Panel Principal - Sistema")
        self._centrar(1000, 720)
        self.root.minsize(800, 520)
        self.root.configure(bg=theme.BG)

        ttk.Label(
            self.root,
            text=f"Bienvenido/a, {nombre_usuario}",
            font=("Helvetica", 16, "bold"),
        ).pack(pady=(25, 20))

        # Pestañas: Inicio | Inventario de Productos
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=40, pady=(0, 30))

        self.tab_inicio = ttk.Frame(self.notebook, padding=20)
        self.tab_productos = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(self.tab_inicio, text="Inicio")
        self.notebook.add(self.tab_productos, text="Inventario de Productos")

        self._crear_inicio()
        self.products_frame()
        self.cargar_productos()

    def _centrar(self, ancho, alto):
        # La ventana del login ya estaba centrada con otro tamaño; sin esto el
        # panel (más grande) podría quedar parcialmente fuera de la pantalla.
        ancho = min(ancho, self.root.winfo_screenwidth() - 40)
        alto = min(alto, self.root.winfo_screenheight() - 80)
        x = (self.root.winfo_screenwidth() - ancho) // 2
        y = max((self.root.winfo_screenheight() - alto) // 3, 0)
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")

    # ------------------------------------------------------------------
    # Pestaña "Inicio"
    # ------------------------------------------------------------------
    def _crear_inicio(self):
        ttk.Label(
            self.tab_inicio,
            text=f"¡Bienvenido/a al Sistema!\n\nUsuario activo:\n{self.nombre_usuario}",
            font=("Helvetica", 14),
            justify="center",
        ).pack(expand=True)

    # ------------------------------------------------------------------
    # Pestaña "Inventario de Productos"
    # ------------------------------------------------------------------
    def products_frame(self):
        self.tab_productos.columnconfigure(1, weight=1)
        self.tab_productos.rowconfigure(0, weight=1)

        self._crear_formulario()
        self._crear_tabla()

    def _crear_formulario(self):
        form = ttk.LabelFrame(self.tab_productos, text="Registrar Producto", padding=10)
        form.grid(row=0, column=0, sticky="ns", padx=(0, 20))
        form.columnconfigure(0, minsize=210)

        ttk.Label(form, text="Nombre:", style="Panel.TLabel").pack(anchor="w", pady=(5, 5))
        self.entry_nombre = ttk.Entry(form)
        self.entry_nombre.pack(fill="x")

        ttk.Label(form, text="Precio:", style="Panel.TLabel").pack(anchor="w", pady=(20, 5))
        self.entry_precio = ttk.Entry(form)
        self.entry_precio.pack(fill="x")

        ttk.Label(form, text="Stock:", style="Panel.TLabel").pack(anchor="w", pady=(20, 5))
        self.entry_stock = ttk.Entry(form)
        self.entry_stock.pack(fill="x")

        ttk.Button(
            form, text="Guardar Producto", cursor="hand2", command=self.guardar_producto
        ).pack(fill="x", pady=(40, 0))

        self.entry_nombre.focus_set()

    def _crear_tabla(self):
        contenedor = ttk.Frame(self.tab_productos)
        contenedor.grid(row=0, column=1, sticky="nsew")
        contenedor.columnconfigure(0, weight=1)
        contenedor.rowconfigure(0, weight=1)

        tree_scroll = ttk.Scrollbar(contenedor, orient="vertical")
        self.table = ttk.Treeview(
            contenedor,
            columns=("ID", "Nombre", "Precio", "Stock"),
            show="headings",
            yscrollcommand=tree_scroll.set,
        )
        tree_scroll.config(command=self.table.yview)

        self.table.heading("ID", text="ID")
        self.table.heading("Nombre", text="Nombre")
        self.table.heading("Precio", text="Precio ($)")
        self.table.heading("Stock", text="Stock")
        self.table.column("ID", width=70, anchor="center", stretch=False)
        self.table.column("Nombre", width=300, anchor="w")
        self.table.column("Precio", width=130, anchor="e")
        self.table.column("Stock", width=100, anchor="center", stretch=False)

        self.table.grid(row=0, column=0, sticky="nsew")
        tree_scroll.grid(row=0, column=1, sticky="ns")

    # ------------------------------------------------------------------
    # Lógica
    # ------------------------------------------------------------------
    def cargar_productos(self):
        """Vuelve a llenar la tabla con los productos de la base de datos."""
        for fila in self.table.get_children():
            self.table.delete(fila)

        productos = Product().get_products()
        if productos is None:
            messagebox.showerror(
                "Error de Conexión",
                "No se pudieron cargar los productos.\n"
                "Verifica que MySQL esté encendido y que la tabla 'products' exista.",
            )
            return

        for p in productos:
            self.table.insert(
                "", "end",
                values=(p["id_product"], p["nombre"], f"{p['precio']:.2f}", p["stock"]),
            )

    def guardar_producto(self):
        nombre = self.entry_nombre.get().strip()
        precio_txt = self.entry_precio.get().strip()
        stock_txt = self.entry_stock.get().strip()

        if not nombre or not precio_txt or not stock_txt:
            messagebox.showwarning("Campos Vacíos", "Completa nombre, precio y stock.")
            return

        try:
            precio = round(float(precio_txt), 2)
            if precio < 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Precio inválido", "El precio debe ser un número mayor o igual a 0.")
            return

        try:
            stock = int(stock_txt)
            if stock < 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Stock inválido", "El stock debe ser un número entero mayor o igual a 0.")
            return

        if Product(nombre=nombre, precio=precio, stock=stock).save():
            for entry in (self.entry_nombre, self.entry_precio, self.entry_stock):
                entry.delete(0, tk.END)
            self.cargar_productos()
            self.entry_nombre.focus_set()
        else:
            messagebox.showerror("Error", "No se pudo guardar el producto en la base de datos.")
