class Game:
    def __init__(self, board, snake, food, rules):
        self.board = board
        self.snake = snake
        self.food = food
        self.rules = rules

        self.game_over = False
        self.score = 0

    def reset(self):
        self.game_over = False
        self.score = 0

    def step(self, action=None):
        """
        Un tick de jeu.
        action : direction demandée ("x+", "y+", "x-", "y-") ou None
        """

        if self.game_over:
            return

        # appliquer l’action (si fournie)
        if action is not None:
            try:
                self.snake.change_direction(action)
            except AssertionError:
                pass  # action invalide → ignorée

        # vérifier si la nourriture va être mangée
        eat_food = self.rules.is_eat_food()

        # avancer le serpent
        self.snake.update(is_increasing=eat_food)

        # collisions
        if self.rules.is_collision_snake_board():
            self.game_over = True
            return

        if self.rules.is_collision_snake_itself():
            self.game_over = True
            return

        # gestion nourriture
        if eat_food:
            self.score += 1
            occupied = self.snake.get_Snake_dequeue()
            free = self.board.free_cases(occupied)
            self.food.spawn(free)

    def is_game_over(self):
        return self.game_over
