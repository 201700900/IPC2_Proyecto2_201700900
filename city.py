import graphviz  
import linkedList as lista
class Ciudad:

    def __init__(self, nombre, matriz, filas, columnas, militares):
        self.nombre = nombre
        self.matriz = matriz
        self.filas = int(filas)
        self.columnas = int(columnas)
        self.militares = militares
        self.entradas = lista.LinkedList()
        self.recursos = lista.LinkedList()
        self.civiles = lista.LinkedList()
        self.Plot()
        self.addMili()
    
    def gConsola(self):
        grafica = ''
        nfila = 0
        for fila in self.matriz:
            nfila+=1

            for columna in fila:
                
                if(columna =='*'):# * - intrasitable
                    grafica +='⬛'
                   
                elif(columna == ' '):# transitable
                    grafica +='⬜'

                elif(columna == 'E'):#E - punto de entrada
                    grafica +='🟩'

                elif(columna == 'C'):# C – representa una unidad civil 
                    grafica +='🟦' 

                elif(columna == 'R'):# R – representa un recurso
                    grafica +='🟫' 
                
                elif(columna == 'M'):# R – representa un recurso
                    grafica +='🟥'

                    
                # for unidad in self.militares:
                #     if int(unidad.fila) == nfila and int(unidad.columna) == ncolumna:
                #         grafica = grafica[:-1]
                #         grafica +='🟥'
            grafica+=' '+str(nfila)        
            
            grafica += '\n\t\t'    
        for i in range(1, int(self.columnas)+1):
            if i <10:
                grafica += ' '+str(i)
            else:
                grafica += str(i)

        Tabla="""\
        |     Ciudad: {0}  
        |
        |       {1}
        |
        +---------------------------------------------------------------------+\
        """

        Tabla = (Tabla.format(str(self.nombre), str(grafica),)) 
        print(Tabla)

    def Plot(self):
        nfila = 0
        for fila in self.matriz:
            nfila+=1
            ncolumna = -1
            for columna in fila:
                ncolumna += 1
                   
                if(columna == 'E'):#E - punto de entrada
                    coordenada = lista.LinkedList()
                    coordenada.Append(nfila)
                    coordenada.Append(ncolumna)
                    self.entradas.Append(coordenada) 

                elif(columna == 'C'):# C – representa una unidad civil 
                    coordenada = lista.LinkedList()
                    coordenada.Append(nfila)
                    coordenada.Append(ncolumna)
                    self.civiles.Append(coordenada)  

                elif(columna == 'R'):# R – representa un recurso
                    coordenada = lista.LinkedList()
                    coordenada.Append(nfila)
                    coordenada.Append(ncolumna)
                    self.recursos.Append(coordenada)  
                
                

    def graph(self, titulo):
        entrada = 1
        recurso = 1
        civil = 1
        h = graphviz.Graph(titulo)  
        table = '<<TABLE  border="10" cellspacing="1" cellpadding="40" style="rounded">'
        nfila = 0
        table+='<TR>'
        table+='<TD border="3"  height="40"></TD>'

        for n in range(1, self.columnas+1):
            table+='<TD border="3"  height="40">'+str(n)+'</TD>'
        table+='</TR>'
    
        for fila in self.matriz:
            nfila+=1

            ncolumna = -1
            table += '<TR>'
            table+='<TD border="3"  height="40">'+str(nfila)+'</TD>'

            for columna in fila:
                ncolumna += 1
            
            
                if(columna =='*'):# * - intrasitable

                    table += '<TD  border="3"  height="40" bgcolor="black"></TD>'

                    
                elif(columna == ' '):# transitable
                    table += '<TD  border="1"  height="40" bgcolor="white"></TD>'


                elif(columna == 'E'):#E - punto de entrada
                    table += '<TD  border="3"  height="40" bgcolor="green">'+str(entrada)+'</TD>'
                    entrada+=1

                elif(columna == 'C'):# C – representa una unidad civil 
                    table += '<TD  border="3"  height="40" bgcolor="blue">'+str(civil)+'</TD>'
                    civil+=1

                elif(columna == 'R'):# R – representa un recurso
                    table += '<TD  border="3"  height="40" bgcolor="gray">'+str(recurso)+'</TD>'
                    recurso+=1
                
                elif(columna == 'M'):
                    table += '<TD  border="3"  height="40" bgcolor="red"></TD>'

                
            table += '</TR>'

        table += '</TABLE>>'    

        h.node( 'tab', shape='rect', label = table)
        h.format = 'png'

        h.render(directory='grafica-patrones', view=True).replace('\\', '/')
        'grafica-patrones/'+titulo +'.gv.png'

    def addMili(self):
        nfila = 0
        for fila in self.matriz:
            nfila+=1
            ncolumna = -1
            for columna in fila:
                ncolumna += 1
                for unidad in self.militares:
                    if int(unidad.fila) == nfila and int(unidad.columna) == ncolumna:
                        self.matriz[nfila-1][ncolumna]='M'
      
                