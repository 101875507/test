import  pandas as pd
import numpy as np
file_name = r"D:\Users\lijun\PycharmProjects\machine learning\data.csv"
movies_data = pd.read_csv(file_name, delimiter=',')
print(movies_data.info())
pd.set_option("display.max_columns", 100)   #让所有列都能加载出来
