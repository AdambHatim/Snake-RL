import pygame
from collections import deque

from Snake import Snake
from Food import Food
from Board import Board
from Rules import Rules
from Game import Game
from Renderer import Renderer


def main():
    pygame.init()
    clock = pygame.time.Clock()

    # --- paramètres ---
    CELL_SIZE = 30
    X_CASES = 20
    Y_CASES = 20
    FPS = 8

    BOARD_COLOR = (30, 30, 30)
    SNAKE_COLOR = (0, 200, 0)
    FOOD_COLOR  = (200, 0, 0)

    # --- initialisation des objets ---
    board = Board(X_CASES, Y_CASES)

    snake_body = deque([(5, 10), (6, 10), (7, 10)])
    snake = Snake(direction="x+", Snake_dequeue=snake_body)

    food = Food(position=(10, 10))

    rules = Rules(board, food, snake)
    game = Game(board, snake, food, rules)

    renderer = Renderer(
        cell_size=CELL_SIZE,
        x_cases=X_CASES,
        y_cases=Y_CASES,
        Board_color=BOARD_COLOR,
        Snake_color=SNAKE_COLOR,
        Food_color=FOOD_COLOR
    )

    running = True

    # --- boucle principale ---
    while running:
        clock.tick(FPS)

        action = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    action = "y-"
                elif event.key == pygame.K_DOWN:
                    action = "y+"
                elif event.key == pygame.K_LEFT:
                    action = "x-"
                elif event.key == pygame.K_RIGHT:
                    action = "x+"

        # --- tick logique ---
        game.step(action)

        if game.is_game_over():
            print("GAME OVER — score :", game.score)
            running = False

        # --- rendu ---
        renderer.screen.fill(BOARD_COLOR)
        renderer.show(
            snake_queue=snake.get_Snake_dequeue(),
            Food_position=food.get_position()
        )
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
