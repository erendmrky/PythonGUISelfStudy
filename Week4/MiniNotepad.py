import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd
from tkinter import messagebox as msg

file_path = ""

def file_menu_new():
    win.title("Untitled - Mini Notepad")
    editor.delete("1.0","end")
def file_menu_open():
    try:
        global file_path
        file_path = fd.askopenfilename(filetypes=(("Text file", "*.txt"),))
        with open(file_path,"r",encoding="utf-8") as f:
            text = f.read()
            win.title(file_path.split("/")[-1])
            editor.insert("1.0", text)
    except FileNotFoundError:
        pass

def file_menu_save_as():
    try:
        global file_path
        if file_path == "":
            file_path = fd.asksaveasfilename(filetypes=(("Text file", "*.txt"),),defaultextension=".txt")
        with open(file_path,"w",encoding="utf-8") as f:
            f.write(editor.get("1.0","end"))
            win.title(file_path.split("/")[-1])
    except FileNotFoundError:
        file_path = ""

def file_menu_exit():
    dialog_result = msg.askyesno(title="Exit", message="Are you sure you want to exit?")
    if dialog_result:
        win.destroy()

def show_about():
    msg.showinfo(message="Mini Notepad\n\nSEN4017 Week 4 self-study exercise.")

# Window
win = tk.Tk()
win.geometry("415x215")
win.title("Untitled - Mini Notepad")
win.protocol("WM_DELETE_WINDOW", file_menu_exit)

# Win Config
win.columnconfigure(0, weight=1)
win.rowconfigure(0, weight=1)
menubar = tk.Menu(win)
win.config(menu=menubar)

# Text Editor
editor = ScrolledText(win,wrap="word",undo=True,font=("Consolas",12))
editor.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)
editor.focus_set()

# File Menu
file_menu = tk.Menu(menubar,tearoff=0)
file_menu.add_command(label="New",underline=0,command=file_menu_new)
file_menu.add_command(label="Open...",underline=0,command=file_menu_open)
file_menu.add_command(label="Save",underline=0,command=file_menu_save_as)
file_menu.add_command(label="Save As...",underline=1,command=file_menu_save_as)
file_menu.add_command(label="Exit",underline=0,command=file_menu_exit)

# Help Menu
help_menu = tk.Menu(menubar,tearoff=0)
help_menu.add_command(label="About...",underline=0,command=show_about)

# Cascading the menu to menubar
menubar.add_cascade(label="File",menu=file_menu)
menubar.add_cascade(label="Help",menu=help_menu)

win.mainloop()
