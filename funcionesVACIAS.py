from principal import *
from configuracion import *
import random
import math

def nuevaPalabra(lista):
    if lista==[]:
        pass
        ## Si la lista está vacia no hace nada
    else:
        ## Elige una palabra al azar
        palabra=random.choice(lista)
        return palabra.lower()

def lectura(archivo, salida, largo):
    ## Lee el archivo que ya fue abierto y agrega a la salida solo las palabras cuya longitus dea la indicada
    lineas=archivo.readlines()
    for linea in lineas:
        if len(linea)==largo+1:
            salida.append(linea[:-1])

def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
    ## Chequea la palabra ingresada por el usuario y carga las letran en la lista que corresponda según su posición
    for i in range (0,len(palabraCorrecta)):
        if palabraCorrecta[i]==palabra[i]:
            correctas.append(palabra[i])
        else:
            if palabra[i] in palabraCorrecta:
                casi.append(palabra[i])
            else:
                incorrectas.append(palabra[i])
    ## Si la palbra es la correcta devuelve True y sino False
    if palabraCorrecta==palabra:
        return True
    return False









