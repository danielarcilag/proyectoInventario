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

def busqueda(query):
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


def crearClienteDao(cliente):
    query=f"INSERT INTO Clientes (nombre,ciudad) VALUES ('{cliente.nombre}','{cliente.ciudad}')"
    executeQuery(query)

def eliminarClienteDao(nombre):
    query=f"DELETE FROM Clientes WHERE nombre='{nombre}'"
    executeQuery(query)

def verClientesDao():
    query = f"SELECT * FROM Clientes"
    return busqueda(query)

def verIdClienteDao(nombre):
    query = f"SELECT id_cliente FROM Clientes WHERE nombre='{nombre}'"
    return busqueda(query)[0][0]

def modificarClienteDao(id_cliente,nombre,ciudad):
    query = f"UPDATE Clientes SET nombre = '{nombre}',ciudad = '{ciudad}' WHERE id_cliente = {id_cliente}" 
    executeQuery(query)

def crearProductoDao(producto):
    query=f"INSERT INTO Productos (referencia,tipo,precio,cantidad_inventario) VALUES ('{producto.referencia}','{producto.tipo}','{producto.precio}','{producto.cantidad_inventario}')"
    executeQuery(query)

def verProductosDao():
    query = f"SELECT referencia FROM Productos"
    return busqueda(query)

def eliminarProductoDao(referencia):
    query=f"DELETE FROM Productos WHERE referencia='{referencia}'"
    executeQuery(query)

def verPrecioProductosDao(referencia):
    query = f"SELECT precio FROM Productos WHERE referencia = '{referencia}'"
    return busqueda(query)[0][0] 

def crearPedidoDao(id_cliente,listaPedido):
    for i in range(len(listaPedido)):
        query= f"INSERT INTO Pedidos (id_cliente,referencia,cantidad) VALUES ('{id_cliente}','{listaPedido[i].referencia }','{listaPedido[i].cantidad_inventario}')"
        executeQuery(query)

def eliminarPedidoDao(nombre):
    id_cliente = verIdClienteDao(nombre)
    query = f"DELETE FROM Pedidos WHERE id_cliente='{id_cliente}'"
    executeQuery(query)

def verPedidosDao(id_cliente):
    query = f"SELECT * FROM Pedidos WHERE id_cliente='{id_cliente}'"
    return busqueda(query)

def verNombreCliente_Pedido():
    query = f"SELECT DISTINCT nombre FROM Clientes,Pedidos WHERE Clientes.id_cliente = Pedidos.id_cliente"
    return busqueda(query)


