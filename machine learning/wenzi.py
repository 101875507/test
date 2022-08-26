from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import time

import warnings
warnings.filterwarnings('ignore')
boston = load_boston()

X=boston.data
y=boston.target
x_trian,x_test,y_trian,y_test = train_test_split(X,y,test_size=0.2,random_state=3)
model = LinearRegression()
model.fit(x_trian,y_trian)
train_score = model.score(x_trian,y_trian)
cv_score = model.score(x_test,y_test)
print(train_score,cv_score)






