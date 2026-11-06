"""Módulo de exportación (Patrón Estrategia).

Toda la lógica de manejo de archivos vive AQUÍ. El Controlador y la Vista
no importan csv, json ni fpdf: solo piden un exportador con get_exporter()
y llaman a .export(), sin importar qué formato sea.

Los datos llegan como lista de diccionarios (así los devuelve el Modelo):
    [{"id_producto": 1, "nombre": "Teclado", "precio": Decimal("499.00"), ...}, ...]
"""
import csv
import json
from abc import ABC, abstractmethod
from datetime import date, datetime
from decimal import Decimal

from fpdf import FPDF


# --------------------------------------------------------------------------- #
# Utilidades internas
# --------------------------------------------------------------------------- #
def _columnas(datos):
    """Nombres de columna tomados de las llaves del primer registro."""
    return list(datos[0].keys()) if datos else []


def _titulo(columna):
    """'id_producto' -> 'Id producto'"""
    return columna.replace("_", " ").capitalize()


def _texto(valor):
    """Convierte un valor de BD a texto legible (None -> vacío)."""
    return "" if valor is None else str(valor)


# --------------------------------------------------------------------------- #
# Clase base (interfaz)
# --------------------------------------------------------------------------- #
class Exporter(ABC):
    """Interfaz común: cada formato hereda de aquí y sobrescribe export()."""

    extension = ""  # p. ej. ".csv"; la usa la Vista para sugerir el nombre

    @abstractmethod
    def export(self, data, file_path):
        """Método que debe ser sobrescrito por las clases hijas."""
        raise NotImplementedError("Este método debe ser implementado por la subclase.")


# --------------------------------------------------------------------------- #
# Clases hijas
# --------------------------------------------------------------------------- #
class CSVExporter(Exporter):
    extension = ".csv"

    def export(self, data, file_path):
        # utf-8-sig: Excel abre bien los acentos; newline='' evita filas en blanco en Windows
        with open(file_path, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=_columnas(data))
            writer.writeheader()
            writer.writerows(data)
        print(f"Archivo CSV generado en: {file_path}")


class TXTExporter(Exporter):
    extension = ".txt"

    def export(self, data, file_path):
        columnas = _columnas(data)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("--- REPORTE DE PRODUCTOS ---\n")
            for producto in data:
                linea = " | ".join(
                    f"{_titulo(col)}: {_texto(producto[col])}" for col in columnas
                )
                file.write(linea + "\n")
        print(f"Archivo TXT generado en: {file_path}")


class JSONExporter(Exporter):
    extension = ".json"

    @staticmethod
    def _convertir(valor):
        """json no sabe serializar Decimal (MySQL DECIMAL) ni fechas."""
        if isinstance(valor, Decimal):
            return float(valor)
        if isinstance(valor, (date, datetime)):
            return valor.isoformat()
        return str(valor)

    def export(self, data, file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4, default=self._convertir)
        print(f"Archivo JSON generado en: {file_path}")


class PDFExporter(Exporter):
    extension = ".pdf"

    ANCHO_UTIL = 190   # A4 (210 mm) menos márgenes de 10 mm
    ALTO_FILA = 8

    @staticmethod
    def _latin1(texto):
        """Las fuentes base de FPDF solo admiten Latin-1 (á, ñ, ü sí; emojis no)."""
        return texto.encode("latin-1", "replace").decode("latin-1")

    def _anchos(self, columnas, datos):
        """Reparte el ancho de la página según el largo del contenido de cada columna."""
        largos = [
            max([len(_titulo(c))] + [len(_texto(fila[c])) for fila in datos]) + 2
            for c in columnas
        ]
        total = sum(largos)
        return [self.ANCHO_UTIL * largo / total for largo in largos]

    def _encabezado_tabla(self, pdf, columnas, anchos):
        pdf.set_font("Arial", "B", 11)
        pdf.set_fill_color(220, 220, 220)
        for col, ancho in zip(columnas, anchos):
            pdf.cell(ancho, self.ALTO_FILA, self._latin1(_titulo(col)), 1, 0, "C", True)
        pdf.ln(self.ALTO_FILA)
        pdf.set_font("Arial", "", 11)

    def export(self, data, file_path):
        columnas = _columnas(data)
        anchos = self._anchos(columnas, data)

        pdf = FPDF()
        pdf.add_page()

        # Título
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Reporte de Inventario de Productos", 0, 1, "C")
        pdf.ln(5)

        self._encabezado_tabla(pdf, columnas, anchos)

        # Cuerpo
        for producto in data:
            if pdf.get_y() + self.ALTO_FILA > pdf.page_break_trigger:
                pdf.add_page()
                self._encabezado_tabla(pdf, columnas, anchos)
            for col, ancho in zip(columnas, anchos):
                pdf.cell(ancho, self.ALTO_FILA, self._latin1(_texto(producto[col])), 1)
            pdf.ln(self.ALTO_FILA)

        pdf.output(file_path)
        print(f"Archivo PDF generado en: {file_path}")


# --------------------------------------------------------------------------- #
# Fábrica: el Controlador pide un exportador por nombre de formato
# --------------------------------------------------------------------------- #
EXPORTERS = {
    "CSV": CSVExporter,
    "TXT": TXTExporter,
    "JSON": JSONExporter,
    "PDF": PDFExporter,
}


def available_formats():
    """Formatos soportados, en el orden en que se muestran en el Combobox."""
    return list(EXPORTERS)


def get_exporter(format_name):
    """Devuelve una instancia del exportador correspondiente al formato."""
    try:
        return EXPORTERS[format_name.upper()]()
    except KeyError:
        raise ValueError(f"Formato no soportado: {format_name}") from None
