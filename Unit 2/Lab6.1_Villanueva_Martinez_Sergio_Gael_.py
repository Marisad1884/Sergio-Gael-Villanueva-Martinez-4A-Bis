import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
from datetime import datetime


class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def turn_on(self) -> str:
        pass

    @abstractmethod
    def turn_off(self) -> str:
        pass


class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living Room Smart Light")

    def turn_on(self) -> str:
        return f"💡 {self.name}: Turned ON with 100% brightness."

    def turn_off(self) -> str:
        return f"💡 {self.name}: Dimmed down and turned OFF."


class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Alexa Speaker")

    def turn_on(self) -> str:
        return f"🔊 {self.name}: Playing Lofi music."

    def turn_off(self) -> str:
        return f"🔊 {self.name}: Music stopped. Speaker in standby."


class SmartThermostat(SmartDevice):
    def __init__(self):
        super().__init__("Ecobee Thermostat")

    def turn_on(self) -> str:
        return f"🌡️ {self.name}: Climate control active (Set to 22°C)."

    def turn_off(self) -> str:
        return f"🌡️ {self.name}: Climate control disabled."


class SmartTV(SmartDevice):
    def __init__(self):
        super().__init__("Bedroom Smart TV")

    def turn_on(self) -> str:
        return f"📺 {self.name}: Screen ON, launching youtube app."

    def turn_off(self) -> str:
        return f"📺 {self.name}: Screen OFF."


class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lab 6: Smart Home Controller (Polymorphism)")
        self.geometry("620x640")
        self.minsize(520, 520)
        self.resizable(True, True)

        self.devices = {
            "Smart Light": SmartLight(),
            "Smart Speaker": SmartSpeaker(),
            "Smart Thermostat": SmartThermostat(),
            "Smart TV": SmartTV(),
        }

        self._build_interface()

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

        frame_buttons = tk.Frame(self)
        frame_buttons.pack(pady=15)

        btn_on = tk.Button(
            frame_buttons,
            text="TURN ON DEVICE",
            command=self._handle_turn_on,
            bg="#2980b9",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_on.pack(side="left", padx=8)

        btn_off = tk.Button(
            frame_buttons,
            text="TURN OFF DEVICE",
            command=self._handle_turn_off,
            bg="#c0392b",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_off.pack(side="left", padx=8)

        self.lbl_output = tk.Label(
            self,
            text="Select a device above and use the buttons to control it.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=500,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

        log_frame = tk.LabelFrame(
            self,
            text=" Activity Log ",
            font=("Arial", 10, "bold"),
            padx=8,
            pady=8
        )
        log_frame.pack(fill="both", expand=True, padx=20, pady=(10, 5))

        scrollbar = ttk.Scrollbar(log_frame, orient="vertical")
        self.txt_log = tk.Text(
            log_frame,
            height=8,
            wrap="word",
            font=("Consolas", 10),
            bg="#fdfefe",
            state="disabled",
            yscrollcommand=scrollbar.set
        )
        scrollbar.config(command=self.txt_log.yview)
        scrollbar.pack(side="right", fill="y")
        self.txt_log.pack(side="left", fill="both", expand=True)

        self.txt_log.tag_config("on", foreground="#1e8449")
        self.txt_log.tag_config("off", foreground="#c0392b")
        self.txt_log.tag_config("time", foreground="#7f8c8d")

        btn_clear = ttk.Button(self, text="Clear Log", command=self._clear_log)
        btn_clear.pack(pady=(5, 12))

    def _get_selected_device(self) -> SmartDevice:
        return self.devices[self.selected_key.get()]

    def _handle_turn_on(self):
        message = self._get_selected_device().turn_on()
        self._show_result(message, "on")

    def _handle_turn_off(self):
        message = self._get_selected_device().turn_off()
        self._show_result(message, "off")

    def _show_result(self, message: str, tag: str):
        self.lbl_output.config(text=message, font=("Arial", 10, "normal"))
        self._log(message, tag)

    def _log(self, message: str, tag: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.txt_log.config(state="normal")
        self.txt_log.insert("end", f"[{timestamp}] ", "time")
        self.txt_log.insert("end", f"{message}\n", tag)
        self.txt_log.see("end")
        self.txt_log.config(state="disabled")

    def _clear_log(self):
        self.txt_log.config(state="normal")
        self.txt_log.delete("1.0", "end")
        self.txt_log.config(state="disabled")


if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()