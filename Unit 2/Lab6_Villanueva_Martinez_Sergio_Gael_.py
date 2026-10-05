import os
import sys
import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


def resource_path(filename: str) -> str:
   
    base_dir = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, filename)


class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def turn_on(self) -> str:
        pass


class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living Room Smart Light")

    def turn_on(self) -> str:
        return f"💡 {self.name}: Turned ON with 100% brightness."


class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Alexa Speaker")

    def turn_on(self) -> str:
        return f"🔊 {self.name}: Playing Lofi music."


class SmartThermostat(SmartDevice):
    def __init__(self):
        super().__init__("Ecobee Thermostat")

    def turn_on(self) -> str:
        return f"🌡️ {self.name}: Climate control active (Set to 22°C)."


class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lab 6: Smart Home Controller (Polymorphism)")
        self.geometry("600x500")
        self.resizable(True, True)

        self._set_icon()

        self.devices = {
            "Smart Light": SmartLight(),
            "Smart Speaker": SmartSpeaker(),
            "Smart Thermostat": SmartThermostat()
        }

        self._build_interface()

    def _set_icon(self):
        """Carga icon.png (debe estar en la misma carpeta que este archivo)."""
        icon_path = resource_path("icon.png")
        try:
            # Se guarda en self para que Python no elimine la imagen de memoria
            self.icon_img = tk.PhotoImage(file=icon_path)
            self.iconphoto(True, self.icon_img)
        except tk.TclError:
            # Si el icono falta o no se puede leer, la app sigue funcionando
            print(f"Aviso: no se pudo cargar el icono en '{icon_path}'.")

    def _build_interface(self):
        lbl_header = tk.Label(
            self,
            text="SMART HOME CENTER",
            font=("Arial", 15, "bold"),
            fg="#2c3e50"
        )
        lbl_header.pack(pady=12)

        group_box = tk.LabelFrame(
            self,
            text=" Select Device ",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=10
        )
        group_box.pack(fill="x", padx=20, pady=5)

        first_key = list(self.devices.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        for key in self.devices.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=3)

        btn_action = tk.Button(
            self,
            text="TURN ON DEVICE",
            command=self._handle_action,
            bg="#2980b9",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_action.pack(pady=15)

        self.lbl_output = tk.Label(
            self,
            text="Select a device above and click 'TURN ON DEVICE'.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

    def _handle_action(self):
        chosen_key = self.selected_key.get()
        active_device: SmartDevice = self.devices[chosen_key]
        result_message = active_device.turn_on()
        self.lbl_output.config(text=result_message, font=("Arial", 10, "normal"))


if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()
