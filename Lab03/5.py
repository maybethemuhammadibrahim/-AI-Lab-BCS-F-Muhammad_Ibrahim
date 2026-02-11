#TASK 5
import random

class LearningAgent:
    def __init__(self):
        self.q_table = {'Play': 0, 'Rest': 0}
        self.actions = ['Play', 'Rest']
        self.learning_rate = 0.1

    def get_reward(self, action):
        if action == "Play":
            return 5
        return 1

    def update(self, action, reward):
        current_q = self.q_table[action]
        self.q_table[action] = current_q + self.learning_rate * (reward - current_q)

    def run(self, iterations):
        for i in range(iterations):
            action = max(self.q_table, key=self.q_table.get)

            if i < 2:
                action = self.actions[i]

            reward = self.get_reward(action)
            self.update(action, reward)

            print(f"Step {i+1}: Action {action} Reward {reward}")

        print("Q-table Updated:", self.q_table)

agent = LearningAgent()
agent.run(10)
