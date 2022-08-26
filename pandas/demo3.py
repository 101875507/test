import csv
from csv import reader ,writer

with open('data.csv','r') as f:
    for line in reader(f):
        with open('aa.csv','a+') as fp:
            wr = writer(fp)
            wr.writerow(line)




