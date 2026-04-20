import tkinter as tk
from tkinter import ttk, messagebox
from HistoryForm import HistoryWindow


class ConverterForm(tk.Toplevel):
    # Conversion factors relative to meters
    UNITS = {
        "Meter": 1.0,
        "Centimeter": 100.0,
        "Kilometer": 0.001,
        "Inch": 39.37,
        "Foot": 3.28,
    }

    def __init__(self, parent, title="Unit Converter"):
        super().__init__(parent)
        self.parent = parent  # root (ConverterApp)
        self.title(title)
        self.geometry("400x200")

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)

        self.resizable(False, False)

        # Variables
        self.input_var = tk.StringVar()
        self.from_var = tk.StringVar(value="Meter")
        self.to_var = tk.StringVar(value="Centimeter")

        # For storing a reference to the history window (if opened)
        self.history_win = None

        # Build UI
        self.build_ui()

        # Window behavior
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.history_win = None

    def build_ui(self):
        ttk.Label(self,text="Value:").grid(row=0,column=0,pady=10,padx=10,sticky="w")
        ttk.Label(self,text="From:").grid(row=1,column=0,pady=10,padx=10,sticky="w")
        ttk.Label(self,text="To:").grid(row=2,column=0,pady=10, padx=10,sticky="w")
        ttk.Label(self,text="Result:").grid(row=3,column=0,pady=10, padx=10,sticky="w")
        self.result_label = ttk.Label(self,text="")
        self.entry_value = ttk.Entry(self,textvariable=self.input_var)
        self.from_combobox = ttk.Combobox(self,textvariable=self.from_var,values=list(self.UNITS.keys()),state="readonly")
        self.to_combobox = ttk.Combobox(self,textvariable=self.to_var,values=list(self.UNITS.keys()),state="readonly")

        self.entry_value.grid(row=0, column=1, columnspan=2, pady=10, padx=10, sticky="ew")
        self.from_combobox.grid(row=1, column=1, columnspan=2, pady=10, padx=10, sticky="ew")
        self.to_combobox.grid(row=2, column=1, columnspan=2, pady=10, padx=10, sticky="ew")
        self.result_label.grid(row=3, column=1, columnspan=2, pady=10, padx=10, sticky="ew")

        buton_frame = ttk.Frame(self)
        buton_frame.grid(row=4,column=1,sticky="e", padx=10, pady=5)

        ttk.Button(buton_frame,text="Convert",command=self.on_convert).grid(row=0,column=1,padx=2)
        ttk.Button(buton_frame,text="History",command=self.open_history).grid(row=0,column=2,padx=2)
        ttk.Button(buton_frame,text="Close",command=self.on_close).grid(row=0,column=3,padx=2)



    def on_convert(self):
        value_in_meters = float(self.input_var.get()) / self.UNITS[self.from_var.get()]
        result = value_in_meters * self.UNITS[self.to_var.get()]
        result_var = f"{self.input_var.get()} {self.from_var.get()}(s) = {result} {self.to_var.get()}(s)"
        self.parent.add_history(result_var)
        self.result_label.configure(text=result_var)
        if self.history_win is not None:
            self.history_win.refresh_list()


    def open_history(self):
        if self.history_win is None:
            self.history_win = HistoryWindow(parent = self)

    def on_close(self):
        if messagebox.askyesno(title="Exit",message="Are you sure you want to exit?"):
            self.destroy()
        # When main form closes, end the whole application
        self.parent.destroy()
