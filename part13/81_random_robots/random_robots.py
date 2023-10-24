import pygame
from random import choice

WIDTH = 640
HEIGHT = 480

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

robot = pygame.image.load("robot.png")
w = robot.get_width()
h = robot.get_height()

w_range = range(WIDTH - w)
h_range = range(HEIGHT - h)

for _ in range(1000):
    window.blit(robot, (choice(w_range), choice(h_range)))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
