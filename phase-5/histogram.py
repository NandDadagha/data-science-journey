# Histogram Visualization
import numpy as np
import matplotlib.pyplot as plt

# Sample data
scores = np.array([72, 85, 90, 60, 88, 70, 75, 80])
plt.hist(scores, bins=5, edgecolor='black')
plt.title('Distribution of Scores')
plt.xlabel('Score Ranges')
plt.ylabel('Frequency')
plt.show()
