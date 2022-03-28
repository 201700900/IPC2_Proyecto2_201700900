class Robot:

    def __init__(self, nombre, tipo, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = int(capacidad)
    
    def __str__(self):
        String = "["+ self.nombre + ', '+ self.tipo + ', ' +str(self.capacidad)+ ']'
        return String

    