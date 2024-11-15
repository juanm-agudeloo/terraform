import pygame
import random
import time

# Inicialización de pygame
pygame.init()

# Configuración de pantalla
SCREEN_W, SCREEN_H = 320, 222
GAME_W, GAME_H = 200, 200
SCORE_W, SCORE_OFFSET = 100, 5
OFFSET_X = (SCREEN_W - SCORE_W - GAME_W - SCORE_OFFSET) // 2
OFFSET_Y = (SCREEN_H - GAME_H) // 2
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Jetpack Bird")

# Colores
COLOR = {
    "bg": (50, 200, 255),
    "bird": (255, 200, 0),
    "hurt": (255, 50, 0),
    "jp": (150, 150, 150),
    "mouth": (255, 100, 0),
    "pipe": (100, 255, 20),
    "line": (0, 0, 0),
    "font1": (60, 60, 60),
    "font2": (255, 255, 255)
}

# Constantes de juego
LINE_W = 2
TARG_FPS = 20
clock = pygame.time.Clock()

# Funciones auxiliares de dibujo
def rect(x, y, w, h, color):
    pygame.draw.rect(screen, color, (int(x), int(y), int(w), int(h)))

def drawBird(bird, hurt_time, flap_time, flap):
    x, y, size = bird["x"], bird["y"], bird["size"]
    bird_color = COLOR["hurt"] if time.time() - hurt_time < 1 else COLOR["bird"]
    rect(x, y, size, size, bird_color)
    # Add other bird parts as in the original code...

# Configuración de puntuación
def actualizeScore(score, best_score):
    font = pygame.font.SysFont(None, 24)
    score_text = font.render(f"Score: {score}", True, COLOR["font2"])
    best_text = font.render(f"Best: {best_score}", True, COLOR["font2"])
    screen.blit(score_text, (OFFSET_X + GAME_W + SCORE_OFFSET, OFFSET_Y + 40))
    screen.blit(best_text, (OFFSET_X + GAME_W + SCORE_OFFSET, OFFSET_Y + 100))

# Creación de pipes
def addPipes(pipes, x, space_size):
    space_y = random.randint(OFFSET_Y, OFFSET_Y + GAME_H - space_size - 20)
    pipes.append([x, OFFSET_Y, 50, space_y])  # Parte superior
    pipes.append([x, OFFSET_Y + space_size + space_y, 50, GAME_H - (space_size + space_y)])  # Parte inferior

# Motor de juego
def gameEngine():
    # Variables de juego
    bird = {"x": 20, "y": OFFSET_Y + GAME_H // 2, "spd_y": 0, "size": 20}
    pipes = []
    score, best_score, life = 0, 0, 3
    hurt_time = flap_time = time.time()
    addPipes(pipes, GAME_W + OFFSET_X, GAME_H // 2)

    running = True
    while running:
        screen.fill(COLOR["bg"])

        # Control de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bird["spd_y"] -= 5

        # Física del pájaro
        bird["spd_y"] += 1
        bird["y"] += bird["spd_y"]
        if bird["y"] < OFFSET_Y:
            bird["y"] = OFFSET_Y
        elif bird["y"] > OFFSET_Y + GAME_H - bird["size"]:
            bird["y"] = OFFSET_Y + GAME_H - bird["size"]
        
        # Dibuja Bird
        drawBird(bird, hurt_time, flap_time, False)

        # Pipes
        for pipe in pipes:
            pipe[0] -= 5
            rect(pipe[0], pipe[1], pipe[2], pipe[3], COLOR["pipe"])

        # Actualiza puntuación y vidas
        actualizeScore(score, best_score)

        pygame.display.flip()
        clock.tick(TARG_FPS)

    pygame.quit()

gameEngine()
