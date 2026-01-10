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
    
    def is_eat_food(self):
        food_position = self.Food.get_position()
        snake_head = self.Snake.get_head()

        return food_position == snake_head


    

    
