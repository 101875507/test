from os import mkdir,listdir
from os.path import isdir,basename
from random import choice,randrange
from string import digits
from PIL import Image,ImageDraw
from PIL.ImageFont import truetype
import PIL
from sklearn import  svm
from sklearn.model_selection import train_test_split

width , height =25,25
fontSize = 25
noiseRate = 8
def generate(dstDir='datasets',num=40000):
    if not isdir(dstDir):
        mkdir(dstDir)
    with open(dstDir+'\\digits.txt','w') as fp:
        for i in range(num):
            digit = choice(digits)
            im = Image.new('RGB',(width,height),(255,0,0))
            img = ImageDraw.Draw(im)
            font = truetype('c:\\windows\\fonts\\TIMESBD.TTF',fontSize)
            img.text((0,0),digit,font=font,fill=(0,0,0))
            im.save(dstDir+'\\'+str(i)+'.jpg')
            fp.write(digit+'\n')
generate(num=8000)



