import pygame
from cube import Cube

class Snake(Cube):
    body = []

    def __init__(self, color, pos):
        self.color = color

