
from logging import exception
from model.conexion import conexion


class cliente:
    def __init__(self,nombre,ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

def crearCliente(cliente):
    query = f'INSERT INTO clientes nombre ciudad VALUES {cliente.nombre} {cliente.ciudad}'

    conexion1 = conexion()
    try:
        with conexion:
            with conexion1.cursor as cursor:
                cursor.execute(query)
                print("guardado")
    except exception as e:
        print(f'no se puo {e}')
        conexion.rollback()
    finally:
        conexion1.close()
         
