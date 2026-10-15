"""Colores, estilos ttk e ícono compartidos por todas las ventanas."""
import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICON_PNG = os.path.join(BASE_DIR, "Assets", "icon.png")
ICON_ICO = os.path.join(BASE_DIR, "Assets", "icon.ico")

BG = "#2b2b2b"          # fondo de la ventana
PANEL = "#333333"       # paneles / pestañas
FIELD = "#1e1e1e"       # campos de texto y tabla
FG = "#ffffff"
FG_MUTED = "#b8b8b8"
ACCENT = "#2196F3"
ACCENT_HOVER = "#42a5f5"
BORDER = "#555555"


def aplicar_icono(root):
    """Pone el ícono de la aplicación en la ventana.
    Devuelve el PhotoImage (hay que conservar la referencia) o None."""
    imagen = None
    try:
        imagen = tk.PhotoImage(file=ICON_PNG)
        root.iconphoto(True, imagen)
    except tk.TclError as e:
        print(f"No se pudo cargar el ícono PNG: {e}")
    if os.name == "nt":
        try:
            root.iconbitmap(ICON_ICO)
        except tk.TclError:
            pass
    return imagen


def aplicar_tema(root):
    """Tema oscuro con ttk (el tema 'clam' respeta los colores en todos los SO)."""
    root.configure(bg=BG)
    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure(".", background=BG, foreground=FG, font=("Helvetica", 12))
    style.configure("TFrame", background=BG)
    style.configure("Panel.TFrame", background=PANEL)
    style.configure("TLabel", background=BG, foreground=FG)
    style.configure("Panel.TLabel", background=PANEL, foreground=FG)
    style.configure("Title.TLabel", font=("Helvetica", 16, "bold"))
    style.configure("Muted.TLabel", foreground=FG_MUTED)

    style.configure("TLabelframe", background=PANEL, bordercolor=FG, relief="solid")
    style.configure("TLabelframe.Label", background=PANEL, foreground=FG,
                    font=("Helvetica", 10, "bold"))

    style.configure("TEntry", fieldbackground=FIELD, foreground=FG,
                    insertcolor=FG, bordercolor=BORDER, lightcolor=BORDER,
                    darkcolor=BORDER, padding=4)
    style.map("TEntry", bordercolor=[("focus", ACCENT)],
              lightcolor=[("focus", ACCENT)], darkcolor=[("focus", ACCENT)])

    # Botón blanco (Guardar Producto)
    style.configure("TButton", background="#ffffff", foreground="#000000",
                    font=("Helvetica", 11, "bold"), padding=4, borderwidth=0)
    style.map("TButton", background=[("active", "#e0e0e0")])
    # Botón de acento (Entrar)
    style.configure("Accent.TButton", background=ACCENT, foreground="#ffffff",
                    font=("Helvetica", 12, "bold"), padding=8)
    style.map("Accent.TButton", background=[("active", ACCENT_HOVER)])

    style.configure("TNotebook", background=BG, bordercolor=BORDER)
    style.configure("TNotebook.Tab", background=BG, foreground=FG,
                    padding=(14, 6), font=("Helvetica", 12))
    style.map("TNotebook.Tab", background=[("selected", "#5a5a5e")],
              foreground=[("selected", FG)])

    style.configure("Treeview", background=FIELD, fieldbackground=FIELD,
                    foreground=FG, rowheight=26, borderwidth=0,
                    font=("Helvetica", 12))
    style.map("Treeview", background=[("selected", ACCENT)],
              foreground=[("selected", "#ffffff")])
    style.configure("Treeview.Heading", background=FIELD, foreground=FG,
                    font=("Helvetica", 11), relief="flat")
    style.map("Treeview.Heading", background=[("active", PANEL)])
    style.configure("TScrollbar", background="#555555", troughcolor=FIELD,
                    bordercolor=FIELD, lightcolor="#555555", darkcolor="#555555",
                    arrowcolor=FG, gripcount=0)
    style.map("TScrollbar", background=[("active", "#6a6a6a")],
              lightcolor=[("active", "#6a6a6a")], darkcolor=[("active", "#6a6a6a")])
    return style
