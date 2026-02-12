# Probability basics for a set of scores

import numpy as np
scores = np.array([60, 70, 72, 74, 75, 76, 78, 80, 90])

prob_greater_than_75 = np.count_nonzero(scores >= 75) / len(scores)
prob_less_than_70 = np.count_nonzero(scores < 70) / len(scores)

print("Probability of scores greater than or equal to 75:", prob_greater_than_75)
print("Probability of scores less than 70:", prob_less_than_70)