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

#Función para mostrar a todos los usuarios
def cargar_usuarios():
    
    registros = tablaUsuarios.get_children()
    for registro in registros:
            tablaUsuarios.delete(registro)

    usuarios = controlador.consultar_usuarios()
    
    for usuario in usuarios:
            tablaUsuarios.insert("", END, values=usuario)

#Función para actualizar un usuario
def actualizar_usuarios():
    controlador.actualizar_usuarios(varid_actualizar.get(), varNom_actualizar.get(), varCorreo_actualizar.get(), varContra_actualizar.get())
    
#Función para eliminar un usuario
def elimina_usuario():
    controlador.eliminar_usuario(varid_eliminar.get())  

Ventana=Tk()
Ventana.title("Crud Usuarios")
Ventana.geometry("800x500")

panel=ttk.Notebook(Ventana)
panel.pack(fill="both", expand="yes")

pestaña1=ttk.Frame(panel)
pestaña2=ttk.Frame(panel)
pestaña3=ttk.Frame(panel)
pestaña4=ttk.Frame(panel)
pestaña5=ttk.Frame(panel)

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
titulo2=Label(pestaña2, text="Buscar usuarios", fg="orange", font=("Modern", 18)).pack()

varBus= tk.StringVar()
lblid=Label(pestaña2, text="Identificador de Usuario: ").pack()
txtid=Entry(pestaña2, textvariable=varBus).pack()
btnBuscar=Button(pestaña2, text="Buscar", command=ejecutaSelectU).pack()

subBus= Label(pestaña2, text="Registrado:", fg="blue").pack()

# crea el objeto Text y asignalo a la variable textBus
textBus = tk.Text(pestaña2, height=5, width=52)
textBus.pack()

#Pestaña 3: Consultar Usuarios
titulo3=Label(pestaña3, text="Consultar todos los Usuarios", fg="orange", font=("Modern", 18)).pack()
frameTabla = Frame(pestaña3)
frameTabla.pack()

frameTabla = Frame(pestaña3)
frameTabla.pack()

tablaUsuarios = ttk.Treeview(frameTabla, columns=(1, 2, 3), show="headings", height=15)
tablaUsuarios.pack()

tablaUsuarios.heading(1, text="ID")
tablaUsuarios.column(1, width=40, anchor=CENTER)

tablaUsuarios.heading(2, text="Nombre")
tablaUsuarios.column(2, width=200, anchor=CENTER)

tablaUsuarios.heading(3, text="Correo")
tablaUsuarios.column(3, width=250, anchor=CENTER)

btnCargarUsuarios = Button(pestaña3, text="Cargar Usuarios", command=cargar_usuarios).pack()

#Pestaña 4: Actualizar Usuarios
titulo4=Label(pestaña4, text="Actualizar Usuario", fg="green", font=("Modern", 18)).pack()

varid_actualizar=tk.StringVar()
lblid_actualizar=Label(pestaña4, text="ID del Usuario que se desea actualizar: ").pack()
txtid_actualizar=Entry(pestaña4, textvariable=varid_actualizar).pack()

varNom_actualizar=tk.StringVar()
lblNom_actualizar=Label(pestaña4, text="Nuevo nombre: ").pack()
txtNom_actualizar=Entry(pestaña4, textvariable=varNom_actualizar).pack()

varCorreo_actualizar=tk.StringVar()
lblCorreo=Label(pestaña4, text="Nuevo correo electrónico: ").pack()
txtCorreo=Entry(pestaña4, textvariable=varCorreo_actualizar).pack()

varContra_actualizar=tk.StringVar()
lblContra=Label(pestaña4, text="Nueva contraseña: ").pack()
txtContra=Entry(pestaña4, textvariable=varContra_actualizar).pack()

btnActualizar=Button(pestaña4, text="Actualizar Usuario", command=actualizar_usuarios).pack()

#Pestaña 5: Eliminar un usuario
titulo5=Label(pestaña5, text="Eliminar Usuario", fg="red", font=("Modern", 18)).pack()

varid_eliminar=tk.StringVar()
lblid_eliminar=Label(pestaña5, text="ID del usuario que desea eliminar: ").pack()
txtid_eliminar=Entry(pestaña5, textvariable=varid_eliminar).pack()

btnEliminar=Button(pestaña5, text="Eliminar Usuario",command=elimina_usuario).pack()

# Cargar usuarios al iniciar la pestaña
cargar_usuarios()

panel.add(pestaña1, text="Formulario de Usuarios")
panel.add(pestaña2, text="Buscar Usuario ")
panel.add(pestaña3, text="Consultar Usuarios")
panel.add(pestaña4, text="Actualizar Usuario")
panel.add(pestaña5, text="Eliminar Usuario")
Ventana.mainloop()
