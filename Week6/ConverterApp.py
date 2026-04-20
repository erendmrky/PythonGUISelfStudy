import tkinter as tk
from ConverterForm import ConverterForm


class ConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Unit Converter")
        # We don't want the main (root) window visible. The converter form will be the "main" window.
        self.withdraw()

        # List of conversion result strings
        self.history = []

        # Open the converter form immediately
        self.open_converter()

    def open_converter(self):
        ConverterForm(parent=self)

    def add_history(self, text):
        self.history.append(text)

    def get_history(self):
        return list(self.history)


if __name__ == "__main__":
    app = ConverterApp()
    app.mainloop()
