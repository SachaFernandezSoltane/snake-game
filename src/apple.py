import random

import pygame
from pygame import Vector2


class Apple:
    def __init__(self, cell_size, number_of_cells):
        self.cell_size = cell_size
        self.number_of_cells = number_of_cells
        self.x = random.randint(0,  self.number_of_cells -1)
        self.y = random.randint(0,  self.number_of_cells -1)
        self.pos = pygame.Vector2(self.x, self.y)
        self.apple_img = pygame.image.load("graphics/apple.png").convert_alpha()
        self.apple_img = pygame.transform.scale(self.apple_img, (cell_size, cell_size))


    def draw(self, screen):
        apple_rect = pygame.Rect(self.pos.x * self.cell_size, self.pos.y * self.cell_size, self.cell_size, self.cell_size)
        screen.blit(self.apple_img, apple_rect)

    def generate_random_position(self):
        new_random_x = random.randint(0, self.number_of_cells - 1)
        new_random_y = random.randint(0, self.number_of_cells - 1)
        new_pos = Vector2(new_random_x, new_random_y)

        return new_pos

    def set_random_position(self, snake_body):
        new_pos = self.generate_random_position()

        while new_pos in snake_body or new_pos == self.pos:
            new_pos = self.generate_random_position()

        self.pos = new_pos


