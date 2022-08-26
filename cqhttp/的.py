import numpy as np
x = np.random.randint(1,10,(2,5))
print(x)
t=np.argsort(x)
x.sort()
print(x[0])