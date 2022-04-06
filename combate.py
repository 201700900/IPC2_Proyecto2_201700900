from copy import deepcopy
import cargar
import linkedList as lista

dronActual = None
cityActual = None
recursoActual = None
misionID = 0


def chooseDron(dronTipo):
    global dronActual
    if len(dronTipo) == 1:
        dronActual = dronTipo[0]
    elif len(dronTipo)>1: 
        Tabla = """\
        +---------------------------------------------------------------------+
        | No.     Tipo                Nombre                           Combate|
        |---------------------------------------------------------------------|\
        """
        n=0
        for dron in dronTipo:
            n+=1
            Tabla += """\
        
        | {0:<2}     {1:<12}        {2:20}                 {3:>3} 
        |---------------------------------------------------------------------|\
        """
            Tabla = Tabla.format(n, dron.tipo, dron.nombre, dron.capacidad)
        print(Tabla)
        op = int(input("\033[;34m"+"Introduce el numero de robot para la misión: "+'\033[0;m'))
        dronActual = dronTipo[int(op)-1]

def chooseCity():
    global cityActual
    if len(cargar.ListaCiudades) == 1:
        cityActual = cargar.ListaCiudades[0]
        cityActual.gConsola(cityActual.matriz, op)
    elif len(cargar.ListaCiudades)>1: 
        n=0
        for ciudad in cargar.ListaCiudades:
            n+=1
            ciudad.gConsola(ciudad.matriz, n)
        op = int(input("\033[;34m"+"Introduce el numero de ciudad para la misión: "+'\033[0;m'))
        if op > len(cargar.ListaCiudades):
            print("\t\033[;31m"+'Introduce un numero entre 1 y '+str(len(cargar.ListaCiudades))+'\033[0;m')
            chooseCity()
        else:
            cityActual = cargar.ListaCiudades[int(op)-1]
            cityActual.gConsola(cityActual.matriz, op)

def chooseRecurso():
    global recursoActual
    if len(cityActual.recursos) == 1:
        recursoActual = cityActual.recursos[0]
    elif len(cityActual.recursos)>1: 
        Tabla = """\
        +---------------------------------------------------------------------+
        | No.     Coordernada Recurso                                         |
        |---------------------------------------------------------------------|\
        """
        n=0
        for coordeneada in cityActual.recursos:
            n+=1
            Tabla += """\
            
        | {0:<2}            ({1}, {2})
        |---------------------------------------------------------------------|\
        """
            Tabla = Tabla.format(n, coordeneada[0],  coordeneada[1])
        print(Tabla)
        op = int(input("\033[;34m"+"Introduce el numero de recurso para la misión: "+'\033[0;m'))
        recursoActual = cityActual.recursos[int(op)-1]
def chooseEntrada():
    global entradaActual
    if len(cityActual.entradas) == 1:
        entradaActual = cityActual.entradas[0]    

    elif len(cityActual.entradas)>1: 
        Tabla = """\
        +---------------------------------------------------------------------+
        | No.     Coordernada Entrada                                         |
        |---------------------------------------------------------------------|\
        """
        n=0
        for coordeneada in cityActual.entradas:
            n+=1
            Tabla += """\
            
        | {0:<2}            ({1}, {2})
        |---------------------------------------------------------------------|\
        """
            Tabla = Tabla.format(n, coordeneada[0],  coordeneada[1])
        print(Tabla)
        op = int(input("\033[;34m"+"Introduce el numero de Entrada para la misión: "+'\033[0;m'))
        entradaActual = cityActual.entradas[int(op)-1]    

def heuristica(a,b):
    x = abs(a.x - b.x)
    y = abs(a.y - b.y)
    return x+y

class Casilla:
    global cityActual

    def __init__(self, x, y, tipo, c=0):
        self.x = x
        self.y = y
        self.tipo = tipo
        #PESOS
        self.f = 0  #coste total (g+h)
        self.g = 0  #pasos dados
        self.h = 0  #heurística (estimación de lo que queda)
        self.c = c  #combate
        self.vecinos = lista.LinkedList()
        self.padre = None
        self.recorrido = lista.LinkedList()

    def __str__(self):
        String = "["+ str(self.y) + ' X '+ str(self.x) +', tipo: '+str(self.tipo)+']'
        return String

    #MÉTODO QUE CALCULA SUS VECNIOS
    def addVecinos(self):
        if cityActual.escenario[self.y][self.x+1] is not False:
            self.vecinos.Append(cityActual.escenario[self.y][self.x+1])
        if cityActual.escenario[self.y+1] is not False:
            self.vecinos.Append(cityActual.escenario[self.y+1][self.x])
        if cityActual.escenario[self.y][self.x-1] is not False:
            self.vecinos.Append(cityActual.escenario[self.y][self.x-1])
        if cityActual.escenario[self.y-1] is not False:
            self.vecinos.Append(cityActual.escenario[self.y-1][self.x]) 


def pathFinding():
    global entradaActual
    global recursoActual
    global cityActual
    global misionID 
    

    openSet = lista.LinkedList()
    closedSet = lista.LinkedList()
    camino = lista.LinkedList()

    terminado = False

    y = -1
    for fila in cityActual.matriz:
        y+=1
        x = -1
        lfila = lista.LinkedList()
        for columna in fila:
            x += 1
            if columna == ' ' or columna == 'E' or columna == 'R' or columna == 'C'  :
                lfila.Append(Casilla(x,y,0))
                
            elif columna == 'M':
                for mili in cityActual.militares:
                    if int(mili.fila) == y+1 and int(mili.columna) == x+1:
                        lfila.Append(Casilla(x,y,2, int(mili.combate)))
            else:
                lfila.Append(Casilla(x,y,1))
                
        cityActual.escenario.Append(lfila)
    
    
    for fila in cityActual.escenario:
        for columna in fila:
            columna.addVecinos()
    fin = cityActual.escenario[recursoActual[0]-1][recursoActual[1]-1]
    principio = cityActual.escenario[entradaActual[0]-1][entradaActual[1]-1]
    openSet.Append(principio)


    
    #ALGORITO A*

    while terminado != True:# SIGUE HASTA ENCONTRAR SOLUCIÓN

        if len(openSet)>0:
            ganador = 0 #índie o posición dentro de lista openset del ganador

            for i in range(0, len(openSet)): #evaluamos qué OpenSet tiene un menor coste / esfuerzo
                if openSet[i].f < openSet[ganador].f:
                    ganador = i

            actual = openSet[ganador]#Analizamos la casilla ganadora

            if actual == fin:#SI HEMOS LLEGADO AL FINAL BUSCAMOS EL CAMINO DE VUELTA
                temporal = actual
                camino.Append(temporal)
                exito = True
                cityActual.setMision()
                dronCapacidad = deepcopy(dronActual.capacidad)

                while temporal.padre != principio:
                     temporal = temporal.padre
                     camino.Append(temporal)
                
                for spot in reversed(camino):
                    x+=1
                    if cityActual.mision[spot.y][spot.x]=='E':
                        cityActual.mision[spot.y][spot.x]='E+'
                    elif cityActual.mision[spot.y][spot.x]=='C':
                        cityActual.mision[spot.y][spot.x]='C+'  
                    elif cityActual.mision[spot.y][spot.x]=='R':
                        cityActual.mision[spot.y][spot.x]='R+'  

                    elif spot.tipo == 2:
                        print(dronCapacidad)
                        if dronCapacidad >= spot.c:
                            dronCapacidad -= spot.c
                            cityActual.mision[spot.y][spot.x]='M+' 
                            exito = True
                        else:
                            exito = False
                            break
                    else: 
                        cityActual.mision[spot.y][spot.x]='+'





                        
                    cityActual.mision[principio.y][principio.x]='E' 
                    cityActual.mision[fin.y][fin.x]='R'  
                    # cityActual.gMision(str(x))

                if exito:
                    for spot in camino:
                        if spot.tipo == 2:
                            dronActual.capacidad -= spot.c
                            for unidad in cityActual.militares:
                                if unidad.fila == spot.y and unidad.columna == spot.x:
                                    cityActual.militares.Remove(unidad)
                                    cityActual.matriz[spot.y][spot.x] = ' '

                    print("\t\033[;32m"+'CAMINO ENCONTRADO'+'\033[0;m')
                    cityActual.gConsola(cityActual.mision, 1)
                    misionID += 1
                    cityActual.gMision('Misión extracción '+ str(misionID))
                else:
                    print("\t\033[;31m"+'NO HAY CAMINO POSIBLE'+'\033[0;m')
                terminado = True
            else: #SI NO HEMOS LLEGADO AL FINAL, SEGUIMOS
                openSet.Remove(actual)
                closedSet.Append(actual)
                for vecino in actual.vecinos:#RECORRO LOS VECINOS DE MI GANADOR

                    


                    if not closedSet.Buscar(vecino) and vecino.tipo!=1:#SI EL VECINO NO ESTÁ EN CLOSEDSET Y NO ES UNA PARED, HACEMOS LOS CÁLCULOS
                        if actual.tipo == 2:
                            tempG += actual.c
                        else:
                            tempG = actual.g + 1


                        if openSet.Buscar(vecino):#si el vecino está en OpenSet y su peso es mayor
                            if tempG < vecino.g:
                                vecino.g = tempG
                        else:
                            vecino.g = tempG
                            openSet.Append(vecino)

                        vecino.h = heuristica(vecino,fin)
                        vecino.f = vecino.g + vecino.h
                        vecino.padre = actual
        else:
            print("\t\033[;31m"+'NO HAY CAMINO POSIBLE'+'\033[0;m')
            terminado = True    


def mision():
    if len(cargar.ChapinFighter) ==0:
         print("\t\033[;31m"+'NO HAY ChapinFighter CARGADOS'+'\033[0;m')
    else:
        chooseDron(cargar.ChapinFighter)
        if len(cargar.ListaCiudades) == 0:
            print("\t\033[;31m"+'NO HAY CIUDADES CARGADAS'+'\033[0;m')
        else:
            chooseCity()
            if len(cityActual.civiles) == 0:
                print("\t\033[;31m"+'NO HAY RECURSOS EN LA CIUDAD'+'\033[0;m')
            else:

                chooseRecurso()
                chooseEntrada()
                pathFinding() 
