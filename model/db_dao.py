import sqlite3

def executeQuery(query):
    conx = sqlite3.connect("db/testdb.db")
    cursor = conx.cursor()
    
    try:
        cursor.execute(query)
        conx.commit()
        print("guardado")
    except Exception as e:
        conx.rollback()
        print(f'error: {e}')
    finally:
        cursor.close()
        conx.close()

def crearCliente(cliente):
    query=f"INSERT INTO Clientes (nombre,ciudad) VALUES ('{cliente.nombre}','{cliente.ciudad}')"
    executeQuery(query)

def borrarCliente(cliente):
    query=f"DELETE FROM Clientes WHERE id_cliente=1"
    executeQuery(query)

