import sqlite3
from tkinter import *
from tkinter import messagebox
import examen
import tkinter as tk
class Banco:
    def __init__(self):
        self.conexion = sqlite3.connect("BD_Banco")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS TBCuentas (IDCuenta INTEGER PRIMARY KEY AUTOINCREMENT, NoCuenta INTEGER, Saldo INTEGER)")

    def __del__(self):
        self.conexion.close()

    def agregar_cuenta(self, cuenta, saldo):
        self.cursor.execute("INSERT INTO TBCuentas (NoCuenta, Saldo) VALUES (?, ?)", (cuenta, saldo))
        self.conexion.commit()

    def consultar_cuenta(self, id_cuenta):
        self.cursor.execute("SELECT * FROM TBCuentas WHERE IDCuenta = ?", (id_cuenta,))
        return self.cursor.fetchone()

    def actualizar_cuenta(self, id_cuenta, nueva_cuenta, nuevo_saldo):
        self.cursor.execute("UPDATE TBCuentas SET NoCuenta = ?, Saldo = ? WHERE IDCuenta = ?", (nueva_cuenta, nuevo_saldo, id_cuenta))
        self.conexion.commit()

    def consultar_cuentas(self):
        self.cursor.execute("SELECT * FROM TBCuentas")
        return self.cursor.fetchall()

    def cerrar(self):
        self.conexion.close()
class GUI:
    def __init__(self):
        self.banco = Banco()

        
        self.window = Tk()
        self.window.title("Banco")
        self.window.geometry("400x500")
        self.window.resizable(False, False)

        # Etiqueta y campo de entrada para número de cuenta
        self.lbl_cuenta = Label(self.window, text="Número de cuenta:")
        self.lbl_cuenta.pack(side=TOP, pady=10)
        self.ent_cuenta = Entry(self.window)
        self.ent_cuenta.pack(side=TOP)

        # Etiqueta y campo de entrada para saldo
        self.lbl_saldo = Label(self.window, text="Saldo:")
        self.lbl_saldo.pack(side=TOP, pady=10)
        self.ent_saldo = Entry(self.window)
        self.ent_saldo.pack(side=TOP)

        # Botón para agregar cuenta
        self.btn_agregar = Button(self.window, text="Agregar cuenta", command=self.agregar_cuenta)
        self.btn_agregar.pack(side=TOP, pady=10)

        # Lista de cuentas
        self.cuentas_list = Listbox(self.window)
        self.cuentas_list.pack(side=LEFT, fill=BOTH, expand=True)
        
        # Botón para mostrar cuentas
        self.btn_mostrar_cuentas = Button(self.window, text="Mostrar cuentas", command=self.consultar_cuentas)
        self.btn_mostrar_cuentas.pack(side=TOP, pady=10)
        
        # Widgets para actualizar cuenta
        self.lbl_id_cuenta = Label(self.window, text="ID de cuenta:")
        self.lbl_id_cuenta.pack(side=TOP, pady=10)
        self.ent_id_cuenta = Entry(self.window)
        self.ent_id_cuenta.pack(side=TOP)
        self.lbl_nueva_cuenta = Label(self.window, text="Nueva cuenta:")
        self.lbl_nueva_cuenta.pack(side=TOP)
        self.ent_nueva_cuenta = Entry(self.window)
        self.ent_nueva_cuenta.pack(side=TOP)
        self.lbl_nuevo_saldo = Label(self.window, text="Nuevo saldo:")
        self.lbl_nuevo_saldo.pack(side=TOP)
        self.ent_nuevo_saldo = Entry(self.window)
        self.ent_nuevo_saldo.pack(side=TOP)
        self.btn_actualizar = Button(self.window, text="Actualizar cuenta", command=self.actualizar_cuenta)
        self.btn_actualizar.pack(side=TOP, pady=10)

        self.window.mainloop()

    def agregar_cuenta(self):
        cuenta = self.ent_cuenta.get()
        saldo = self.ent_saldo.get()

        if cuenta and saldo:
            self.banco.agregar_cuenta(cuenta, saldo)
            messagebox.showinfo("Cuenta agregada", "La cuenta se ha agregado correctamente")
            self.ent_cuenta.delete(0, END)
            self.ent_saldo.delete(0, END)
            self.cuentas_list.insert(END, (cuenta, saldo))
        else:
            messagebox.showwarning("Error", "Los campos número de cuenta y saldo son requeridos")

    def consultar_cuentas(self):
        self.cuentas_list.delete(0, END)
        cuentas = self.banco.consultar_cuentas()
        for cuenta in cuentas:
            self.cuentas_list.insert(END, cuenta)

    def actualizar_cuenta(self):
        id_cuenta = self.ent_id_cuenta.get()
        nueva_cuenta = self.ent_nueva_cuenta.get()
        nuevo_saldo = self.ent_nuevo_saldo.get()

        if id_cuenta and nueva_cuenta and nuevo_saldo:
            cuenta_existente = self.banco.consultar_cuenta(id_cuenta)
        if cuenta_existente:
            self.banco.actualizar_cuenta(id_cuenta, nueva_cuenta, nuevo_saldo)
            messagebox.showinfo("Cuenta actualizada", "La cuenta se ha actualizado correctamente")
            self.ent_id_cuenta.delete(0, END)
            self.ent_nueva_cuenta.delete(0, END)
            self.ent_nuevo_saldo.delete(0, END)
            self.consultar_cuentas()
        else:
            messagebox.showwarning("Error", "No existe una cuenta con el ID especificado")

    def cerrar_ventana(self):
        self.banco.cerrar()
        self.window.destroy()

gui = GUI()
gui.banco.cerrar()
