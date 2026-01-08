import pygame
from Renderer import Renderer

def renderer_test():
    # --- pygame init (ONCE) ---
    pygame.init()

    # --- test parameters ---
    CELL_SIZE = 30
    X_CASES = 20
    Y_CASES = 20

    BOARD_COLOR = (30, 30, 30)
    SNAKE_COLOR = (0, 200, 0)
    FOOD_COLOR = (200, 0, 0)

    # --- create renderer ---
    renderer = Renderer(
        cell_size=CELL_SIZE,
        x_cases=X_CASES,
        y_cases=Y_CASES,
        Board_color=BOARD_COLOR,
        Snake_color=SNAKE_COLOR,
        Food_color=FOOD_COLOR
    )

    # --- fake game state ---
    snake_queue = [(0, 0), (1, 0), (2, 0)]
    direction = "x+"
    food_position = (10, 8)

    clock = pygame.time.Clock()
    running = True

    # --- main loop ---
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # clear board
        renderer.screen.fill(BOARD_COLOR)
        renderer.show(snake_queue, food_position)

        x_queue, y_queue = snake_queue[-1]
        del snake_queue[0]

        if direction == "x+":
            if x_queue < X_CASES - 1:
                snake_queue.append((x_queue + 1, y_queue))
            else:
                snake_queue.append((x_queue, y_queue + 1))
                direction = "y+"
        
        elif direction == "y+":
            if y_queue < Y_CASES - 1:
                snake_queue.append((x_queue, y_queue + 1))
            else:
                snake_queue.append((x_queue - 1, y_queue))
                direction = "x-"

        elif direction == "x-":
            if x_queue > 0:
                snake_queue.append((x_queue - 1, y_queue))
            
            else:
                snake_queue.append((x_queue, y_queue - 1))
                direction = "y-"

        else:
            if y_queue > 0:
                snake_queue.append((x_queue, y_queue - 1))
            else:
                snake_queue.append((x_queue + 1, y_queue))
                direction = "x+"


        # draw state

        # update display
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


renderer_test()