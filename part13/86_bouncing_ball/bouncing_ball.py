import pygame

WIDTH = 640
HEIGHT = 480

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

ball = pygame.image.load("ball.png")
w = ball.get_width()
h = ball.get_height()

x, velocity_x = w, 2
y, velocity_y = h, 2

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    x += velocity_x
    y += velocity_y

    if y <= 0:
        velocity_y *= -1

    if x <= 0:
        velocity_x *= -1

    if y + h >= HEIGHT:
        velocity_y *= -1

    if x + w >= WIDTH:
        velocity_x *= -1

    clock.tick(60)
