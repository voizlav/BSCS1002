import pygame

WIDTH = 640
HEIGHT = 480

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

robot = pygame.image.load("robot.png")
w = robot.get_width()
h = robot.get_height()

x, y = 0, 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    y += velocity

    if velocity > 0 and y + h >= HEIGHT:
        velocity = -velocity

    if velocity < 0 and y <= 0:
        velocity = -velocity

    clock.tick(60)
