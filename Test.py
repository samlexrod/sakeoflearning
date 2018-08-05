import numpy as np

height = np.round(np.random.normal(1.75, .20, 5000), 2)

weight = np.round(np.random.normal(60.3, 16, 5001), 2)

np_stack = np.column_stack((height, weight))

print(np_stack)