'''import csv
from csv import reader ,writer
a = ['城市','环比','同比','定基']
b = [['北京','101.5','120.7','121.4'],
 ['上海','101.2','127.3','127.8'],
 ['广州','101.3','119.4','120.0'],
 ['深圳','102.0','140.9','145.5'],
 ['沈阳','100.1','101.4','101.6']]
with open('data.csv','w',newline='') as f:
    wr = csv.writer(f)
    wr.writerow(a)
    wr.writerows(b)
with open('data.csv','r') as  f :
    for k in csv.reader(f):
            print(k)'''






'''import numpy as np
print(np.arange(5,33,3))
print(np.mat('1 1 1;1 0 1;1 1 1'))
print(np.random.randint(1,10,(3,2)))
print(np.random.randint(1,10,(3,2)).reshape(2,3))
print(np.random.uniform(5,10,(5,3)))
a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7,8])
print((np.sum((a-b)**2))**0.5)'''
import pandas

