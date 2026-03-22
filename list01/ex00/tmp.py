import numpy as np

a = np.arange(10)
print(a)
print(np.sum(a))
print(np.add.reduce(a))
print(np.add.accumulate(a))
