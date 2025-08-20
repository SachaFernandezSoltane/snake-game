import asyncio
import pygame
from pygame import Vector2
from src.apple import Apple
from src.snake import Snake

class Game:
    def __init__(self):
        pygame.init()
        self.cell_size = 30
        self.number_of_cells = 25
        self.screen = pygame.display.set_mode(
            (self.cell_size * self.number_of_cells, self.cell_size * self.number_of_cells)
        )
        pygame.display.set_caption("Snake")
        self.running = True
        self.apple = Apple(self.cell_size, self.number_of_cells)
        self.snake = Snake(self.cell_size, self.number_of_cells)
        self.game_status = 'RUNNING'

    async def run_async(self):
        asyncio.create_task(self.snake_loop())

        while self.running:
            if self.game_status == 'RUNNING':
                self.draw()
                self.handle_events()
                self.check_victory()
                self.check_collision()
                self.check_himself_collision()
                self.check_outside_collision()
            else:
                self.start_game()

            pygame.display.flip()
            await asyncio.sleep(0)

        pygame.quit()

    async def snake_loop(self):
        while self.running:
            if self.game_status == 'RUNNING':
                self.snake.update()
            await asyncio.sleep(0.25)  # 250 ms

    def start_game(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.game_status = 'RUNNING'

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.snake.direction != Vector2(1, 0):
                    self.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT and self.snake.direction != Vector2(-1, 0):
                    self.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_UP and self.snake.direction != Vector2(0, 1):
                    self.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN and self.snake.direction != Vector2(0, -1):
                    self.snake.direction = Vector2(0, 1)

    def check_collision(self):
        if self.snake.body[0] == self.apple.pos:
            self.apple.set_random_position(self.snake.body)
            self.snake.add_segment = True

    def check_himself_collision(self):
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over()

    def check_outside_collision(self):
        head = self.snake.body[0]
        if head.x < 0 or head.x >= self.number_of_cells or head.y < 0 or head.y >= self.number_of_cells:
            self.game_over()

    def draw(self):
        self.screen.fill((173, 204, 96))
        self.snake.draw(self.screen)
        self.apple.draw(self.screen)

    def game_over(self):
        self.snake.reset_position()
        self.apple.set_random_position(self.snake.body)
        self.draw()
        self.game_status = 'STOPPED'
        pygame.display.flip()

    def check_victory(self):
        if len(self.snake.body) == self.number_of_cells * self.number_of_cells:
            self.victory()

    def victory(self):
        self.draw()
        font = pygame.font.Font(None, 60)
        text = font.render("YOU WIN!", True, (255, 215, 0))
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        self.game_status = 'VICTORY'
