import numpy as np

# Define the environment (grid world)
# S: Start, T: Treasure, #: Obstacle
environment = np.array([
    ['S', ' ', ' ', ' ', ' '],
    [' ', '#', ' ', '#', ' '],
    [' ', ' ', ' ', '#', ' '],
    [' ', '#', ' ', '#', 'T'],
])

# Parameters
num_actions = 4  # Up, Down, Left, Right
num_states = np.prod(environment.shape)
learning_rate = 0.1
discount_factor = 0.9
exploration_prob = 0.3
num_episodes = 100

# Initialize Q-values
Q = np.zeros((num_states, num_actions))

# Helper function to convert state to index
def state_to_index(state):
    return state[0] * environment.shape[1] + state[1]

# Helper function to get valid next state
def get_next_state(state, action):
    next_state = tuple(np.array(state) + np.array([
        [-1, 1, 0, 0],  # Actions: Up, Down, Left, Right
        [0, 0, -1, 1]
    ])[:, action])
    next_state = np.clip(next_state, (0, 0), tuple(np.array(environment.shape) - 1))
    return next_state

# Q-learning algorithm
for episode in range(num_episodes):
    state = np.unravel_index(np.random.choice(num_states), environment.shape)
    done = False
    
    print(f"Episode {episode + 1}")
    
    while not done:
        print(f"Current state: {state}")
        
        if np.random.uniform() < exploration_prob:
            action = np.random.randint(num_actions)
            print(f"Exploring with random action: {action}")
        else:
            action = np.argmax(Q[state_to_index(state)])
            print(f"Exploiting with action: {action}")
        
        next_state = get_next_state(state, action)
        
        next_row, next_col = next_state
        reward = -1 if environment[next_row, next_col] != '#' else -10
        
        max_next_q = np.max(Q[state_to_index(next_state)])
        Q[state_to_index(state)][action] += learning_rate * (reward + discount_factor * max_next_q - Q[state_to_index(state)][action])
        
        state = next_state
        
        if environment[state[0], state[1]] == 'T':
            # Here's the corrected line
            print("Treasure found!")
            done = True
        elif environment[state[0], state[1]] == '#':
            print("Hit an obstacle!")
            done = True
        
        print(f"Reward received: {reward}")
        print("-" * 20)

# Optimal policy extraction
optimal_policy = np.argmax(Q, axis=1).reshape(environment.shape)
print("Optimal Policy:")
print(optimal_policy)
