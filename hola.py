import tkinter as tk

def saludar():
    print("Hola a todos")

def despedirse():
    print("Nos vemos")

def saltar():
    print("El humano salta")

def respirar():
    print("Respira")

def mirar():
    print("Mirar")

ventana = tk.Tk()
ventana.geometry("600x400")

boton = tk.Button(text="Presioname")
boton.pack(padx=10, pady=10)

ventana.mainloop()