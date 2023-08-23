import numpy as np


def generate_path(A, s_0, p_client=0.85):
  '''
  Inputs: 
    transition matrix, A
    initial state, s_0 -- Should be an integer from 0 to k-1
    probablility to still be a client, 0.85 by default

  Output:
    list -- random walk on the Markov chain
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


def clv_estimation(A, P, s_0, N=10**4):
  '''
  Inputs:
    transition matrix, A
    vector of profit per group, P
    initial state, s_0 -- Should be an integer from 0 to k-1
    number of iterations, N -- choose a very high number (10^4 by default)

  Output:
    CLV estimation as an average of the estimates at each iteration
  '''

  estimates = []

  for i in range(N):
    path = generate_path(A, s_0)

    profits = [P[j] for j in path]  # mapping the profit to the corresponding group in our path
    gamma = [(1/1.15)**(k+1) for k in range(len(path))]  # "discount" factor

    X = [profits[i]*gamma[i] for i in range(len(profits))]

    estimates.append(sum(X))
  
  return sum(estimates)/N
