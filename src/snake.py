import pygame
from pygame import Vector2


class Snake:
    def __init__(self,cell_size, number_of_cells):
        self.cell_size = cell_size
        self.number_of_cells = number_of_cells
        self.body = [Vector2(6, 9),Vector2(5,9)]
        self.direction = Vector2(1,0)
        self.add_segment = False

    def reset_position(self):
        self.body = [Vector2(6, 9),Vector2(5,9)]
        self.direction = Vector2(1,0)


    def draw(self, screen):
        for segment in self.body:
            segment_rect = pygame.Rect(segment.x * self.cell_size, segment.y * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(screen, (43,51,24), segment_rect,0,7)

    def update(self):
        self.body.insert(0, self.body[0] + self.direction)

        if self.add_segment:
            self.add_segment = False
        else:
            self.body.pop()

        pygame.display.flip()

