import tkinter as tk

ventana = tk.Tk()
ventana.geometry("600x400")

boton = tk.Button(text="Presioname")
boton.pack(padx=10, pady=10)

ventana.mainloop()