import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)
    
    def draw(self,no_balls):
        if no_balls > len(self.contents): return self.contents
        
        balls = []
        for _ in range(no_balls):
            choice = random.randrange(len(self.contents))
            balls.append(self.contents.pop(choice))
        
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):
        ball_drawn = copy.deepcopy(hat).draw(num_balls_drawn)

        draw_success = True

        for key in expected_balls:
            if expected_balls[key] > ball_drawn.count(key):
                draw_success = False
                break
        
        if draw_success:
            success +=1
    
    return success/num_experiments