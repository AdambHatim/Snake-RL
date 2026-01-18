from utils.utils import move_head
class Rules:
    def __init__(self, Board, Food, Snake):

        self.Board = Board
        self.Food = Food
        self.Snake = Snake

    def is_collision_snake_board(self):
        snake_head = self.Snake.get_head()
        return not self.Board.is_within_board(snake_head)
    
    def is_collision_snake_itself(self):
        snake_dequeue = self.Snake.get_Snake_dequeue()
        return len(snake_dequeue) != len(set(snake_dequeue))
    
    def is_eat_food(self, action):
        
        x_food, y_food = self.Food.get_position()
        x_head, y_head = self.Snake.get_head()
        x_dir, y_dir = move_head(action)
        x_next_head, y_next_head = x_head + x_dir, y_head + y_dir

        return (x_next_head == x_food and y_next_head == y_food)


    

    
