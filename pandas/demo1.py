import pandas as  pd
ab=pd.DataFrame()
ab = pd.DataFrame({'Gender':['Female','Male','Male','Female','Male'],'Name':['Gaopen Yang','Changqiang You','Mei Sun','Xiaojuan Sun','Gaojuan You']})
ab.to_excel('D:\Users\lijun\PycharmProjects\pandas\工作簿1.xlsx')
print('done')