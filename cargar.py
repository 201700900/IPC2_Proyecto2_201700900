import xml.etree.ElementTree as ET
import linkedList as lista
import milicia
import city
import dron

ListaCiudades = lista.LinkedList()
ChapinRescue = lista.LinkedList()
ChapinFighter = lista.LinkedList()


def leer():
    global ListaCiudades
    global ChapinRescue
    global ChapinFighter


    path = input("Introduzca la dirreción del XML:\n")
    try:
        tree = ET.parse(path)
        root = tree.getroot()#configuracion
        ###################################################################################
        for ciudad in root[0]:#root[0] es listaCiudades
            #print(ciudad.tag)#obtener cada ciudad
            malla = lista.LinkedList()
            nombre = ciudad.find('nombre').text
            
            is_in_list = False
            index = 0
            for ci in ListaCiudades:#comprobar si la ciudad existe ya en la lista
                if ci.nombre ==  ciudad.find('nombre').text:
                    is_in_list=True
                    break
                index+=1
            
            nfilas = ciudad.find('nombre').attrib['filas']
            ncolumnas = ciudad.find('nombre').attrib['columnas']

            #print(nombre)
            #print(nfilas, 'X', ncolumnas)

            for fila in ciudad.iter('fila'):#obtener cada fila
                columna = lista.LinkedList()
                for c in fila.text: 
                    if c!='"':
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
                
            if is_in_list:
                ListaCiudades[index] = city.Ciudad(nombre, malla, nfilas, ncolumnas, militares)
            else: 
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
                r= False
                for rob in ChapinFighter:
                    if rob.nombre == nombre:
                        rob = dron.Robot(nombre, tipo, capacidad)
                        r = True
                if not r:
                    ChapinFighter.Append(dron.Robot(nombre, tipo, capacidad))
            else:
                r= False
                for rob in ChapinFighter:
                    if rob.nombre == nombre:
                        rob = dron.Robot(nombre, tipo, 0)
                        r = True
                if not r:
                    ChapinRescue.Append(dron.Robot(nombre, tipo, 0))

            



        print("\t\033[;32m"+ path + " cargado con exito"+'\033[0;m')

    except:
        print("\t\033[;31m"+ path, "no encontrado"+'\033[0;m')



