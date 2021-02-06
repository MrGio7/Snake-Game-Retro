import pygame

class Cube:
    def __init__(self):
        self.rows = 20
        self.screen_width = 500
        self.posx = 0
        self.posy = 0
        self.rect = pygame.Rect(self.posx + 1, self.posy + 1, 24, 24)
        
    def draw_cube(self, surface, color):
        self.rect = pygame.Rect(self.posx + 1, self.posy + 1, 24, 24)
        pygame.draw.rect(surface, color, self.rect)