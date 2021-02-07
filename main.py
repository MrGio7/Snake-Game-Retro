import pygame
from cube import Cube
from snake import Snake
from messege import Messege

pygame.init()

##SCREEN
screen_width = 500
screen = pygame.display.set_mode([screen_width, screen_width])
pygame.display.set_caption("Snake BY Mr.Gio7")

##COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255,255,0)

##LOOP
done = False
clock = pygame.time.Clock()

##DRAWING
rows = 20

##OBJECTS
s = Snake()
m = Messege()

def drawGrid(surface):
    y = 0
    distance = screen_width / rows
    for i in range(rows):
        y += distance
        pygame.draw.line(surface, WHITE, [0, y], [500, y], 1)
        pygame.draw.line(surface, WHITE, [y, 0], [y, 500], 1)


while not done:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    drawGrid(screen)
    
    if s.bite == False:
        screen.fill(BLACK)
        drawGrid(screen)
        s.move()
        s.draw_snake(screen, RED)
        s.random_cube(screen, YELLOW)
    elif s.bite == True:
        screen.fill(BLACK)
        m.message(screen, "Game Over", 100, WHITE, (60, 50))  
        m.message(screen, s.get_score(), 60, WHITE, (120, 158))
        m.message(screen, "Select Speed", 70, WHITE, (125, 250))
        m.message(screen, "Play Again", 70, WHITE, (125, 375))
        m.message(screen, "Press Space", 30, WHITE, (185, 425))
        s.reset(screen, WHITE)

    pygame.display.update()

pygame.quit()