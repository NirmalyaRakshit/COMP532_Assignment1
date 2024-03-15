import random

class MultiArmedBandit:
    def __init__(self, n_arms, epsilon):
        self.n_arms = n_arms
        self.epsilon = epsilon
        self.action_values = [0] * n_arms

    def choose_action(self):
        if random.random() < self.epsilon:
            return random.randint(0, self.n_arms - 1)
        else:
            return max(range(self.n_arms), key=lambda x: self.action_values[x])

    def update_action_values(self, chosen_arm, reward):
        self.action_values[chosen_arm] += (1 / (1 + self.action_values[chosen_arm])) * (reward - self.action_values[chosen_arm])

    def run_simulation(self, n_plays):
        for _ in range(n_plays):
            chosen_arm = self.choose_action()
            reward = random.gauss(0.5, 1)  # Assume a Gaussian reward distribution with mean 0.5 and variance 1
            self.update_action_values(chosen_arm, reward)

        return self.action_values