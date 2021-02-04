import pygame
from cube import Cube

pygame.init()

##SCREEN
screen_width = 500
screen = pygame.display.set_mode([screen_width, screen_width])
pygame.display.set_caption("Snake BY Mr.Gio7")

##COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

##LOOP
done = False
clock = pygame.time.Clock()

##DRAWING
rows = 20

##OBJECTS
s_body = [10, 10]
s_head = Cube(screen, s_body, RED)

def drawGrid(surface):
    y = 0
    distance = screen_width / rows
    for i in range(rows):
        y += distance
        pygame.draw.line(surface, WHITE, [0, y], [500, y], 1)
        pygame.draw.line(surface, WHITE, [y, 0], [y, 500], 1)


while not done:
    clock.tick(10)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    drawGrid(screen)
    s_head.draw_cube(screen, RED, screen_width, rows)
    s_head.move()

    pygame.display.update()

pygame.quit()