from tkinter import *
from tkinter import messagebox
from Entrada_examen import *
ventana=Tk()

class Ventana:
    def __init__(self,main):
        self.main=main
        nombre = self.entrada_nombre.get()
        APP = self.entrada_Ap_materno.get()
        APM = self.entrada_Ap_materno.get()
        Fecha= self.entrada_fecha.get()
        Carrera= self.entrada_Carrera.get()
        
        
        main.title('Examen Segundo Parcial')
        main.geometry("600x250")
        main.resizable(False, False)
        main.config(bg="White")
        self.etiqueta_nombre = Label(main, text="Nombre:")
        self.etiqueta_nombre.pack()
        self.entrada_nombre = Entry(main)
        self.entrada_nombre.pack()

        self.etiqueta_Ap_paterno= Label(main, text="Apellido Paterno:")
        self.etiqueta_Ap_paterno.pack()
        self.entrada_Ap_paterno = Entry(main)
        self.entrada_Ap_paterno.pack()
        
        self.etiqueta_Ap_materno= Label(main, text="Apellido Materno:")
        self.etiqueta_Ap_materno.pack()
        self.entrada_Ap_materno = Entry(main)
        self.entrada_Ap_materno.pack()
        
        self.etiqueta_fecha= Label(main, text="Año de Nacimiento:")
        self.etiqueta_fecha.pack()
        self.entrada_fecha = Entry(main)
        self.entrada_fecha.pack()
        
        self.etiqueta_Carrera= Label(main, text="Carrera:")
        self.etiqueta_Carrera.pack()
        self.entrada_Carrera = Entry(main)
        self.entrada_Carrera.pack()

run=Ventana(ventana)
ventana.mainloop()