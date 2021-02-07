import pygame
from snake import Snake

class Messege(Snake):
    def __init__(self):
        super().__init__()

    def message(self, screen, text, size, color, cord):
        font = pygame.font.SysFont(None, size)
        text = font.render(text, True, color)
        screen.blit(text, cord)

    def play_again(self, screen, text, size, color, cord):
            
        font = pygame.font.SysFont(None, size)
        text = font.render(text, True, color)
        screen.blit(text, cord)