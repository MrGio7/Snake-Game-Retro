import pygame

class Messege():
    def __init__(self):
        pass

    def message(self, screen, text, size, color, cord):
        font = pygame.font.SysFont(None, size)
        text = font.render(text, True, color)
        screen.blit(text, cord)