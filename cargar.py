import xml.etree.ElementTree as ET
import linkedList as lista
import milicia
import city
import dron

ListaCiudades = lista.LinkedList()
ListaRobots = lista.LinkedList()

def leer():
    global ListaCiudades
    global ListaRobots

    path = 'x'#input("Introduzca la dirreción del XML:\n")
    try:
        tree = ET.parse('entrada.xml')
        root = tree.getroot()#configuracion
        ###################################################################################
        for ciudad in root[0]:#root[0] es listaCiudades
            #print(ciudad.tag)#obtener cada ciudad
            malla = lista.LinkedList()
            nombre = ciudad.find('nombre').text
            nfilas = ciudad.find('nombre').attrib['filas']
            ncolumnas = ciudad.find('nombre').attrib['columnas']

            #print(nombre)
            #print(nfilas, 'X', ncolumnas)

            for fila in ciudad.iter('fila'):#obtener cada fila
                columna = lista.LinkedList()
                for c in fila.text:
                    columna.Append(c)
                #print(columna)    
                malla.Append(columna)
                #print(fila.text)

            militares = lista.LinkedList() 

            for unidad in ciudad.iter('unidadMilitar'):#obtener cada unidadMilitar
                ufila = unidad.attrib['fila']
                ucolumna = unidad.attrib['columna']
                poder = unidad.text
                militares.Append(milicia.Militar(ufila, ucolumna, poder))

            ListaCiudades.Append(city.Ciudad(nombre, malla, nfilas, ncolumnas, militares))  
        ####################################################################################
        for robot in root[1]:#root[0] es robots
            #print(robot.tag)#obtener cada robot
            tipo = robot.find('nombre').attrib['tipo']
            #print(tipo)
            nombre = robot.find('nombre').text
            #print(nombre)

            if tipo == "ChapinFighter":
                capacidad = robot.find('nombre').attrib['capacidad']
                #print(capacidad)
                ListaRobots.Append(dron.Robot(nombre, tipo, capacidad))
            else:
                ListaRobots.Append(dron.Robot(nombre, tipo, ''))

            



        print("\033[;32m"+ path + " cargado con exito"+'\033[0;m')

    except:
        print("\033[;31m"+ path, "no encontrado"+'\033[0;m')

leer()
for c in ListaCiudades:

    c.gRows()