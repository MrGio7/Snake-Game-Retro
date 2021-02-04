import pygame

class Cube:
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.movex = 0
        self.movey = 0
        self.rect = pygame.Rect(self.posx + 1, self.posy + 1, 24, 24)
        
    def draw_cube(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)

    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:
            self.movex = 0
            self.movey = 25
            
        if key[pygame.K_UP]:
            self.movex = 0
            self.movey = -25
            
        if key[pygame.K_LEFT]:
            self.movex = -25
            self.movey = 0
            
        if key[pygame.K_RIGHT]:
            self.movex = 25
            self.movey = 0
        
        self.rect.move_ip(self.movex, self.movey)