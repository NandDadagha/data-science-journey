# Distribution check for a set of scores

import numpy as np;
scores = np.array([60, 70, 72, 74, 75, 76, 78, 80, 90])

print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Standard Deviation:", np.std(scores))
print("Range:", np.max(scores) - np.min(scores))