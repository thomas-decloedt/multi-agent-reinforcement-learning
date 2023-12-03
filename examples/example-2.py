from pettingzoo.mpe import simple_tag_v3
import os

# Function to clear the terminal screen
def clear_terminal(n_step):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"N_step = {n_step}")

env = simple_tag_v3.parallel_env(render_mode="human", num_good=1, num_adversaries=1, num_obstacles=0, max_cycles=1000)
observations, infos = env.reset()

n_step = 0

while env.agents:
    # this is where you would insert your policy
    actions = {agent: env.action_space(agent).sample() for agent in env.agents}

    observations, rewards, terminations, truncations, infos = env.step(actions)

    clear_terminal(n_step)

    n_step += 1

env.close()