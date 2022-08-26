
# Author:Griffy
# Date:2021-10-01
# Description:画出漫天的繁星和仰望星空的小人，有背景音乐
# version:1.0

import turtle as t
import random
import pygame
import time


# 播放背景音乐
def play_music():
    file = r'666.mp3'  # 最好把背景音乐文件和代码文件放在一个文件夹下，这里填背景音乐文件路径
    pygame.mixer.init()
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play(loops=2)


# 画渐变色的夜空
def dark_sky():
    t.bgcolor('black')  # 首先设置背景色，为黑色
    t.colormode(255)
    t.pensize(50)  # 笔头粗一点，刷上去颜色
    for i in range(0, 150):  # for循环调整画笔位置和颜色，调出渐变效果
        red = i
        green = i
        blue = i
        t.color(red, green, blue)  # 调色
        t.up()
        y = 3 * i
        t.goto(-350, 150 - y)  # 调位置
        t.down()
        t.forward(700)


# 画四角繁星
def draw_star(a):
    t.speed(0)
    t.pensize(1)
    t.color('#FFE62F')
    t.begin_fill()
    for n in range(4):
        t.right(30)
        t.forward(a)
        t.left(120)
        t.forward(a)
    t.end_fill()


# 仰望星空的小人
def mini_man():
    t.color('white')
    t.speed(2)
    t.pensize(5)
    t.up()
    t.goto(-160, -250)
    t.seth(110)
    t.down()
    t.forward(80)
    t.seth(30)
    t.circle(40, 300)
    t.seth(-110)
    t.forward(80)
    t.up()
    t.color('black')
    t.goto(-190, -145)
    t.down()
    t.seth(110)
    t.forward(25)
    t.up()
    t.goto(-200, -160)
    t.seth(30)
    t.pensize(8)
    t.color('pink')
    t.down()
    t.forward(10)
    # 画小人脚下的土地
    t.up()
    t.speed(0)
    t.goto(450, -1030)
    t.seth(90)
    t.color('#4F310D', '#4F310D')
    t.down()
    t.begin_fill()
    t.circle(800, 90)
    t.end_fill()
    # 画土地上的小草
    t.speed(1)
    t.up()
    t.goto(-150, -250)
    t.seth(75)
    t.color('green')
    t.down()
    t.forward(10)
    t.up()
    t.goto(-150, -250)
    t.seth(105)
    t.down()
    t.forward(10)
    # 画土地上的小花
    t.up()
    t.goto(-135, -255)
    t.seth(90)
    t.down()
    t.forward(10)
    t.dot(15, '#F85124')
    # 画小人的小心心
    t.up()
    t.goto(-200, -210)
    t.down()
    t.pensize(1)
    t.color('red', 'red')
    t.begin_fill()
    t.seth(45)
    t.forward(10)
    t.circle(5, 180)
    t.right(90)
    t.circle(5, 180)
    t.forward(4)
    t.end_fill()


# 写字
def write_content():
    t.color('white')  ##FFFDBB
    t.up()
    t.goto(-180, 0)
    t.down()
    t.write('Look up at the STARS', font=('MV Boli', 30, 'bold'))
    t.up()
    t.goto(-180, -50)
    time.sleep(1)
    t.down()
    t.write('Down to Earth', font=('MV Boli', 30, 'bold'))


####这里开始执行
# 背景音乐
play_music()
t.hideturtle()
t.speed(0)
t.setup(600, 600)
# 天空
dark_sky()
# 繁星
for i in range(15):
    x = random.randrange(-300, 300, 60)
    y = random.randrange(70, 300, 60)
    t.up()
    t.goto(x, y)  # 星星位置随机
    t.down()
    a = random.randint(3, 10)
    draw_star(a)
    t.left(30)
# 小人
mini_man()
time.sleep(1)
# 写字
write_content()

t.done()








