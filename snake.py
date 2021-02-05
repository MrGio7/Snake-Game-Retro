import pygame

class Snake():
    def __init__(self):
        self.rows = 20
        self.screen_width = 500
        self.pos = [75, 25]
        self.body = [[75, 25], [50, 25], [25, 25]]
        self.size = self.screen_width / self.rows - 1
        self.direction = "Right"
        self.update = 0
        
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