import pygame

WIDTH = 640
HEIGHT = 480

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

window.fill((0, 0, 0))

for i in range(1, 11):
    window.blit(robot, (robot_width * i, robot_height))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
