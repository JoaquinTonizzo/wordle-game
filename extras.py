import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    ## Para poder ingresar la letra ñ tenemos que colocar el teclado en ingles y usar K_SEMICOLON
    if key == K_SEMICOLON:
        return("ñ")
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SLASH:
        return("-")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def dibujar(screen, listaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano, correctas, incorrectas, casi, intentos, mensaje):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #Muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (350, 550))

    #Muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))

    #Muestra los mensajes de error si es que lo hay
    screen.blit(defaultFont.render(mensaje, 1, COLOR_TEXTO), (10, ALTO-95))

    #Muestra los intentos restantes que tiene el usuario
    screen.blit(defaultFont.render("Intentos: " + str(intentos), 1, COLOR_TEXTO), (680, 30))

    #Muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    #Muestra las palabras anteriores que arriesgó el usuario
    pos = 0
    for palabra in listaDePalabrasUsuario:
        screen.blit(defaultFontGrande.render(palabra, 1, (225,180,43)), (ANCHO//2-len(palabra)*TAMANNO_LETRA_GRANDE//4,20 + 50 * pos))
        pos += 1

    #Muestra el abcdario y cambia el color de las letras segun la lista en la que están
    abcdario = ["qwertyuiop", "asdfghjklñ", "zxcvbnm"]
    y=0
    for abc in abcdario:
        x = 0
        for letra in abc:
            if letra in correctas:
                color = (0,255,0) ##Verde
            else:
                if letra in casi:
                    color = (255, 255,0) ##Amarillo
                else:
                    if letra in incorrectas:
                        color = (255, 0, 0) ##Rojo
                    else:
                        color = COLOR_LETRAS
            screen.blit(defaultFont.render(letra, 1, color), (10 + x, ALTO/1.5 + y))
            x += TAMANNO_LETRA
        y += TAMANNO_LETRA

##Esta pantalla se muestra cuando el usuario se queda sin tiempo
def perdisteTiempo(screen, palabraCorrecta, puntos, segundos, intentos):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))

    #muestra los intentos restantes
    screen.blit(defaultFont.render("Intentos: " + str(intentos), 1, COLOR_TEXTO), (680, 30))

    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    #muestra la frase segun el caso
    pos = 5
    frase="Perdiste! Te quedaste sin tiempo!"
    screen.blit(defaultFontGrande.render(frase, 1, (225,180,43)), (ANCHO//2-len(frase)*TAMANNO_LETRA_GRANDE//4,20 + 50 * pos))
    pos += 1
    frase1="La palabra era: "+palabraCorrecta
    screen.blit(defaultFontGrande.render(frase1, 1, (225,180,43)), (ANCHO//2-len(frase1)*TAMANNO_LETRA_GRANDE//4,20 + 50 * pos))

##Esta pantalla se muestra cuando el usuario se queda sin intentos
def perdisteIntentos(screen, palabraCorrecta, puntos, segundos, intentos):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))

    #muestra los intentos restantes
    screen.blit(defaultFont.render("Intentos: " + str(intentos), 1, COLOR_TEXTO), (680, 30))

    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    #muestra la frase segun el caso
    pos = 5
    frase="Perdiste! Te quedaste sin intentos!"
    screen.blit(defaultFontGrande.render(frase, 1, (225,180,43)), (ANCHO//2-len(frase)*TAMANNO_LETRA_GRANDE//4,20 + 50 * pos))
    pos += 1
    frase1="La palabra era: "+palabraCorrecta
    screen.blit(defaultFontGrande.render(frase1, 1, (225,180,43)), (ANCHO//2-len(frase1)*TAMANNO_LETRA_GRANDE//4,20 + 50 * pos))
    pos += 1

##Esta pantalla se muestra cuando el usuario acierta la palabra
def ganaste(screen, palabraCorrecta, puntos, segundos, intentos):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))

    #muestra los intentos restantes
    screen.blit(defaultFont.render("Intentos: " + str(intentos), 1, COLOR_TEXTO), (680, 30))

    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    #muestra la frase segun el caso
    pos = 5
    frase="Ganaste!"
    screen.blit(defaultFontGrande.render(frase, 1, (225,180,43)), (ANCHO//2-len(frase)*TAMANNO_LETRA_GRANDE//4,20 + 50 * pos))
    pos += 1
    frase1="La palabra era: "+palabraCorrecta
    screen.blit(defaultFontGrande.render(frase1, 1, (225,180,43)), (ANCHO//2-len(frase1)*TAMANNO_LETRA_GRANDE//4,20 + 50 * pos))
    pos += 1


