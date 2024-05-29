TAMANNO_LETRA = 20
TAMANNO_LETRA_GRANDE = 40
FPS_inicial = 3

TIEMPO_MAX = int(input("Ingrese el tiempo en segundos con el que desea jugar: "))
## Si el tiempo ingresado es menor a 10 o mayor a 300 vuelve a pedirlo
while TIEMPO_MAX<10 or TIEMPO_MAX>300:
    TIEMPO_MAX = int(input("El tiempo minimo son 10 segundos y el maximo 300: "))

## Configuracion de la pantalla de juego
ANCHO = 800
ALTO = 600

LARGO = int(input("Ingrese el largo de las palabras con las que desea jugar: "))
## Si el largo ingresado es menor a 2 o mayor a 10 vuelve a pedirlo
while LARGO<2 or LARGO>10:
    LARGO = int(input("El largo minimo es 2 y el maximo 10: "))

## Nosotros cambiamos los colores
COLOR_LETRAS = (117,188,243)
COLOR_FONDO = (55,71,79)
COLOR_TEXTO = (103,195,91)
COLOR_TIEMPO_FINAL = (255,66,66)




