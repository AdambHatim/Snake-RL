import numpy as np

class Agent:
    def __init__(self, learning_rate, exploration_rate, Discount_rate):
        
        """
        in self.state_to_index
        keys are States and values are the index of states, each state is represented by two attributes
        food_position and snake_dequeue 

        in self.Q_values
        keys are numbers and values represent the state value corresponding to that index in Q_table
        """
        self.state_to_index = {} 
        self.Q_tables = {}
        self.possible_actions = ["continue", "clockwise", "anticlockwise"]
        self.index_last_state = 0
        
        self.lr = learning_rate
        self.exp_r = exploration_rate
        self.discount_rate = Discount_rate

       
    def get_optimal_state_action(self, state_index):
        
        max_value = self.Q_tables[state_index]["continue"]
        max_action = "continue"
        if  max_value < self.Q_tables[state_index]["clockwise"]:
            max_action = "clockwise"
            max_value = self.Q_tables[state_index]["clockwise"]
        if max_value < self.Q_tables[state_index]["anticlockwise"]:
            max_action = "anticlockwise"
        return max_action


    def get_index_state(self, State):
        val = self.state_to_index.get(State, -1)

        if val == -1:
            self.index_last_state += 1
            self.state_to_index[State] = self.index_last_state
            
            self.Q_tables[self.index_last_state] = {}
            self.Q_tables[self.index_last_state]["continue"] = 0
            self.Q_tables[self.index_last_state]["clockwise"] = 0
            self.Q_tables[self.index_last_state]["anticlockwise"] = 0
            return self.index_last_state
        else: 
            return val
        

    def get_action(self, state_index):
        a = np.random.random()
        if a < self.exp_r:
            return np.random.choice(self.possible_actions)
        else:
            max_action = self.get_optimal_state_action(state_index)
            return max_action
        
       
    def update(self, State, next_state, action, reward, done):
             
            state_index = self.get_index_state(State)
    
            if done:
                max_value = 0
            else:
                next_state_index = self.get_index_state(next_state)
                max_action = self.get_optimal_state_action(next_state_index)
                max_value = self.Q_tables[next_state_index][max_action]

            TD_error = reward + self.discount_rate * max_value - self.Q_tables[state_index][action]
            self.Q_tables[state_index][action] += self.lr*TD_error
                                                                      

            



        