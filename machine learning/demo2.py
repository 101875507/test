import  json
import csv
with open(r"D:\data\annotations\labeled.json","r") as f:
    ls = json.load(f)
    a = [list(ls[0].keys())]
    for i in ls :
        a.append(list(i.values()))
with open(r'D:\Users\lijun\PycharmProjects\machine learning\data.csv','w',newline='',encoding='utf-8') as fp :
    fw=csv.writer(fp)
    fw.writerows(a)