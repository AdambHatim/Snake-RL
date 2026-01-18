from utils.utils import move_head
class Snake:
    def __init__(self, direction, Snake_dequeue):

        assert direction in ["x+", "y+", "x-", "y-"], "Invalid direction"
        self.direction = direction
        self.Snake_dequeue = Snake_dequeue

    def get_direction(self):
        return self.direction
    
    def get_Snake_dequeue(self):
        return self.Snake_dequeue
    
    def get_head(self):
        return self.Snake_dequeue[-1]
    
    def change_direction(self, next_direction):

        assert next_direction in ["x+", "y+", "x-", "y-"], "Invalid direction"

        axis = self.direction[0]
        next_axis = next_direction[0]

        assert axis != next_axis, "Invalid direction"

        self.direction = next_direction

    def update(self, is_increasing = False):
        
        x_head, y_head = self.get_head()

        if not is_increasing:
            del self.Snake_dequeue[0]
        
        x_dir, y_dir = move_head(self.direction)
 
        self.Snake_dequeue.append((x_head + x_dir, y_head + y_dir))
   


        




        
    
