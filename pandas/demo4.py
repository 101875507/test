import pandas as pd
df1 = pd.read_excel(r"D:\Users\lijun\PycharmProjects\pandas\超市营业额2.xlsx",sheet_name="Sheet1",header=None)
df2 = pd.read_excel(r"D:\Users\lijun\PycharmProjects\pandas\超市营业额2.xlsx",sheet_name="Sheet2",header=0)
c = pd.merge()
#c = pd.concat([df1,df2],ignore_index=True)
#c.to_excel(r"D:\Users\lijun\PycharmProjects\pandas\2.xlsx",index=False,header=None)
#df = pd.read_excel(r'D:\Users\lijun\PycharmProjects\pandas\2.xlsx')
#print(df[''])



