import numpy as np
import gymnasium as gym

def simple_policy(state):
    action = 0 if state<5 else 1
    return action

if __name__== '__main__':
    env = gym.make("CartPole-v1")
    alpha = 0.1
    gamma= 0.99

    states = np.linspace(-0.2094,0.2094,10)
    V={}
    for state in range(len(states)+1):
        V[state]=0

    for i in range(5000):
        observation, info = env.reset()
        Truncated   = False
        Terminated  = False
        while not Terminated:
            state = int(np.digitize(observation[2],state,right=False))
            action = simple_policy(state)
            observation_, reward, truncated, terminated, info = gym.step(action)
            state_ = int(np.digitize(observation_[2],state,right=False))
            V[state] = V[state] - alpha * (reward + gamma * V[state_] - V[state])
            observation = observation_

    for state in V:
        print(state, "%.3f" %V[state])