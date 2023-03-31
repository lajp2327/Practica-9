from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBD import *
from tkinter import messagebox

controlador=controladorBD()

#Proceder a guardar usando el métdodo guardarUsuario() del objeto contolador
def ejecutarInsert():
    controlador.guardar_usuario(varNom.get(), varCorreo.get(), varContra.get())
    
#Función para buscar un usuario
def ejecutaSelectU():
    rsUsuario= controlador.consultarUsuario(varBus.get())
    
    textBus.config(state='normal')
    textBus.delete('1.0', tk.END)  
    for usu in rsUsuario:
        textBus.insert(tk.END, str(usu[0]) + " " + usu[1] + " " + usu[2] + " " + str(usu[3]) + "\n")
    textBus.config(state='disabled')
    
    if not rsUsuario:
        messagebox.showinfo("Usuario no encontrado", "No se encontró ningún usuario con ese identificador")

        
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

#Pestaña 2: Buscar usuario
titulo2=Label(pestaña2, text="Buscar usuarios", fg="blue", font=("Modern", 18)).pack()

varBus= tk.StringVar()
lblid=Label(pestaña2, text="Identificador de Usuario: ").pack()
txtid=Entry(pestaña2, textvariable=varBus).pack()
btnBuscar=Button(pestaña2, text="Buscar", command=ejecutaSelectU).pack()

subBus= Label(pestaña2, text="Registrado:", fg="blue").pack()

# crea el objeto Text y asignalo a la variable textBus
textBus = tk.Text(pestaña2, height=5, width=52)
textBus.pack()

panel.add(pestaña1, text="Formulario de Usuarios")
panel.add(pestaña2, text="Buscar Usuario ")
panel.add(pestaña3, text="Consultar Usuarios")
panel.add(pestaña4, text="Actualizar Usuario")
Ventana.mainloop()
