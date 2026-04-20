import tkinter as tk
from tkinter import ttk

class HistoryWindow(tk.Toplevel):
    def __init__(self, parent, title="History"):
        super().__init__(parent)
        self.parent = parent
        self.title(title)
        self.geometry("270x225")
        self.resizable(False, False)

        self.build_ui()
        self.refresh_list()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def build_ui(self):
        ttk.Label(self,text="Previous Conversions: ").grid(row=0,column=0,padx=10,pady=(10,15),sticky="w")
        self.listbox = tk.Listbox(self,width=40,height=8)
        self.listbox.grid(row=1,column=0,padx=10,sticky="ew")
        button_frame = ttk.Frame(self)
        button_frame.grid(row=2,column=0,sticky="e",pady=(15,5))
        ttk.Button(button_frame,text="Clear",command=self.clear_history).grid(row=0,column=1,padx="5")
        ttk.Button(button_frame,text="Close",command=self.on_close).grid(row=0,column=2,padx="5")

    def refresh_list(self):
        if self.parent.parent.get_history() is not None and len(self.listbox.get(0,"end")) == 0:
            for item in self.parent.parent.get_history():
                self.listbox.insert("end", item)
        elif len(self.parent.parent.get_history()) > len(self.listbox.get(0,"end")):
            self.listbox.insert("end",self.parent.parent.get_history()[len(self.parent.parent.get_history())-1])

    def on_close(self):
        self.parent.history_win = None
        self.destroy()

    def clear_history(self):
        self.listbox.delete(0,"end")
        self.parent.parent.history = []