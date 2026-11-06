from Models.product_model import Product
from exporters import available_formats, get_exporter


class ProductController:
    """Intermediario entre la Vista y el Modelo.

    No importa csv, json ni fpdf: solo conoce la interfaz Exporter
    (get_exporter + .export()). El polimorfismo hace el resto.
    """

    def __init__(self):
        self.model = Product()

    def obtener_productos(self):
        return self.model.get_all()

    def formatos_disponibles(self):
        return available_formats()

    def extension_de(self, formato):
        return get_exporter(formato).extension

    def generar_reporte(self, formato, ruta_archivo):
        """Exporta el inventario actual. Devuelve (exito, mensaje) para que la Vista lo muestre."""
        productos = self.model.get_all()
        if productos is None:
            return False, "No se pudo consultar la base de datos."
        if not productos:
            return False, "No hay productos registrados para exportar."

        try:
            exportador = get_exporter(formato)   # solo se instancia la clase del formato elegido
            exportador.export(productos, ruta_archivo)  # llamada genérica: polimorfismo
        except Exception as e:
            return False, f"No se pudo generar el reporte {formato}:\n{e}"

        return True, f"Reporte {formato} generado correctamente:\n{ruta_archivo}"
