import pygame

class Renderer:
    def __init__(self, cell_size,  x_cases, y_cases, Board_color, Snake_color, Food_color):

        self.cell_size = cell_size
        self.Board_color = Board_color
        self.Snake_color = Snake_color
        self.Food_color = Food_color
        self.x_cases = x_cases
        self.y_cases = y_cases

    def show(self, snake_dequeue, Food_position):
    
        screen = pygame.display.set_mode((self.cell_size * self.x_cases, self.cell_size * self.y_cases))
        screen.fill(self.Board_color)

        x_food, y_food = Food_position
        x_pos, y_pos = x_food * self.cell_size, y_food * self.cell_size
        pygame.draw.rect(screen, self.Food_color, (x_pos, y_pos, self.cell_size, self.cell_size))

        
        for x_snake ,y_snake in snake_dequeue:
            x_pos, y_pos = x_snake * self.cell_size, y_snake * self.cell_size
            pygame.draw.rect(screen, self.Snake_color, (x_pos, y_pos, self.cell_size, self.cell_size))



