import pygame
from player import Player

# Initialize the pygame
pygame.init()
WIDTH, HEIGHT = 800, 600

clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption("총알 피하기")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = Player(WIDTH/2, HEIGHT/2)

# Game Loop
x = 0
running = True
while running:
    
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 게임 창의 X 버튼을 눌렀을 때
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.goto(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.goto(1, 0)
            elif event.key == pygame.K_UP:
                player.goto(0, -1)
            elif event.key == pygame.K_DOWN:
                player.goto(0, 1)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.goto(1, 0)
            elif event.key == pygame.K_RIGHT:
                player.goto(-1, 0)
            elif event.key == pygame.K_UP:
                player.goto(0, 1)
            elif event.key == pygame.K_DOWN:
                player.goto(0, -1)

    screen.fill((0, 0, 0)) # 화면에 검은색 채우기 (RGB - Red, Green, Blue)

    player.update(dt, screen)

    player.draw(screen) # 화면에 player 그리기

    pygame.display.update() # 화면 갱신 (화면에 새로운 그림을 그린다.)