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

def get_direction_for_RL_environement(current_direction, action):
    assert current_direction in ["x+", "y+", "x-", "y-"]
    assert action in ["continue", "clockwise", "anticlockwise"], "invalid_action"

    if action == "continue":
        return current_direction

    directions = ["x+", "y+", "x-", "y-"]
    idx = directions.index(current_direction)

    if action == "anticlockwise":  # sens trigonométrique
        return directions[(idx + 1) % 4]

    if action == "clockwise":  # sens horaire
        return directions[(idx - 1) % 4]




def get_compact_state_version(Snake_flattened):

    state_compact = ''
    for x in Snake_flattened:
        state_compact += str(x)
    return state_compact


