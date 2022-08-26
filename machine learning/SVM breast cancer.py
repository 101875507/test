from  sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
cancer = load_breast_cancer()
X = cancer.data
Y =cancer.target
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)
clf = SVC(C=0.01,kernel="linear")
clf.fit(X_train,Y_train)
a =clf.score(X_train, Y_train)
b =clf.score(X_test, Y_test)
print("train score = {0} test score = {1}".format(a,b))