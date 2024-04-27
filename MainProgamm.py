import tkinter as tk
import os
import Setup

# Hauptfenster erstellen
root = tk.Tk()
root.title("Mitarbeiter Management Programm")
root.geometry("900x600")

# Setup Wizard starten
Setup.Setupstart(root)

# GUI-Schleife starten
root.mainloop()
