#! /usr/bin/env python
import os, random, sys, math
import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesVACIAS import *

# Función principal
def main():
    # Centrar la ventana y después inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    # pygame.mixer.init()

    # Preparar la ventana
    pygame.display.set_caption("Encontrar la palabra escondida")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    # Tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0
    palabraUsuario = ""
    listaPalabrasDiccionario = []
    ListaDePalabrasUsuario = []
    correctas = []
    incorrectas = []
    casi = []
    gano = False
    mensaje = ""

    archivo = open("lemario.txt", "r", encoding='latin-1')
    # Lectura del diccionario
    lectura(archivo, listaPalabrasDiccionario, LARGO)

    # Carga la música
    pygame.mixer.music.load('cancion.mp3')
    # Pone play
    pygame.mixer.music.play()

    # Elige una al azar
    palabraCorrecta = nuevaPalabra(listaPalabrasDiccionario)
    intentos = 5

    dibujar(screen, ListaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano, correctas, incorrectas, casi, intentos, mensaje)
    # Mostramos la palabra correcta por consola
    print("La palabra correcta es:", palabraCorrecta)

    while segundos > fps / 1000 and intentos > 0 and not gano:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        # Buscar la tecla apretada del módulo de eventos de pygame
        for e in pygame.event.get():
            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return

            # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                palabraUsuario += letra  # Es la palabra que escribe el usuario
                if e.key == K_BACKSPACE:
                    palabraUsuario = palabraUsuario[0:len(palabraUsuario) - 1]
                if e.key == K_RETURN:
                    if len(palabraCorrecta) != len(palabraUsuario):
                        # Si la palabra ingresada no tiene el largo correspondiente mostramos un mensaje de error
                        palabraUsuario = ""
                        mensaje = "La longitud de la palabra debe ser " + str(LARGO) + ", Ingrese otra."
                    else:
                        if palabraUsuario not in listaPalabrasDiccionario:
                            # Si la palabra ingresada no está en el lemario mostramos un mensaje de error
                            palabraUsuario = ""
                            mensaje = "La palabra no está en la lista, Ingrese otra."
                        else:
                            if palabraUsuario in ListaDePalabrasUsuario:
                                # Si la palabra ingresada ya fue ingresada antes mostramos un mensaje de error
                                palabraUsuario = ""
                                mensaje = "La palabra ya fue ingresada, Ingrese otra."
                            else:
                                # Si no hay ningún problema con la palabra ingresada no mostramos ningún mensaje de error
                                mensaje = ""
                                # Para que el teclado pinte solo las de la última palabra ingresada debemos vaciar las listas después de cada palabra
                                correctas = []
                                incorrectas = []
                                casi = []
                                # Se evalúa si el usuario ganó
                                gano = revision(palabraCorrecta, palabraUsuario, correctas, incorrectas, casi)
                                # Se agrega la palabra ingresada a la lista de palabras ingresadas
                                ListaDePalabrasUsuario.append(palabraUsuario)
                                # Se limpia la entrada
                                palabraUsuario = ""
                                # Se resta un intento
                                intentos -= 1

        segundos = TIEMPO_MAX - pygame.time.get_ticks() / 1000

        # Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        # Dibujar de nuevo todo
        dibujar(screen, ListaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano, correctas, incorrectas, casi, intentos, mensaje)
        pygame.display.flip()

    if gano:
        # Si el usuario ganó suena el sonido correspondiente
        pygame.mixer.music.load('ganaste.mp3')
        pygame.mixer.music.play()
        # Se agrega un punto
        puntos += 1
        # Se limpia la pantalla anterior
        screen.fill(COLOR_FONDO)
        # Se cambia a la pantalla correspondiente
        ganaste(screen, palabraCorrecta, puntos, segundos, intentos)
        pygame.display.flip()
    else:
        if int(segundos) != 0:
            # Si el usuario se quedó sin intentos suena el sonido correspondiente
            pygame.mixer.music.load('perdiste.mp3')
            pygame.mixer.music.play()
            # Se limpia la pantalla anterior
            screen.fill(COLOR_FONDO)
            # Se cambia a la pantalla correspondiente
            perdisteIntentos(screen, palabraCorrecta, puntos, segundos, intentos)
            pygame.display.flip()
        else:
            # Si el usuario se quedó sin tiempo suena el sonido correspondiente
            pygame.mixer.music.load('perdiste.mp3')
            pygame.mixer.music.play()
            # Se limpia la pantalla anterior
            screen.fill(COLOR_FONDO)
            # Se cambia a la pantalla correspondiente
            perdisteTiempo(screen, palabraCorrecta, puntos, segundos, intentos)
            pygame.display.flip()

    while True:
        # Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return

    archivo.close()

# Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
