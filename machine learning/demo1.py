from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
iris =load_iris()
model = LinearRegression(normalize=True)
x =np.arange(10)
y = 2*x+1
plt.plot(x,y,'o')
plt.show()


