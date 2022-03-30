import os
import linkedList as lista
import imageio
 

def crear():

    # Ubicación de la base de datos
    path = 'C:/Users/gujho/OneDrive/Documentos/1SEM2022/IPC2/LAB/IPC2_Proyecto2_201700900/cargar.py'
    archivos = sorted(os.listdir(path))
    img_array = lista.LinkedList()

    #Leer todos los archivos formato imagen desde path
    for x in range(0, len(archivos)):
        nomArchivo = archivos[x]
        dirArchivo = path + str(nomArchivo)
        
        #Asignar a variable leer_imagen, el nombre de cada imagen
        leer_imagen = imageio.imread(dirArchivo)
        
        # añadir imágenes al arreglo img_array
        img_array.Append(leer_imagen)
        
    #Guardar Gif
    imageio.mimwrite('Gato.gif', img_array, 'GIF', duration=0.5)