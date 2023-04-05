from tkinter import messagebox
import sqlite3
import bcrypt
class controladorBD:
    def __init__(self):
        pass
    
    def ConexionBD(self):
        try:
            conexion= sqlite3.connect("/Users/lajp2/Documents/GitHub/Practica-9/thinter SQL/DB.db")
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
            qrInsert="Insert into TABLA(Nombre,Correo,Contraseña) values(?,?,?)"
            
            cursor.execute(qrInsert, datos)
            conx.commit()
            messagebox.showinfo("Exito", "Se ha guardado el usuario")
            conx.close()
    
    def encriptarCon(self,contra):
        contraPlana= contra
        contraPlana= contraPlana.encode() #Convertir contra a bytes
        sal= bcrypt.gensalt()
        contraHa= bcrypt.hashpw(contraPlana, sal)
        print(contraHa)
        return contraHa
    
    def consultarUsuario(self, id):
        #1.- Preparar la conexión
        conx= self.ConexionBD()
        
        #2.- Verificar que el ID no esté vacio
        if(id==""):
            messagebox.showwarning("Cuidado Usuario", "ID vacio, escribe uno válido")
            conx.close()
        else:
            #3.- Proceder a buscar
            try:
                #4.- Preparar lo necesario para el select
                cursor= conx.cursor()
                sqlSelect= "select * from TABLA where id="+id
                
                #5.- Ejecución y guardado de la consulta
                cursor.execute(sqlSelect)
                RSusuario= cursor.fetchall()
                conx.close()
                
                return RSusuario
            
            except sqlite3.OperationalError:
                print("Error de consulta")
    
    def consultar_usuarios(self):
        conx = self.ConexionBD()
        cursor = conx.cursor()
        sql= "SELECT * FROM TABLA"
        cursor.execute(sql)
        usuarios = cursor.fetchall()
        conx.close()
        return usuarios
    
    def actualizar_usuarios(self, id_usuario, nuevoNom, nuevoCorreo, nuevaContra):
        conx= self.ConexionBD()
        cursor= conx.cursor()
        campos = []
        datos = []
        if nuevoNom != "":  
            campos.append("Nombre=?")
            datos.append(nuevoNom)
        if nuevoCorreo != "":
            campos.append("Correo=?")
            datos.append(nuevoCorreo)
        if nuevaContra != "":
            contra = self.encriptarCon(nuevaContra)
            campos.append("Contraseña=?")
            datos.append(contra)
    
        if campos:
            campos_query = ", ".join(campos)
            query = f"UPDATE TABLA SET {campos_query} WHERE id=?"
            datos.append(id_usuario)
            cursor.execute(query, tuple(datos))
            conx.commit()
            messagebox.showinfo("Exito", "Se ha actualizado el usuario")
        else:
            messagebox.showwarning("Cuidado", "No se ha ingresado información para actualizar")
        cursor.close()
        conx.close()
