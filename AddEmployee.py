import tkinter as tk

import EmployeeManager


def AddEmployee(event, root):
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Add", font=("Helvetica", 16), bg="white")
    label.place(x=840, y=11)

    # Binde die AddEmployee-Funktion an das Label
    label.bind("<Button-1>", lambda event: EmployeeManager.NormalScreen(root))