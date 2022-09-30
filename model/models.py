

class cliente:
    def __init__(self,nombre,ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
    
    def __str__(self) -> str:
        return f'nombre: {self.nombre} ciudad: {self.ciudad}'