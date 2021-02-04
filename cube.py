import pygame

class Cube:
    def __init__(self, surface, pos, color):
        self.surface = surface
        self.pos = pos
        self.color = color
        
    def draw_cube(self, surface, color, surface_width, rows):
        dis = surface_width/rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, color, [i*dis + 1, j*dis + 1, dis - 1, dis - 1])

    def move_cube():
        pygame.Rect.move()