
'''a = [1,2,3,4,5,6]
b = [2,3,4,5,6,7]
print(a+b)
c = []
for i in range(len(a)):
    d =a[i]+b[i]
    c.append(d)
print(c)
dd =list(map(str,a+b))
print(dd)
print(''.join(dd))'''
import turtle
t = turtle.Pen()
for x in range(100):
      t.forward(x)
      t.left(45)
