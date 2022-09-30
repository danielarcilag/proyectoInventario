import sqlite3

class conexion:
    def __init__(self):
        self.baseDeDatos = '.sql3'
        self.conexionDB = sqlite3.connect(self.database)
        self.cursor = self.conexionDB.cursor
