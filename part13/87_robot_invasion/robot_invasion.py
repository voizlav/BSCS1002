import pygame
from random import randrange


class Robot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.velocity = 2
        self.direction = 1


WIDTH = 640
HEIGHT = 480

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

robot = pygame.image.load("robot.png")
w = robot.get_width()
h = robot.get_height()
robots = []

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    if len(robots) < 10 and randrange(60) == 1:
        robots.append(Robot(x=randrange(WIDTH - w), y=-h))

    for r in robots:
        if r.direction == 1:
            r.y += r.velocity
            if r.y + h >= HEIGHT:
                r.direction = 2 if r.x > HEIGHT / 2 else 3

        if r.direction == 2:
            r.x += r.velocity
            if r.x - w >= WIDTH:
                robots.remove(r)

        if r.direction == 3:
            r.x -= r.velocity
            if r.x + w < 0:
                robots.remove(r)

        window.blit(robot, (r.x, r.y))

    pygame.display.flip()

    clock.tick(60)
