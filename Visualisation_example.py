import matplotlib.pyplot as plt

n_arms = 10
epsilon = 0.1
n_plays = 2000

bandit = MultiArmedBandit(n_arms, epsilon)
action_values = bandit.run_simulation(n_plays)

plt.plot(range(n_plays), action_values)
plt.xlabel('Play')
plt.ylabel('Estimated Action Value')
plt.title('Estimated Action Values for a 10-Armed Bandit with ε = 0.1')
plt.show()

average_reward = sum(action_values) / n_plays
optimal_reward = 0.5

print(f'Average Reward: {average_reward:.3f}')
print(f'Optimal Reward: {optimal_reward:.3f}')