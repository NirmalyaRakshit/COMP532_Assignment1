n_arms = 10
epsilon = 0.1
n_plays = 2000

bandit = MultiArmedBandit(n_arms, epsilon)
action_values = bandit.run_simulation(n_plays)print(action_values)