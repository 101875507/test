import pandas as pd
df = pd.read_csv(r"D:\Users\lijun\PycharmProjects\machine learning\data.csv")
df = df.dropna()
#print(df.isnull())#删除缺失的行
print(df['title'])