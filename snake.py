from messege import Messege
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
        self.bite = False
        self.speed = 10
        self.response = 0
        
    def draw_snake(self, surface, color):
        self.update += 1
        for square in self.body:
            pygame.draw.rect(surface, color, (square[0] + 1, square[1] + 1, self.size, self.size))
            if self.body.count(square) > 1 or square[0] > 500 or square[0] < 0 or square[1] < 0 or square[1] > 500:
                self.bite = True
        
        if self.update >= self.speed:
            if self.direction == "Right":
                self.pos[0] += 25
            elif self.direction == "Left":
                self.pos[0] -= 25
            elif self.direction == "UP":
                self.pos[1] -= 25
            elif self.direction == "Down":
                self.pos[1] += 25

            self.body.append(list(self.pos))

            if self.pos != [self.posx, self.posy]:
                self.body.pop(0)
            else:
                pass
            self.update = 0

    def move(self):
        if self.bite == False:
            key = pygame.key.get_pressed()

            if key[pygame.K_DOWN]:
                if self.direction == "UP":
                    pass
                else:
                    self.direction = "Down"
                
            if key[pygame.K_UP]:
                if self.direction == "Down":
                    pass
                else:
                    self.direction = "UP"
                
            if key[pygame.K_LEFT]:
                if self.direction == "Right":
                    pass
                else:
                    self.direction = "Left"
                
            if key[pygame.K_RIGHT]:
                if self.direction == "Left":
                    pass
                else:
                    self.direction = "Right"

    def random_cube(self, surface, color):
        for square in self.body:
            if [self.posx, self.posy] != [square[0], square[1]] and square != [self.posx, self.posy]:
                self.draw_cube(surface, color)
            elif [self.posx, self.posy] == [square[0], square[1]]:
                self.posx = random.randrange(0, self.screen_width, self.screen_width / self.rows)
                self.posy = random.randrange(0, self.screen_width, self.screen_width / self.rows)

    def get_score(self):
        return f"Your Score: {len(self.body)}"

    def reset(self, screen, color):
        key = pygame.key.get_pressed()
        m = Messege()
        speed = "Speed: " + str(int((60 - self. speed) / 5))
        m.message(screen, speed, 70, color, (125, 315))
        self.response += 1
        if key[pygame.K_SPACE]:
            self.pos = [250, 250]
            self.body = [[250, 250]]
            self.direction = "Right"
            self.update = 0
            self.bite = False
        elif key[pygame.K_UP] and self.speed > 5 and self.response > 10:
            self.speed -= 5
            self.response = 0
        elif key[pygame.K_DOWN] and self.speed < 60 and self.response > 10:
            self.speed += 5
            self.response = 0
        else:
            pass