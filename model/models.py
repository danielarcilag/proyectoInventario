
class cliente:
    def __init__(self,nombre,ciudad):
        self.nombre = nombre
        self.ciudad = ciudad


class produto:
    def __init__(self,referencia,tipo,precio,cantiadad_inventario):
        self.referencia = referencia
        self.tipo = tipo
        self.precio = precio
        self.cantidad_inventario = cantiadad_inventario

class pedido:
    def __init__(self,id_cliente,referencia,cantidad):
        self.id_cliente = id_cliente
        self.referencia = referencia
        self.cantidad = cantidad