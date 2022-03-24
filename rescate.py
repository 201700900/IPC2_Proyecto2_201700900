import cargar
import city

dronActual = None
cityActual = None
civilActual = None


def chooseDron(dronTipo):
    global dronActual

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
    print(dronActual)
chooseDron(cargar.ChapinRescue)

def chooseCity():
    global cityActual
    n=0
    for ciudad in cargar.ListaCiudades:
        n+=1
        ciudad.gConsola(n)
    op = int(input("\033[;34m"+"Introduce el numero de ciudad para la misión: "+'\033[0;m'))
    cityActual = cargar.ListaCiudades[int(op)-1]
    cityActual.gConsola(op)
chooseCity()

def chooseCivil():
    global civilActual