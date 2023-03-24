from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBD import *

controlador=controladorBD()

def ejecutarInsert():
    controlador.guardar_usuario(varNom.get(), varCorreo.get(), varContra.get())

Ventana=Tk()
Ventana.title("Crud Usuarios")
Ventana.geometry("500x300")

panel=ttk.Notebook(Ventana)
panel.pack(fill="both", expand="yes")

pestaña1=ttk.Frame(panel)
pestaña2=ttk.Frame(panel)
pestaña3=ttk.Frame(panel)
pestaña4=ttk.Frame(panel)

#Pestaña 1: Formulario Usuarios
titulo=Label(pestaña1, text="Registro Usuarios", fg="blue", font=("Modern", 18)).pack()

varNom= tk.StringVar()
lblNom=Label(pestaña1, text="Nombre: ").pack()
txtNom=Entry(pestaña1, textvariable=varNom).pack()

varCorreo= tk.StringVar()
lblCorreo=Label(pestaña1, text="Correo: ").pack()
txtCorreo=Entry(pestaña1, textvariable=varCorreo).pack()

varContra= tk.StringVar()
lblContra=Label(pestaña1, text="Contraseña: ").pack()
txtContra=Entry(pestaña1, textvariable=varContra).pack()

btnGuardar=Button(pestaña1, text="Guardar Usuario", command=ejecutarInsert).pack()



panel.add(pestaña1, text="Formulario de Usuarios")
panel.add(pestaña2, text="Buscar Usuario ")
panel.add(pestaña3, text="Consultar Usuarios")
panel.add(pestaña4, text="Actualizar Usuario")
Ventana.mainloop()
