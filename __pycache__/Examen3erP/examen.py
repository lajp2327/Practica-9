import sqlite3

def create_connection():
    conn = sqlite3.connect('BD_Banco.db')
    return conn

def create_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS TBCuentas
                 (IDCuenta INTEGER PRIMARY KEY AUTOINCREMENT,
                  NoCuenta INTEGER,
                  Saldo INTEGER)''')

def insert_record(conn, no_cuenta, saldo):
    c = conn.cursor()
    c.execute("INSERT INTO TBCuentas (NoCuenta, Saldo) VALUES (?, ?)", (no_cuenta, saldo))
    conn.commit()
