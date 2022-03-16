class Ciudad:

    def __init__(self, nombre, matriz, filas, columnas, militares):
        self.nombre = nombre
        self.matriz = matriz
        self.filas = filas
        self.columnas = columnas
        self.militares = militares

    
    def gRows(self):
        grafica = ''
        nfila = 0
        for fila in self.matriz:
            nfila+=1
            ncolumna = 0
            for columna in fila:
                ncolumna += 1
                
                
                if(columna =='*'):#intrasitable
                    grafica +='⬛'
                   
                elif(columna == ' '):#transitable
                    grafica +='⬜'

                elif(columna == 'E'):#punto de entrada
                    grafica +='🟩' 

                elif(columna == 'C'):#(C – representa una unidad civil) 
                    grafica +='🟦' 

                elif(columna == 'R'):#letra R (R – representa un recurso). 
                    grafica +='🟫'  
                    
                for unidad in self.militares:
                    if int(unidad.fila) == nfila and int(unidad.columna) == ncolumna:
                        temp = grafica
                        grafica = temp[:-1]
                        grafica +='🟥'        
            
            grafica += '\n\t\t'    
        
        Tabla="""\
        |     Ciudad: {0}  
        |
        |       {1}
        |
        +---------------------------------------------------------------------+\
        """

        Tabla = (Tabla.format(str(self.nombre), str(grafica),)) 
        print(Tabla)