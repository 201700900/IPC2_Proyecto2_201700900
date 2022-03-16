class Robot:

    def __init__(self, nombre, tipo, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
    
    def __str__(self):
        String = "["+ self.nombre + ' ,'+ self.tipo + ' ,' + self.capacidad+ ']'
        return String

    