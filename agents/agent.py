import numpy as np

class agent:
    def __init__(self, learning_rate, exploration_rate, Discount_rate):
        
        """
        in self.States
        keys are numbers and values are the states, each state is represented by two attributes
        food_position and snake_dequeue 

        in self.Q_values
        keys are numbers and values represent the state value corresponding to that index in Q_table
        """
        self.States = {} 
        self.Q_tables = {}
        self.actions = ["continue", "clockwise", "anticlockwise"]
        self.next_index = 0
        
        self.learning_rate = learning_rate
        self.exploration_rate = exploration_rate
        self.Discount_rate = Discount_rate

       

    
    def get_action(self, state):
        a = np.random.random()
        if a < self.exploration_rate:
            pass
        
    def update(self, state, next_state):
        pass


print(np.random.choice(["continue", "clockwise", "anticlockwise"]))
        