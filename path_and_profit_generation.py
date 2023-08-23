import numpy as np


def generate_path(A, s_0, p_client=0.85):
  '''
  Inputs: 
    transition matrix, A
    initial state, s_0 -- Should be an integer from 0 to k-1
    probablility to still be a client, 0.85 by default
  '''

  path = [s_0]

  u = np.random.uniform()
  current_state = s_0
  while u <= p_client:
    next_state = np.random.choice([i for i in range(A.shape[0])], p=A[current_state,:])
    path.append(next_state)
    current_state = next_state
    u = np.random.uniform()
  
  return path


# Function for Monte-Carlo simulation in progress...


