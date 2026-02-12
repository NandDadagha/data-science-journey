# Correlation coefficient between scores and hours studied

import numpy as np

scores = np.array([50, 60, 70, 80, 90])
hours = np.array([1, 2, 3, 4, 5])

print("Correlation coefficient:", np.corrcoef(scores, hours)[0, 1])