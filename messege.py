import pygame
from snake import Snake

class Messege(Snake):
    def __init__(self):
        super().__init__()
        self.sysfont = pygame.font.get_default_font()
        self.font = pygame.font.SysFont(None, 48)
        self.text = self.font.render("End Game", True, (255, 255, 255))
        self.rect = self.text.get_rect()

    def end_message(self, screen):
        screen.blit(self.text, (25, 25))
