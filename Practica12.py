from tkinter import Tk,Button, Frame, messagebox, Label, Entry

ventana=Tk()

class Login:
    def __init__(self, master):
        self.master = master
        master.title("Login con Tkinter")
        master.geometry("400x200")

        self.etiqueta_correo = Label(master, text="Correo electrónico:")
        self.etiqueta_correo.pack()

        self.entrada_correo = Entry(master)
        self.entrada_correo.pack()

        self.etiqueta_contraseña = Label(master, text="Contraseña:")
        self.etiqueta_contraseña.pack()

        self.entrada_contraseña = Entry(master, show="*")
        self.entrada_contraseña.pack()

        self.boton_inicio_sesion = Button(master, text="Iniciar sesión", command=self.validacion)
        self.boton_inicio_sesion.pack()

    def validacion(self):
        correo = self.entrada_correo.get()
        contraseña = self.entrada_contraseña.get()

        if correo == "" or contraseña == "":
            messagebox.showerror("Error", "Ingresa los datos solicitados, por favor.")
        elif correo == "121038819@upq.edu.mx" and contraseña == "L.a.j.p2327":
            messagebox.showinfo("Bienvenido", f"Bienvenido {correo}")
        else:
            messagebox.showerror("Error", "Email y/o contraseña incorrectos.")


run = Login(ventana)
ventana.mainloop()
