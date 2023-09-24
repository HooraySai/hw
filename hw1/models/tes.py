import numpy as np

a = [[1, 2], [3, 4]]
data = np.array(a[:])[:, 1:]
print(data)
