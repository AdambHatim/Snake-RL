import numpy as np

class Food:
    def __init__(self, position):
        self.position = position
 

    def spawn(self, possible_positions):
        position = np.random.choice(possible_positions)
        self.position = position