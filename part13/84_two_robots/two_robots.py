import pygame

WIDTH = 640
HEIGHT = 480

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

robot1 = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")
w = robot1.get_width()
h = robot1.get_height()

r1x, r1y = 0, w
r2x, r2y = 0, w * 3

velocity1 = 1
velocity2 = 2

clock = pygame.time.Clock()


def velocity(x: int, w: int, v: int):
    if v > 0 and x + w >= WIDTH:
        return -v
    if v < 0 and x <= 0:
        return -v
    return v


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot1, (r1x, r1y))
    window.blit(robot2, (r2x, r2y))
    pygame.display.flip()

    r1x += velocity1
    velocity1 = velocity(r1x, w, velocity1)

    r2x += velocity2
    velocity2 = velocity(r2x, w, velocity2)

    clock.tick(60)
