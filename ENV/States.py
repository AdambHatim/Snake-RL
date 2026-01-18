from utils.utils import food_vector, danger_feature_vector, free_space_ratio, manhattan_distance_to_food

class States:
    def __init__(self, X_cases, Y_cases):
        self.X_cases = X_cases
        self.Y_cases = Y_cases
        
        pass
        
    def get_naive_representation(self, State):

        Snake_dequeue, Food_position = tuple(State["Snake_dequeue"]), State["Food_position"]
        return (Snake_dequeue, Food_position)

    def grid_based_representation(self, State):
        pass

    def feature_based_representation(self, State):
        Snake_dequeue = State["Snake_dequeue"]
        Food_position = State["Food_position"]
        current_Direction = State["Direction"]

        x_head, y_head = Snake_dequeue[-1]

        
        danger = danger_feature_vector(Snake_dequeue, current_Direction, self.X_cases, self.Y_cases)
        food = food_vector(Snake_dequeue, current_Direction, Food_position)
        ratio = free_space_ratio(Snake_dequeue, self.X_cases, self.Y_cases)
        distance_to_food = manhattan_distance_to_food(Snake_dequeue, Food_position)


        return tuple(danger + food + ratio + distance_to_food)

  









