from ENV.Game import Game
from ENV.Board import Board
from ENV.Food import Food
from ENV.Snake import Snake
from ENV.Rules import Rules
from utils.utils import get_possible_directions, get_direction_for_RL_environement

class Snake_env:
    def __init__(self, X_CASES, Y_CASES, position, direction, Snake_dequeue=[(0,0)]):

        self.X_CASES = X_CASES
        self.Y_CASES = Y_CASES
        self.init_position = position
        self.init_direction = direction
        self.init_snake = Snake_dequeue

        self.reset()

    def reset(self):
        board_env = Board(self.X_CASES, self.Y_CASES)
        food_env = Food(self.init_position)
        snake_env = Snake(self.init_direction, self.init_snake.copy())
        rules_env = Rules(board_env, food_env, snake_env)
        self.Game = Game(board_env, snake_env, food_env, rules_env)

        return self.get_state()

    def step(self, action):
        current_score = self.Game.score 
        current_direction = self.Game.snake.get_direction()
        real_action = get_direction_for_RL_environement(current_direction, action)

        self.Game.step(real_action)

        done = self.Game.game_over
        new_score = self.Game.score
        # reward simple (à améliorer plus tard)

        reward = 1 if new_score > current_score else -0.01
        if done:
            reward = -1
        
        
        return self.get_state(), reward, done, new_score

    def get_state(self):
        state = {
            "Snake_dequeue": tuple(self.Game.snake.get_Snake_dequeue()),
            "Food_position": self.Game.food.get_position(),
            "Direction": self.Game.snake.get_direction(),
        }
        return state

