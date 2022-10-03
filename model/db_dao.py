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

def busquedaGeneral(query):
    conx = sqlite3.connect("db/testdb.db")
    cursor = conx.cursor()
    
    try:
        cursor.execute(query)
        datos = cursor.fetchall()
        conx.commit()
        print("guardado")
    except Exception as e:
        conx.rollback()
        print(f'error: {e}')
    finally:
        cursor.close()
        conx.close()
    return datos

def busquedaIndividual(query):
    conx = sqlite3.connect("db/testdb.db")
    cursor = conx.cursor()
    
    try:
        cursor.execute(query)
        dato = cursor.fetchone()
        conx.commit()
        print("guardado")
    except Exception as e:
        conx.rollback()
        print(f'error: {e}')
    finally:
        cursor.close()
        conx.close()
    return dato[0]



def crearClienteDao(cliente):
    query=f"INSERT INTO Clientes (nombre,ciudad) VALUES ('{cliente.nombre}','{cliente.ciudad}')"
    executeQuery(query)

def eliminarClienteDao(nombre):
    query=f"DELETE FROM Clientes WHERE nombre='{nombre}'"
    executeQuery(query)

def crearProductoDao(producto):
    query=f"INSERT INTO Productos (referencia,tipo,precio,cantidad_inventario) VALUES ('{producto.referencia}','{producto.tipo}','{producto.precio}','{producto.cantidad_inventario}')"
    executeQuery(query)

def eliminarProductoDao(referencia):
    query=f"DELETE FROM Productos WHERE referencia='{referencia}'"
    executeQuery(query)

def crearPedidoDao(pedido):
    query=f"INSERT INTO Pedidos (id_cliente,referencia,cantidad) VALUES ('{pedido.id_cliente}','{pedido.referencia}','{pedido.cantidad}')"
    executeQuery(query)

def verDatosDao(dato,tabla):
    query = f"SELECT {dato} FROM {tabla}"
    return busquedaGeneral(query)

def verDatoDao(dato,tabla,campo,datoCampo):
    query = f"SELECT {dato} FROM {tabla} WHERE {campo}='{datoCampo}'"
    return busquedaIndividual(query)