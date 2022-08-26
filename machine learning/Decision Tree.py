from sklearn import tree
import numpy as np
questions = ('C语言学的怎么样?',
             'java学的怎么样？',
             'python学的怎么样？',
             'go语言学的怎么样？',
             '前端学的怎么样？',
             '后端学的怎么样？',
             '算法学的怎么样？',
             '线性代数学的怎么样？',
             '高等数学学的怎么样？',
             '英语学的怎么样？',
             )
answers = [[3,3,3,3,3,3,3,3,3,3],
           [0,0,0,0,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1],
           [0,0,0,2,2,1,0,0,0,0],
           [0,0,0,0,0,3,0,3,3,0],
           [3,3,3,0,0,0,1,0,0,0],
           [3,0,3,3,3,3,0,2,0,0],
           [0,3,0,3,0,3,0,3,0,0],
           [2,2,0,0,0,0,0,0,2,1],
           [0,2,1,3,1,1,0,0,2,1]
           ]
labels = ['超级高手','门外汉','初级选手','初级选手','高级选手','中级选手','超级选手','高级选手','初级选手','初级选手']
clf = tree.DecisionTreeClassifier().fit(answers,labels)
youranswer =[]
for question in questions:
    print('===========\n',question)
    while(True):
        print('没学过 输入0，很多都不熟 输入1'
              '大部分都会 输入2，就这！就这！不会吧不会吧！，不会有人不会吧  输入3')
        try:
            answer = int(input('请输入：'))
            assert 0<=answer<=3
            break
        except:
            print('输入无效，请重新输入')
            pass
    youranswer.append(answer)
print(clf.predict(np.array(youranswer).reshape(1,-1)))