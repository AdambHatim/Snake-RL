class Board:
    def __init__(self, X_CASES, Y_CASES):

        self.X_CASES = X_CASES
        self.Y_CASES = Y_CASES


    def is_within_board(self, position):
        x, y = position
        return (0 <= x < self.X_CASES and 0 <= y < self.Y_CASES)
    
    def free_cases(self, occupied_cases):
        return [(x,y) for x in range(0, self.X_CASES) for y in range(0, self.Y_CASES) if (x,y) not in
                occupied_cases]
    

