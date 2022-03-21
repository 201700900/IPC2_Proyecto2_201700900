def entrada():

    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print("\033[;31m"+ 'Error, introduce un numero entero.'+'\033[0;m')

    return num

salir = False
opcion = 0

while not salir:

    print("------------------------------------------------------------------------------------------")
    print("Elija una opción.")
    print ("1. Cargar archivos de configuración.")
    print ("2. Misión de rescate.")
    print ("3. Misión de extracción de recursos.")
    print ("4. Salir")
    print("~~~~~~")
    print ("Elige una opcion")
    opcion = entrada()

    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    
    elif opcion == 4:
        salir = True
    else:
        print("\033[;31m"+ 'Introduce un numero entre 1 y 4'+'\033[0;m')


print("\033[;32m"+"FIN"+'\033[0;m')
