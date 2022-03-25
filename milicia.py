

class Militar:
    def __init__(self, fila, columna, combate):
        self.fila = fila
        self.columna = columna
        self.combate = combate

    def __str__(self):
        String = "["+ self.fila + ', '+ self.columna + ', ' + self.combate+ ']'
        return String