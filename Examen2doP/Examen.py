from tkinter import *
from tkinter import messagebox
import random
ventana=Tk()


def entrada(nombre, APP, APM, Fecha, Carrera):
        año_curso =23
        año_curso=str(año_curso)
        año_nacimiento=Fecha[-2:]
        año_nacimiento=str(año_nacimiento)
        letra_nombre = nombre[0].upper()
        letras_apellidos = (APP[:3] + APM[:3]).upper()
        letras_carrera = Carrera[:3].upper()
        randomm = str(random.randint(100, 999))
        matricula=letras_carrera+año_curso+año_nacimiento+letra_nombre+letras_apellidos+randomm
        matricula=matricula.upper()
        return matricula
        
def mostrar_matricula():
        
        nombre = entrada_nombre.get().strip()
        app = entrada_Ap_paterno.get().strip()
        apm = entrada_Ap_materno.get().strip()
        fecha = entrada_fecha.get().strip()
        carrera = entrada_Carrera.get().strip() 
        
        if nombre and app and apm and fecha and carrera:
                matricula = entrada(nombre, app, apm, fecha, carrera)

                messagebox.showinfo("Matrícula Generada", matricula)
        else:
        
                messagebox.showerror("Error", "Por favor complete todos los campos.")
        
ventana.title('Examen Segundo Parcial')
ventana.geometry("600x250")
ventana.resizable(False, False)
ventana.config(bg="White")
etiqueta_nombre = Label(ventana, text="Nombre:")
etiqueta_nombre.pack()
entrada_nombre = Entry(ventana)
entrada_nombre.pack()

etiqueta_Ap_paterno= Label(ventana, text="Apellido Paterno:")
etiqueta_Ap_paterno.pack()
entrada_Ap_paterno = Entry(ventana)
entrada_Ap_paterno.pack()
        
etiqueta_Ap_materno= Label(ventana, text="Apellido Materno:")
etiqueta_Ap_materno.pack()
entrada_Ap_materno = Entry(ventana)
entrada_Ap_materno.pack()
        
etiqueta_fecha= Label(ventana, text="Año de Nacimiento:")
etiqueta_fecha.pack()
entrada_fecha = Entry(ventana)
entrada_fecha.pack()
        
etiqueta_Carrera= Label(ventana, text="Carrera:")
etiqueta_Carrera.pack()
entrada_Carrera = Entry(ventana)
entrada_Carrera.pack()

boton_generar = Button(ventana, text="Generar Matrícula", command=mostrar_matricula)
boton_generar.pack()

ventana.mainloop()