import random

class Food:
    def __init__(self, position):
        self.position = position
 

    def spawn(self, possible_positions):
        position = random.choice(possible_positions)
        self.position = position

    def get_position(self):
        return self.position