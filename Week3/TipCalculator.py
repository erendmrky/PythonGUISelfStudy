import tkinter as tk
import tkinter.ttk as ttk
import math

def discombobulate():
    if ServiceComboBox.get() == "Poor(5%)":
        return 0.05
    if ServiceComboBox.get() == "Ok(10%)":
        return 0.1
    if ServiceComboBox.get() == "Good(12.5%)":
        return 0.125
    if ServiceComboBox.get() == "Great(15%)":
        return 0.15
    if ServiceComboBox.get() == "Excellent(20%)":
        return 0.2
    return 0.125

def calculate_button_handler():
    try:
        tipLabelResult = discombobulate() * float(BillEntry.get())
        totalLabelResult = discombobulate() * float(BillEntry.get()) + float(BillEntry.get())

        if selected_radio_item.get() == "tip":
            tipLabelResult = round(tipLabelResult,0)
        if selected_radio_item.get() == "total":
            totalLabelResult = round(totalLabelResult,0)
        TipLabel.configure(text=f"Tip: {tipLabelResult}")
        TotalLabel.configure(text=f"Total: {totalLabelResult}")
    except ValueError:
        print("Value Error found type only number")
        return

def clear_button_handler():
    TipLabel.configure(text="Tip:--")
    TotalLabel.configure(text="Total:--")
    BillEntry.configure(textvariable=tk.StringVar())
    selected_combo_item.set("Good(12.5%)")
    selected_radio_item.set("none")

win = tk.Tk()
win.geometry("500x230")
win.title("Tip Calculator")

# Win configure
win.rowconfigure(index=0,weight=1)
win.columnconfigure(index=0,weight=1)
win.columnconfigure(index=1,weight=1)
win.rowconfigure(index=1,weight=2)

selected_combo_item = tk.StringVar(value="Good(12.5%)")
selected_radio_item = tk.StringVar(value="none")

# Inputs Label Frame
Inputs = ttk.Labelframe(win,text="Inputs")
BillLabel = ttk.Label(Inputs,text="Bill:")
BillEntry = ttk.Entry(Inputs,width=30)
ServiceLabel = ttk.Label(Inputs,text="Service:")
ServiceComboBox = ttk.Combobox(Inputs,width=15,textvariable=selected_combo_item,state="readonly")
ServiceComboBox["values"] = ("Poor(5%)","Ok(10%)","Good(12.5%)","Great(15%)","Excellent(20%")
RoundingLabel = ttk.Label(Inputs,text="Rounding:")
RoundingButton1 = ttk.Radiobutton(Inputs,text="No Rounding",value="none",variable=selected_radio_item)
RoundingButton2 = ttk.Radiobutton(Inputs,text="Round tip",value="tip",variable=selected_radio_item)
RoundingButton3 = ttk.Radiobutton(Inputs,text="Round total",value="total",variable=selected_radio_item)

# Result Label Frame
ResultsLabel = ttk.LabelFrame(win,text="Results")
TipLabel = ttk.Label(ResultsLabel,text="Tip:--")
TotalLabel = ttk.Label(ResultsLabel,text="Total:--")

# Calculate / Clear Button
ButtonFrame = ttk.Frame(win)
CalculateButton = ttk.Button(ButtonFrame,text="Calculate",command=calculate_button_handler)
ClearButton = ttk.Button(ButtonFrame,text="Clear",command=clear_button_handler)

# Inputs Label Grid
Inputs.grid(row=0,column=0,padx=10,pady=15,sticky="nswe")
BillLabel.grid(row=0,column=0,padx=5,pady=5,sticky="nswe")
BillEntry.grid(row=0,column=1,padx=5,pady=5,sticky="nswe")
ServiceLabel.grid(row=1,column=0,padx=5,pady=5,sticky="nswe")
ServiceComboBox.grid(row=1,column=1,padx=5,pady=5,sticky="nswe")
RoundingLabel.grid(row=2,column=0,padx=5,sticky="nswe")
RoundingButton1.grid(row=2,column=1,padx=5,sticky="nswe")
RoundingButton2.grid(row=3,column=1,padx=5,sticky="nswe")
RoundingButton3.grid(row=4,column=1,padx=5,sticky="nswe")

# Result Label Grid
ResultsLabel.grid(row=0,column=1,padx=10,pady=15,sticky="nswe")
TipLabel.pack(padx=5,pady=5,anchor="w")
TotalLabel.pack(padx=5,pady=5,anchor="w")

# Calculate / Clear Button Pack
ButtonFrame.grid(row=1,column=0,sticky="nswe",padx=10)
CalculateButton.grid(row=0,column=0,padx=5)
ClearButton.grid(row=0,column=1)

win.mainloop()
