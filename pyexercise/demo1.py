'''result = {}
while True:
    x = input('请输入一个单词，回车输入下一个，结束输入exit')
    if x=='exit':
         break
    else:
         result[x] = result.get(x,0)+1
for key,value in result.items():
    print(key,value,sep='\t')'''
'''import datetime
print(datetime.datetime.now())
lst = []
for n in range(1,200):
    for i in range(2,n):
        if n%i==0:
            break
        else:
            lst.append(n)
            break
print(lst)
print(datetime.datetime.now())'''














'''1
from collections import Counter
a = input('请输入一个字符串：')
b =Counter(a)
print(b)'''

'''2
try:
    x = eval(input('请输入x的值：'))
    assert 0<=x<20
    if x>=0 and x<5 :
        y = -x+2.5
    if x>=5 and x<10 :
        y = 2-1.5*(x-3)*(x-3)
    if x>=10 and x<20 :
        y =x/2-1.5
    print(y)
except:
    print('error')'''

'''3
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
num = eval(input('请输入1-12的数字'))
a = months[3*num-3:3*num]
print(a)'''


'''4
a = eval(input('请输入一个正整数:'))
b = eval(input('请输入一个正整数:'))
c = eval(input('请输入一个正整数:'))
s = 0
for i in range(a,b):
    if i%c==0:
        s=s+i
print(s)'''

'''5
a =eval(input('请输入学生的分数:'))
if a>=0 and a<60:
    print('不及格')
if a>=60 and a<70:
    print('及格')
if a>=70 and a<80:
    print('中')
if a>=80 and a<90:
    print('良')
if a>=90 and a<100:
    print('优')'''


'''6
result = {}
while True :
    x = input('请输入一个单词,回车输入下一个，退出输入exit')
    if x =='exit':
        break
    else:
        result[x]=result.get(x,0)+1
for key,value in result.items():
    print(value,key,sep=' ')'''


'''7
a=input('请输入一个字符串:')
f =open('1.txt','wb')
f.write(a.upper().encode('utf-8'))
f.close()'''

'''8
a = int(input('请输入一个整数:'))
def shusu(num):
    if num<2 :
        return 'No'
    else:
        for i in range(2,num):
            if num%i==0:
                return 'No'
                break
            else:
                return 'Yes'
print(shusu(a))'''


'''9
import random
a = [random.randint(0,100) for i in range(20)]
x=a[0:10]
y=a[10:20]
x.sort(reverse=False)
y.sort(reverse=True)
print(x+y)'''
'''import math
a = eval(input('是否选择加急，如果是请输入1，如果不是请输入0'))
b = eval(input('请输入邮件的重量:'))
if b <=1000:
    if a==0:
        cost = 8
    else:
        cost = 13
else:
    if a==0:
        cost = math.ceil((b-1000)/500)*4+8
    else:
        cost = math.ceil((b - 1000)/500) * 4+13
print(cost)'''
import string
'''a =input('请输入一个句子').split()
b =input('输入需要查找的字符')
result={}
for i in a:
    result[i] = result.get(i, 0)
    if b in i :
        result[i] = result.get(i, 0) + 1
for key,value in result.items():
    print(key,value,sep='  ')'''















'''for i in range(100):
    U = eval(input('请输入一个平衡电压:'))
    t = eval(input('请输入下落时间:'))
    q = 1.0218/(t*(1+0.0219*(t**0.5))**1.5)/U
    n = 100000*q/1.6
    q1 = q/n
    print(q)
    print(n)
    print(q1)



for i in range(100):
    U = eval(input('请输入一个提升电压:'))
    t1 = eval(input('请输入下落时间:'))
    t2 = eval(input('请输入上升时间:'))
    q = 1.0218/((1+0.0219*t1)**1.5)*(1/t1+1/t2)*((1/t1)**0.5)*(1/U)
    n = 100000 * q / 1.6
    q1 = q / n
    print(q)
    print(n)
    print(q1)'''


'''lst1 = []
n = int(input('请选择输入几个整数:'))
for i in range(n):
    a = int(input('请输入一个整数:'))
    lst1.append(a)
print(sum(lst1))
print(sum(lst1)/len(lst1))'''


'''a = input('请输入一个字符串')
if a == a[::-1]:
    print('Yes')
else:
    print('No')'''
'''import random
a = [random.randint(0,100) for i in range(20)]
print(a)
print(a[::2])
print(a[1::2])
a[::2]=sorted(a[::2],reverse=False)
print(a)'''

































