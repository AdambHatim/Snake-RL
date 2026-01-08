class Rules:
    def __init__(self, Board, Food, Snake):

        self.Board = Board
        self.Food = Food
        self.Snake = Snake

    def is_collision_snake_board(self):
        snake_head = self.Snake.get_head()
        return not self.Board.is_within_board(snake_head)