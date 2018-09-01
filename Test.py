import numpy as np

x = np.array([[4], [5], [6], [7]])
x = x[:, :1]
w = [1.2]

result = np.matmul(x, w)
