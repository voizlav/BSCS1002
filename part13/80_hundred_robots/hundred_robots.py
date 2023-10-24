import pygame

WIDTH = 640
HEIGHT = 480

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

robot = pygame.image.load("robot.png")
w = robot.get_width()
h = robot.get_height()

window.fill((0, 0, 0))

indent = w
for row in range(0, 10):
    for col in range(0, 10):
        indent += 10 if col == 0 else 0
        window.blit(robot, (indent + (w - 10) * col, h + (h / 4 * row)))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
