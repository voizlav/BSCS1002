import pygame

WIDTH = 640
HEIGHT = 480

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

robot = pygame.image.load("robot.png")
w = robot.get_width()
h = robot.get_height()

x, velocity_x = 0, 1
y, velocity_y = 0, 1

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    if x <= 0 and y <= 0:
        velocity_x = 1
        velocity_y = 0

    if x + w >= WIDTH and y <= 0:
        velocity_x = 0
        velocity_y = 1

    if x + w >= WIDTH and y + h >= HEIGHT:
        velocity_x = -1
        velocity_y = 0

    if x <= 0 and y + h >= HEIGHT:
        velocity_x = 0
        velocity_y = -1

    x += velocity_x
    y += velocity_y

    clock.tick(60)
