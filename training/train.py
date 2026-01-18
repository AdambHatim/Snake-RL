from ENV.Snake_env import Snake_env
from ENV.Renderer import Renderer
from ENV.States import States
from agents.Agent import Agent
from utils.utils import find_state
import pygame
import matplotlib.pyplot as plt
import numpy as np

X_CASES = 8
Y_CASES = 8
CELL_SIZE = 30
BOARD_COLOR = (30, 30, 30)
SNAKE_COLOR = (0, 200, 0)
FOOD_COLOR  = (200, 0, 0)
first_food_position = (0,0)
first_Snake_dequeue=[(1,1),(1,2),(1, 3)]
direction = "x+"

learning_rate = 0.1
Discount_rate = 0.01
exploration_rate = 0.3

env = Snake_env(X_CASES, Y_CASES, first_food_position, direction, first_Snake_dequeue)
agent = Agent(learning_rate, exploration_rate, Discount_rate)
renderer = Renderer(CELL_SIZE, X_CASES, Y_CASES, BOARD_COLOR, SNAKE_COLOR, FOOD_COLOR)
St = States(X_CASES, Y_CASES)
def train(agent, env, episodes):
    for _ in range(episodes): 
        if _ % 1000 == 0: print(_)
        is_finished = False
        current_State = env.get_state()
       
        while not is_finished:

            state_rl = St.feature_based_representation(current_State)
            state_index = agent.get_index_state(state_rl)
            action = agent.get_action(state_index)

            next_state, reward, done, _ = env.step(action)

            next_state_rl = St.feature_based_representation(current_State)

            agent.update(state_rl, next_state_rl, action, reward, done)

            is_finished = done
            current_State = next_state

        env.reset()
    
def evaluate(agent, env, St,  renderer):

    clock = pygame.time.Clock()
    is_finished = False
    current_State = env.get_state()
    old_exp_r = agent.exp_r
    agent.exp_r = 0
    while not is_finished:
        Snake_dequeue = current_State["Snake_dequeue"]
        Food_position = current_State["Food_position"]
       
        state_rl = St.feature_based_representation(current_State)
        State_index = agent.get_index_state(state_rl)
        action = agent.get_action(State_index)

        renderer.show(Snake_dequeue, Food_position)
        
        pygame.display.flip()

        clock.tick(5)

        next_state, reward, done, score = env.step(action)
        is_finished = done
        current_State = next_state
    
    agent.exp_r = old_exp_r
    return score

def evaluate_avg_score(agent, env, states, episodes=1000):

    scores = np.array([0] * episodes)

    old_exp_r = agent.exp_r
    agent.exp_r = 0.0  

    for _ in range(episodes):
      
        current_state = env.reset()
        done = False

        while not done:
            state_rl = states.feature_based_representation(current_state)

            State_index = agent.get_index_state(state_rl)
            action = agent.get_action(State_index)

            next_state, reward, done, score = env.step(action)
            current_state = next_state

        scores[_] = score

    agent.exp_r = old_exp_r

    mean = np.mean(scores)
    std = np.std(scores)

    return mean, std






"""
vals = train(agent, env, 1000)
X = [_ for _ in range(1000)]
plt.plot(X, vals)
plt.show()
"""
train(agent, env, 10000)
env.reset()
score = evaluate(agent, env, St, renderer)

print("the score is ", score)
"""
print("the mean is ", mean)
print("the std is ", std)
"""