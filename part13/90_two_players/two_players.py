import pygame


class Robot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.direction = 0


WIDTH = 640
HEIGHT = 480

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

robot = pygame.image.load("robot.png")
w = robot.get_width()
h = robot.get_height()

player1 = Robot(0, 0)
player2 = Robot(0, 0)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            # Player 1
            if event.key == pygame.K_LEFT:
                player1.direction = 1
            if event.key == pygame.K_RIGHT:
                player1.direction = 2
            if event.key == pygame.K_UP:
                player1.direction = 3
            if event.key == pygame.K_DOWN:
                player1.direction = 4
            # Player 2
            if event.key == pygame.K_a:
                player2.direction = 1
            if event.key == pygame.K_d:
                player2.direction = 2
            if event.key == pygame.K_w:
                player2.direction = 3
            if event.key == pygame.K_s:
                player2.direction = 4

        if event.type == pygame.KEYUP:
            # Player 1
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                player1.direction = 0
            # Player 2
            if event.key in [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]:
                player2.direction = 0

    # Player 1
    if player1.direction == 1 and player1.x >= 0:
        player1.x -= 2
    if player1.direction == 2 and player1.x + w <= WIDTH:
        player1.x += 2
    if player1.direction == 3 and player1.y >= 0:
        player1.y -= 2
    if player1.direction == 4 and player1.y + h <= HEIGHT:
        player1.y += 2
    # Player 2
    if player2.direction == 1 and player2.x >= 0:
        player2.x -= 2
    if player2.direction == 2 and player2.x + w <= WIDTH:
        player2.x += 2
    if player2.direction == 3 and player2.y >= 0:
        player2.y -= 2
    if player2.direction == 4 and player2.y + h <= HEIGHT:
        player2.y += 2

    window.fill((0, 0, 0))
    window.blit(robot, (player2.x, player2.y))
    window.blit(robot, (player1.x, player1.y))
    pygame.display.flip()

    clock.tick(60)
