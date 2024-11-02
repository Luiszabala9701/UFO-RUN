import pygame, sys, random

pygame.init()
pygame.display.set_caption("UFO RUN")
 
#Configuración de la ventana
ancho = 800
alto = 600
pantalla = pygame.display.set_mode((ancho, alto))

#Configuración del fondo
fondo = pygame.image.load("src/fondo.jpg").convert()
fondo = pygame.transform.smoothscale(fondo, (ancho, alto))

#configuracion sonido y musica
volumen = 0.3
musica_fondo = pygame.mixer.music.load("src/musica_fondo_2.mp3")
sonido_muerte = pygame.mixer.Sound("src/sonido_muerte.mp3")
sonido_puntaje = pygame.mixer.Sound("src/sonido_puntaje.mp3")
sonido_invencible = pygame.mixer.Sound("src/sonido_invencibilidad.mp3")
pygame.mixer.music.set_volume(0.4)
sonido_muerte.set_volume(volumen)
sonido_invencible.set_volume(volumen)
sonido_puntaje.set_volume(volumen)

#Configuración de colores
azul = (50, 120, 240) 
rojo = (100, 5, 5)
verde = (5, 100, 5)

#Configuración de la fuente
fuente = pygame.font.Font("src/slkscr.ttf", 74)
fuente_pequeña = pygame.font.Font("src/slkscr.ttf", 30)

#Configuración del reloj
reloj = pygame.time.Clock()
fps = 80

#Configuración del UFO
ufo = pygame.image.load("src/ufo_principal.png").convert_alpha()
ufo_muerto = pygame.image.load("src/ufo_muerto.png").convert_alpha()
ufo_rojo = pygame.image.load("src/ufo_rojo.png").convert_alpha()
ufo_amarillo = pygame.image.load("src/ufo_amarillo.png").convert_alpha()
ufo_azul = pygame.image.load("src/ufo_azul.png").convert_alpha()
ufo_coord_x = 150
gravedad = 0.25

#Configuración de powerups
invencibilidad = pygame.image.load("src/powerup_star.png").convert_alpha()
invencibilidad = pygame.transform.scale(invencibilidad, (50, 50))
multicolor = [ufo, ufo_rojo, ufo_amarillo, ufo_azul]
movimiento_powerup = 4

#Configuración de pinchos
pincho_anchura = 80
pincho_altura = 400
pincho_superior = pygame.image.load("src/pincho_alto.png").convert_alpha()
pincho_superior = pygame.transform.scale(pincho_superior, (pincho_anchura, pincho_altura))
pincho_inferior = pygame.image.load("src/pincho_bajo.png").convert_alpha()
pincho_inferior = pygame.transform.scale(pincho_inferior, (pincho_anchura, pincho_altura))
pincho_x = ancho

def mostrar_menu():
    while True:
        pantalla.blit(fondo, (0, 0))
        titulo = fuente.render("UFO RUN", True, azul)
        pantalla.blit(titulo, (ancho // 2 - titulo.get_width() // 2, 130))
        
        boton_jugar = pygame.Rect(ancho // 2 - 100, alto // 2 - 50, 200, 50)
        boton_salir = pygame.Rect(ancho // 2 - 100, alto // 2 + 20, 200, 50)
        pygame.draw.rect(pantalla, verde, boton_jugar)
        pygame.draw.rect(pantalla, rojo, boton_salir)
        
        texto_jugar = fuente_pequeña.render("Jugar", True, azul)
        texto_salir = fuente_pequeña.render("Salir", True, azul)
        
        pantalla.blit(texto_jugar, (boton_jugar.x + 50, boton_jugar.y + 10))
        pantalla.blit(texto_salir, (boton_salir.x + 50, boton_salir.y + 10))
        
        pygame.display.flip()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if boton_jugar.collidepoint(evento.pos):
                    return True
                if boton_salir.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()
                
def mostrar_menu_reinicio():
    while True:
        pantalla.blit(fondo, (0, 0))
        ufo_rotado = pygame.transform.rotate(ufo_muerto, 10)
        pantalla.blit(ufo_rotado, rectangulo_ufo.topleft)
        
        powerup = pygame.Rect(invencibilidad_coord_x, invencibilidad_coord_y, 50, 50)
        pantalla.blit(invencibilidad, powerup.topleft)
        
        for pincho in pinchos:
            pincho_superior_x, pincho_superior_y, pincho_inferior_x, pincho_inferior_y, _ = pincho
            pantalla.blit(pincho_superior, (pincho_superior_x, pincho_superior_y))
            pantalla.blit(pincho_inferior, (pincho_inferior_x, pincho_inferior_y))
            
        mensaje = fuente.render("Juego Terminado", True, azul)
        pantalla.blit(mensaje, (ancho // 2 - mensaje.get_width() // 2, 80 ))
        
        texto_puntaje = fuente_pequeña.render(f"Puntaje: {puntaje}", True, azul)
        pantalla.blit(texto_puntaje, (ancho // 2 - texto_puntaje.get_width() // 2, 190))
        
        creditos = fuente_pequeña.render("Creditos", True, azul)
        pantalla.blit(creditos, (20, alto - 150))
        nombre1 = fuente_pequeña.render("Luis Zabala", True, azul)
        pantalla.blit(nombre1, (20, alto - 100))    
        nombre2 = fuente_pequeña.render("Agustin Bustamante", True, azul)
        pantalla.blit(nombre2, (20, alto - 50)) 
        
        boton_reiniciar = pygame.Rect(ancho // 2 - 100, alto // 2 - 50, 200, 50)
        boton_salir = pygame.Rect(ancho // 2 - 100, alto // 2 + 20, 200, 50)
        pygame.draw.rect(pantalla, verde, boton_reiniciar)
        pygame.draw.rect(pantalla, rojo, boton_salir)
        
        texto_reiniciar = fuente_pequeña.render("Reiniciar", True, azul)
        texto_salir = fuente_pequeña.render("Salir", True, azul)
        pantalla.blit(texto_reiniciar, (boton_reiniciar.x + 20, boton_reiniciar.y + 10))
        pantalla.blit(texto_salir, (boton_salir.x + 50, boton_salir.y + 10))
        
        pygame.display.flip()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if boton_reiniciar.collidepoint(evento.pos):
                    return True
                if boton_salir.collidepoint(evento.pos):
                    return False
                
def crear_pinchos(pincho_x):
    brecha_pinchos = random.randint(0, 150)
    pincho_superior_y = -190 - brecha_pinchos
    pincho_inferior_y = alto - pincho_altura + 190 - brecha_pinchos
    return (pincho_x, pincho_superior_y, pincho_x, pincho_inferior_y, False)

def detectar_colision_pincho(ufo, pinchos):
    for pincho in pinchos:
        pincho_superior_x, pincho_superior_y, pincho_inferior_x, pincho_inferior_y, _ = pincho
        pincho_superior = pygame.Rect(pincho_superior_x, pincho_superior_y, pincho_anchura, pincho_altura)
        pincho_inferior = pygame.Rect(pincho_inferior_x, pincho_inferior_y, pincho_anchura, pincho_altura)
        if ufo.colliderect(pincho_superior) or ufo.colliderect(pincho_inferior):
            return True
    return False

def detectar_colision_powerup(ufo, powerup):
    if ufo.colliderect(powerup):
        return True
    else:
        return False
    
jugar = mostrar_menu()
reiniciar_run = True

while jugar:
    pygame.mixer.music.play(-1) 
    ufo_coord_y = alto // 2
    salto = 0
    contador_pinchos = 0
    frecuencia_pinchos = 90 
    movimiento_pinchos = 3 
    pinchos = []
    puntaje = 0
    invencible = False
    tiempo_invencible = 0
    duracion_invencible = 320
    powerup_activo = False
    invencibilidad_coord_x = ancho
    invencibilidad_coord_y = alto // 2
    indice_color = 0
    tiempo_cambio_color = 0
    frecuencia_cambio_color = 120 
    sonido_activo = False
    
    while reiniciar_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                salto = -6
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                salto = -6
        pantalla.blit(fondo, (0, 0))

        #Salto del UFO 
        salto += gravedad
        ufo_coord_y += salto
        
        #Colisiones con los bordes
        if ufo_coord_y >= alto or ufo_coord_y <= 0:
            sonido_muerte.play()
            if invencible:
                sonido_invencible.stop()
            reiniciar_run = False
            
        #Crear pinchos
        contador_pinchos += 1
        if contador_pinchos > frecuencia_pinchos:
            pincho_superior_x, pincho_superior_y, pincho_inferior_x, pincho_inferior_y, contado= crear_pinchos(pincho_x)
            pinchos.append((pincho_superior_x, pincho_superior_y, pincho_inferior_x, pincho_inferior_y, contado))
            contador_pinchos = 0
        
        #Mover pinchos
        nuevos_pinchos = []
        for pincho in pinchos:
            pincho_superior_x, pincho_superior_y, pincho_inferior_x, pincho_inferior_y, contado = pincho
            pincho_superior_x -= movimiento_pinchos
            pincho_inferior_x -= movimiento_pinchos

            if pincho_superior_x + pincho_anchura > 0:
                nuevos_pinchos.append((pincho_superior_x, pincho_superior_y, pincho_inferior_x, pincho_inferior_y, contado))
                if not contado and ufo_coord_x > pincho_superior_x and not sonido_activo:
                    sonido_activo = True
                    sonido_puntaje.play()
                if not contado and ufo_coord_x > pincho_superior_x + pincho_anchura:
                    nuevos_pinchos[-1] = (pincho_superior_x, pincho_superior_y, pincho_inferior_x, pincho_inferior_y, True)
                    puntaje += 1
                    sonido_activo = False
                    if puntaje < 44:
                        if puntaje % 4 == 0:
                            movimiento_pinchos += 0.5
                            frecuencia_pinchos -= 5
                    if puntaje % 4 == 0:
                        powerup_activo = True   
                        powerup = pygame.Rect(invencibilidad_coord_x, invencibilidad_coord_y, 50, 50)
        pinchos = nuevos_pinchos 
        
        tiempo_cambio_color += contador_pinchos
        if tiempo_cambio_color > frecuencia_cambio_color:
            indice_color = (indice_color + 1) % len(multicolor)
            tiempo_cambio_color = 0
        
        #Mostrar pinchos
        for pincho in pinchos:
            pincho_superior_x, pincho_superior_y, pincho_inferior_x, pincho_inferior_y, _ = pincho
            pantalla.blit(pincho_superior, (pincho_superior_x, pincho_superior_y))
            pantalla.blit(pincho_inferior, (pincho_inferior_x, pincho_inferior_y))   
        
        #Rotar UFO
        if salto < 0:
            angulo = -10 
        else:
            angulo = 10
        ufo_rotado = pygame.transform.rotate(ufo, angulo)
        ufo_multicolor_rotado = pygame.transform.rotate(multicolor[indice_color], angulo)
        
        #verificar colisión con los pinchos
        rectangulo_ufo = pygame.Rect(ufo_coord_x, ufo_coord_y, ufo.get_width() -5, ufo.get_height() -5)
        if not invencible:
            pantalla.blit(ufo_rotado, rectangulo_ufo.topleft)
        else:
            pantalla.blit(ufo_multicolor_rotado, rectangulo_ufo.topleft)
            
        #Mover powerup
        if powerup_activo:
            invencibilidad_coord_x -= movimiento_powerup
            powerup.x = invencibilidad_coord_x
            pantalla.blit(invencibilidad, powerup.topleft)
            if detectar_colision_powerup(rectangulo_ufo, powerup):
                sonido_invencible.play()
                invencible = True
                powerup_activo = False
                invencibilidad_coord_x = ancho
            if invencibilidad_coord_x +50 < 0:
                powerup_activo = False
                invencibilidad_coord_x = ancho
                
        if detectar_colision_pincho(rectangulo_ufo, pinchos) and not invencible:
            sonido_muerte.play()
            reiniciar_run = False
        
        if invencible:
            tiempo_invencible += 1
            if tiempo_invencible > duracion_invencible:
                sonido_invencible.stop()
                invencible = False
                tiempo_invencible = 0
                invencibilidad_coord_x = ancho
                invencibilidad_coord_y = alto // 2
        
        texto_puntaje = fuente_pequeña.render(f"Puntaje: {puntaje}", True, azul)
        pantalla.blit(texto_puntaje, (10, 10))
        
        pygame.display.flip()
        reloj.tick(fps)

    if mostrar_menu_reinicio():
        reiniciar_run = True
    else:
        pygame.quit()
        sys.exit()

pygame.quit()
sys.exit()