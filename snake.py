from cube import Cube
import pygame
import random

class Snake(Cube):
    def __init__(self):
        super().__init__()
        self.pos = [250, 250]
        self.body = [[250, 250]]
        self.size = self.screen_width / self.rows - 1
        self.direction = "Right"
        self.update = 0
        self.posx = random.randrange(0, self.screen_width, self.screen_width / self.rows)
        self.posy = random.randrange(0, self.screen_width, self.screen_width / self.rows)
        
    def draw_snake(self, surface, color):
        for square in self.body:
            pygame.draw.rect(surface, color, (square[0] + 1, square[1] + 1, self.size, self.size))

        self.update += 1
        if self.update >= 50:
            if self.direction == "Right":
                self.pos[0] += 25
            elif self.direction == "Left":
                self.pos[0] -= 25
            elif self.direction == "UP":
                self.pos[1] -= 25
            elif self.direction == "Down":
                self.pos[1] += 25

            self.body.append(list(self.pos))
            self.body.pop(0)
            self.update = 0

    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:
            self.direction = "Down"
            
        if key[pygame.K_UP]:
            self.direction = "UP"
            
        if key[pygame.K_LEFT]:
            self.direction = "Left"
            
        if key[pygame.K_RIGHT]:
            self.direction = "Right"

    def random_cube(self, surface, color):
        for square in self.body:
            if [self.posx, self.posy] != [square[0], square[1]]:
                self.draw_cube(surface, color)
            elif [self.posx, self.posy] == [square[0], square[1]]:
                self.posx = random.randrange(0, self.screen_width, self.screen_width / self.rows)
                self.posy = random.randrange(0, self.screen_width, self.screen_width / self.rows)