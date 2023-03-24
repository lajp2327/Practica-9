from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    def __init__(self):
        pass
    
    def ConexionBD(self):
        try:
            conexion= sqlite3.connect("C:/Users/lajp2/Documents/GitHub/Practica-9/thinter SQL/DB.db")
            print("Conectado BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    
    def guardar_usuario(self, nom, correo, contra):
        
        conx= self.ConexionBD()
        
        if (nom== "" or correo== "" or contra== ""):
            messagebox.showwarning("Cuidado", "Revisa el formulario")
            conx.close()
        else:
            cursor=conx.cursor()
            conH= self.encriptarCon(contra)
            datos=(nom, correo, conH)
            qrInsert="Insert into TBRegistrados(Nombre,Correo,Contraseña) values(?,?,?)"
            
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Se ha guardado el usuario")
    
    def encriptarCon(self,contra):
        contraPlana= contra
        contraPlana= contraPlana.encode() #Convertir contra a bytes
        sal= bcrypt.gensalt()
        contraHa= bcrypt.hashpw(contraPlana, sal)
        print(contraHa)
        return contraHa