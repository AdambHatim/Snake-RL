import numpy as np

def transform_naive_representation(Snake_dequeue, X_cases, Y_cases):
    Snake = np.zeros(X_cases* Y_cases)
    for x,y in Snake_dequeue:
        pos_flatened = X_cases * y + x
        Snake[pos_flatened] = 1

    return Snake
    
def get_possible_directions(direction):
    possible_directions = ["x+", "y+", "x-", "y-"]

    index_direction = possible_directions.index(direction)
    
    possible_direction_1 = possible_directions[(index_direction + 1) % 4]
    possible_direction_2 = possible_directions[(index_direction + 2) % 4]
    possible_direction_3 = possible_directions[(index_direction + 3) % 4]

    return possible_direction_1, possible_direction_2, possible_direction_3


def get_compact_state_version(Snake_flattened):

    state_compact = ''
    for x in Snake_flattened:
        state_compact += str(x)
    return state_compact


def find_state(agent, Snake_dequeue, food_position, direction = "continue"):
    
    State = (tuple(Snake_dequeue), food_position)
    
    val = agent.get_index_state(State)
    return agent.Q_tables[val][direction]

def get_direction_for_RL_environement(current_direction, action):
    assert current_direction in ["x+", "y+", "x-", "y-"], "invalid_current_direction"
    assert action in ["continue", "clockwise", "anticlockwise"], "invalid_action"

    if action == "continue":
        return current_direction

    directions = ["x+", "y+", "x-", "y-"]
    idx = directions.index(current_direction)

    if action == "anticlockwise":  # sens trigonométrique
        return directions[(idx + 1) % 4]

    if action == "clockwise":  # sens horaire
        return directions[(idx - 1) % 4]

def move_head(action):

    assert action in ["x+", "y+", "x-", "y-"], "invalid_action"
    if action == "x+":
        return (1, 0)

    if action == "y+":
        return (0, 1)

    if action == "x-":
        return (-1, 0)
        
    if action == "y-":
        return (0, -1)
    
# current_direction: "x+", "y+", "x-", "y-"
def danger_feature_vector(Snake_dequeue, current_direction, X_cases, Y_cases):
    assert current_direction in ["x+", "y+", "x-", "y-"], "invalid_current_direction"
    Snake_copy = list(Snake_dequeue).copy()

    x_head, y_head = Snake_copy[-1]
    del Snake_copy[0]

    
    continue_action = get_direction_for_RL_environement(current_direction, "continue")
    clockwise_action = get_direction_for_RL_environement(current_direction, "clockwise")
    anticlockwise_action = get_direction_for_RL_environement(current_direction, "anticlockwise")

    x_continue, y_continue = move_head(continue_action)
    x_clockwise, y_clockwise = move_head(clockwise_action)
    x_anticlockwise, y_anticlockwise = move_head(anticlockwise_action)

    x_head_continue, y_head_continue = x_head + x_continue, y_head + y_continue
    x_head_clockwise, y_head_clockwise = x_head + x_clockwise, y_head + y_clockwise
    x_head_anticlockwise, y_head_anticlockwise = x_head + x_anticlockwise, y_head + y_anticlockwise

    
    hit_board_continue = not (0 <= x_head_continue < X_cases and 0 <= y_head_continue < Y_cases)
    hit_board_clockwise = not (0 <= x_head_clockwise < X_cases and 0 <= y_head_clockwise < Y_cases)
    hit_board_anticlockwise = not (0 <= x_head_anticlockwise < X_cases and 0 <= y_head_anticlockwise < Y_cases)

    hit_itself_continue = True if (x_head_continue, y_head_continue) in Snake_copy else False
    hit_itself_clockwise = True if (x_head_clockwise, y_head_clockwise) in Snake_copy else False
    hit_itself_anticlockwise = True if (x_head_anticlockwise, y_head_anticlockwise) in Snake_copy else False

    danger_continue = hit_board_continue or hit_itself_continue
    danger_clockwise = hit_board_clockwise or hit_itself_clockwise
    danger_anticlockwise = hit_board_anticlockwise or hit_itself_anticlockwise

    return (danger_continue, danger_clockwise, danger_anticlockwise)


def food_vector(Snake_dequeue, current_direction, Food_position):
    assert current_direction in ["x+", "y+", "x-", "y-"], "invalid_current_direction"

    Snake_copy = list(Snake_dequeue).copy()
    x_head, y_head = Snake_copy[-1]
    x_food, y_food = Food_position

    # distance actuelle à la nourriture
    dist_current = abs(x_head - x_food) + abs(y_head - y_food)

    continue_action = get_direction_for_RL_environement(current_direction, "continue")
    clockwise_action = get_direction_for_RL_environement(current_direction, "clockwise")
    anticlockwise_action = get_direction_for_RL_environement(current_direction, "anticlockwise")

    x_continue, y_continue = move_head(continue_action)
    x_clockwise, y_clockwise = move_head(clockwise_action)
    x_anticlockwise, y_anticlockwise = move_head(anticlockwise_action)

    # nouvelles positions de la tête
    head_continue = (x_head + x_continue, y_head + y_continue)
    head_clockwise = (x_head + x_clockwise, y_head + y_clockwise)
    head_anticlockwise = (x_head + x_anticlockwise, y_head + y_anticlockwise)

    # distances après action
    dist_continue = abs(head_continue[0] - x_food) + abs(head_continue[1] - y_food)
    dist_clockwise = abs(head_clockwise[0] - x_food) + abs(head_clockwise[1] - y_food)
    dist_anticlockwise = abs(head_anticlockwise[0] - x_food) + abs(head_anticlockwise[1] - y_food)

    food_continue = 1 if dist_continue < dist_current else 0
    food_clockwise = 1 if dist_clockwise < dist_current else 0
    food_anticlockwise = 1 if dist_anticlockwise < dist_current else 0

    return (food_continue, food_clockwise, food_anticlockwise)


def free_space_ratio(Snake_dequeue, X_cases, Y_cases, radius = 3):

    Snake_copy = list(Snake_dequeue).copy()
    x_head, y_head = Snake_copy[-1]

    # positions dans le voisinage local
    neighborhood = [
        (x_head + dx, y_head + dy)
        for dx in range(-radius, radius + 1)
        for dy in range(-radius, radius + 1)
        if (dx != 0 or dy != 0)
        and (0 <= x_head + dx < X_cases)
        and (0 <= y_head + dy < Y_cases)
    ]

    total_spaces = len(neighborhood)
    if total_spaces == 0:
        return 0.0

    snake_set = set(Snake_copy)
    free_spaces = [pos for pos in neighborhood if pos not in snake_set]

    free_ratio = len(free_spaces) / total_spaces
    return (free_ratio,)



def manhattan_distance_to_food(Snake_dequeue, Food_position):
    """
    Compute Manhattan distance between the snake head and the food.

    Parameters
    ----------
    Snake_dequeue : list or deque of (x, y)
        Snake body positions
    Food_position : tuple (x, y)
        Food coordinates

    Returns
    -------
    int
        Manhattan distance
    """
    x_head, y_head = Snake_dequeue[-1]
    x_food, y_food = Food_position

    return (abs(x_head - x_food) + abs(y_head - y_food),)





    
