from tkinter import Tk,Button,Frame, messagebox

#Declarar funciones para mensajes
def mostrarmensajes():
    messagebox.showinfo("Botón azul", "Presionaste el botón azul")
    messagebox.showerror("Error" , "Todo falló con éxito")
    print(messagebox.askyesnocancel("Pregunta" , "¿Ella jugó con tu corazón?"))

#Función para agregar botones
def agregarBoton():
    GreenButton.config(text="+", bg="green", fg="white")
    NewButton=Button(seccion3, text="Nuevo")
    NewButton.pack()

#Instancia de objeto ventana
ventana= Tk()
ventana.title("Ejemplo de 3 frames")
ventana.geometry("600x400")

#Frames
seccion1=Frame(ventana, bg="red")
seccion1.pack(expand=True, fill='both')
seccion2=Frame(ventana, bg="purple")
seccion2.pack(expand=True, fill='both')
seccion3=Frame(ventana, bg="pink")
seccion3.pack(expand=True, fill='both')

#Botones
Bluebutton= Button(seccion1,text="Botón azul", fg="white" ,bg="blue", command=mostrarmensajes)
Bluebutton.place(x=60, y=60)

YellowButton= Button(seccion2, text="Botón amarillo", fg="black", bg="yellow" )
YellowButton.grid(row=1, column=0)

BlackButton=  Button(seccion2, text="Botón negro", fg="white", bg="black")
BlackButton.grid(row=0 , column=0)

GreenButton= Button(seccion3, text="Botón verde", bg="green", fg="white", height=2, width=10, command=agregarBoton)
GreenButton.pack()

#llamamos al Main
ventana.mainloop()