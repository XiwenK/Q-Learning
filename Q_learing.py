import os

import pandas as pd
from matplotlib import pyplot as plt

from environment import CliffBoxPushingBase
from collections import defaultdict
import numpy as np
import random


class QAgent(object):
    def __init__(self):
        self.action_space = [1, 2, 3, 4]
        #         self.V = []
        self.Q = defaultdict(lambda: np.zeros(len(self.action_space)))
        self.discount_factor = 0.99
        self.alpha = 0.5
        self.epsilon = 0.01

    def take_action(self, state):
        if random.random() < self.epsilon:
            action = random.choice(self.action_space)
        else:
            action = self.action_space[np.argmax(self.Q[state])]
        return action

    # def take_action2(self, state):
    #     return self.action_space[np.argmax(self.Q[state])]

    # implement your train/update function to update self.V or self.Q
    # you should pass arguments to the train function
    def train(self, state, action, next_state, reward):
        self.Q[state][action - 1] = (1 - self.alpha) * self.Q[state][action - 1] + \
                                    self.alpha * (reward + self.discount_factor * max(self.Q[next_state]))


if __name__ == '__main__':
    env = CliffBoxPushingBase()
    # you can implement other algorithms
    agent = QAgent()
    teminated = False
    rewards = []
    time_step = 0
    num_iterations = 10000
    for i in range(num_iterations):
        env.reset()
        step_reword = []
        while not teminated:
            state = env.get_state()
            action = agent.take_action(state)
            #         print(action)
            reward, teminated, _ = env.step([action])
            next_state = env.get_state()
            step_reword.append(reward)
            #     print(f'step: {time_step}, actions: {action}, reward: {reward}')
            time_step += 1
            agent.train(state, action, next_state, reward)
        # print(f'rewards: {sum(rewards)}')
        #     print(f'print the historical actions: {env.episode_actions}')
        teminated = False
        rewards.append(sum(step_reword))

    print("training complete.")

    # actions = ["UP", "DOWN", "LEFT", "RIGHT"]
    # env.reset()
    # rwd = 0
    # while not teminated:
    #     state = env.get_state()
    #     action = agent.take_action2(state)
    #     print("state: %s, action: %s" % (state, actions[action - 1]))
    #     reward, teminated, _ = env.step([action])
    #     rwd += reward
    # print("reward: %f" % rwd)
    #
    # print("test complete.")

    # Create Q-value Table and import data
    actions = ["UP", "DOWN", "LEFT", "RIGHT"]
    state = []
    up = []
    down = []
    left = []
    right = []
    policy = []

    for k, v in agent.Q.items():
        state.append(k)
        up.append(v[0])
        down.append(v[1])
        left.append(v[2])
        right.append(v[3])
        policy.append(actions[np.argmax(v)])
        # print("%s state : %s" % (k, v))

    data = {
        "state": state,
        "UP": up,
        "DOWN": down,
        "LEFT": left,
        "RIGHT": right,
        "POLICY": policy,
    }
    dataFrame = pd.DataFrame(data)
    dataFrame.to_csv(os.getcwd() + '/Q_value table.csv')

    # episode rewards vs episodes
    plt.plot(range(num_iterations), rewards, 'b')
    plt.xlabel('Episodes')
    plt.ylabel('Rewards')
    plt.title('Episodes rewards vs episodes')
    plt.savefig(os.getcwd() + '/episode reward')
    plt.show()
