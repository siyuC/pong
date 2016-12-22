import gym
env = gym.make('Pong-v0')
# for i in range(1000):
# 	env.render()
# 	x = env.step(3)
# 	if i % 100 == 0:
# 		env.reset()
state_dim = env.observation_space.shape[0]
action_dim = env.action_space
action_bound = env.action_space

print state_dim,action_dim,action_bound 