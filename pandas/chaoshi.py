import pandas as pd
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.EAST_asian_width',True)
df = pd.read_excel(r'D:\Users\lijun\PycharmProjects\pandas\fruit (1).xlsx')
print(df[:10])
print(df[2:9])
print(df.index)
print(df['Sale'].sum())
for i in ['Grape','Banana','Peach','Pear']:
    print(df[df['Fruit']==i].sum())
print(df.groupby(by='Date')['Sale'].sum())
print(df.groupby(by='Fruit')['Sale'].sum())

'''ab=pd.DataFrame()
ab = pd.DataFrame({'Gender':['Female','Male','Male','Female','Male'],'Name':['Gaopen Yang','Changqiang You','Mei Sun','Xiaojuan Sun','Gaojuan You']})
ab.to_excel('D:\Users\lijun\PycharmProjects\pandas\工作簿1.xlsx')
print('done')'''



