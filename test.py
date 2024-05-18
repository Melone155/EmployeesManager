import os
import tkinter as tk
from tkinter import Frame, Label, Button
from PIL import Image, ImageTk
import yaml

import AddEmployee
import EmployeeDetails

OpenMenu = True

def NormalScreen(root):
    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(root, width=900, height=50, bg="#FFFFFF")
    canvas.grid(row=0, column=0, columnspan=2, sticky='ew')

    # Bild laden und skalieren
    image_path = "Picture/img.png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        image = image.resize((460, 327))
        tk_image = ImageTk.PhotoImage(image)

        # Bild anzeigen
        label = tk.Label(root, image=tk_image)
        label.image = tk_image  # Referenz speichern
        label.grid(pady=0, row=1, column=0, columnspan=2)  # Columnspan hinzugefügt

    else:
        print("Bild nicht gefunden:", image_path)

    # Hinzufügen und Einstellungs-Labels
    add = tk.Label(root, text="Add", font=("Helvetica", 16), bg="white")
    add.grid(row=0, column=1, sticky='e', padx=20)

    options = tk.Label(root, text="Settings", font=("Helvetica", 16), bg="white")
    options.grid(row=0, column=0, sticky='w', padx=20)

    add.bind("<Button-1>", lambda event: AddEmployee.AddEmployee(root))
    options.bind("<Button-1>", lambda event: Settingsmenu(root))

    data = load_data()
    display_data(root, data)

def Settingsmenu(root):
    global OpenMenu
    if OpenMenu:
        settings_frame = Frame(root, bg="#FFFFFF")
        settings_frame.grid(row=1, column=0, columnspan=2, sticky='nsew')

        user = tk.Label(settings_frame, text="User", font=("Helvetica", 16), bg="white")
        user.grid(row=0, column=0, sticky='w', padx=10, pady=5)

        importdata = tk.Label(settings_frame, text="Import", font=("Helvetica", 16), bg="white")
        importdata.grid(row=1, column=0, sticky='w', padx=10, pady=5)

        export = tk.Label(settings_frame, text="Export", font=("Helvetica", 16), bg="white")
        export.grid(row=2, column=0, sticky='w', padx=10, pady=5)

        OpenMenu = False
    else:
        for widget in root.winfo_children():
            widget.destroy()
        OpenMenu = True
        NormalScreen(root)

def load_data():
    file_path = "Config/Employees.yaml"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file) or {}
        return data.get('Employees', {})
    return {}

def display_data(root, data):
    # Nur den Datenanzeigebereich löschen
    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) > 0:
            widget.grid_forget()

    container = Frame(root)
    container.grid(row=1, column=0, columnspan=2, padx=0, pady=1, sticky='nsew')

    main_frame = Frame(container)
    main_frame.pack(padx=0, pady=0, side="left", expand=False, fill='both')

    row = 0
    for emp_id, details in data.items():
        frame = Frame(main_frame, borderwidth=1, relief="solid", pady=5, padx=5)
        frame.grid(row=row, column=0, padx=10, pady=5, sticky='ew')

        name = f"{details['Last Name']}, {details['First Name']}"
        name_label = Label(frame, text=name, font=("Helvetica", 16))
        name_label.pack(side="left", padx=5, pady=5)

        view_button = Button(frame, text=">", font=("Helvetica", 16), command=lambda emp_id=emp_id: EmployeeDetails.Details(root, emp_id))
        view_button.pack(side="right", padx=5, pady=5)

        row += 1

    # Configure row and column weight for better resizing behavior
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)

def view_details(emp_id, data):
    details = data.get(emp_id)
    if details:
        # Hier kannst du eine neue Seite oder ein Popup-Fenster anzeigen, um die Details anzuzeigen.
        print(f"Details for {emp_id}: {details}")

# Hauptfenster erstellen
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x600")
    NormalScreen(root)
    root.mainloop()
