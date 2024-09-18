import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jogo do Dinossauro')

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Parâmetros do dinossauro
dino_width = 40
dino_height = 60
dino_x = 50
dino_y = SCREEN_HEIGHT - dino_height
dino_velocity = 5
is_jumping = False
jump_count = 10

# Parâmetros dos obstáculos
obstacle_width = 20
obstacle_height = 40
obstacle_velocity = 10
obstacle_frequency = 1500  # Milissegundos
last_obstacle_time = pygame.time.get_ticks()
obstacles = []

# Fonte para o texto
font = pygame.font.SysFont(None, 35)

def draw_dino(x, y):
    pygame.draw.rect(screen, BLACK, [x, y, dino_width, dino_height])

def draw_obstacle(x, y):
    pygame.draw.rect(screen, GREEN, [x, y, obstacle_width, obstacle_height])

def display_score(score):
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [10, 10])

def game_loop():
    global is_jumping, jump_count
    clock = pygame.time.Clock()
    running = True
    score = 0
    obstacle_timer = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not is_jumping:
            is_jumping = True

        if is_jumping:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                dino_y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                is_jumping = False
                jump_count = 10

        screen.fill(WHITE)

        # Atualizar obstáculos
        current_time = pygame.time.get_ticks()
        if current_time - obstacle_timer > obstacle_frequency:
            obstacle_x = SCREEN_WIDTH
            obstacle_y = SCREEN_HEIGHT - obstacle_height
            obstacles.append([obstacle_x, obstacle_y])
            obstacle_timer = current_time

        # Mover e desenhar obstáculos
        for obstacle in obstacles:
            obstacle[0] -= obstacle_velocity
            draw_obstacle(obstacle[0], obstacle[1])

        # Remover obstáculos fora da tela
        obstacles = [obstacle for obstacle in obstacles if obstacle[0] > -obstacle_width]

        # Verificar colisões
        for obstacle in obstacles:
            if dino_x + dino_width > obstacle[0] and dino_x < obstacle[0] + obstacle_width:
                if dino_y + dino_height > obstacle[1]:
                    running = False

        draw_dino(dino_x, dino_y)
        display_score(score)
        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    game_loop()

#git de uma aluna desatenta: Ana Beatriz Camassuti Franciscatto