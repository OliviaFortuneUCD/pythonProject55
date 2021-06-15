import pandas as pd
import numpy as np
dummy_data1 = {
        'id': ['1', '2', '3', '4', '5'],
        'Feature1': ['A', 'C', 'E', 'G', 'I'],
        'Feature2': ['B', 'D', 'F', 'H', 'J']}

df1 = pd.DataFrame(dummy_data1, columns = ['id', 'Feature1', 'Feature2'])

dummy_data2 = {
        'id': ['1', '2', '6', '7', '8'],
        'Feature1': ['K', 'M', 'O', 'Q', 'S'],
        'Feature2': ['L', 'N', 'P', 'R', 'T']}
df2 = pd.DataFrame(dummy_data2, columns = ['id', 'Feature1', 'Feature2'])


#Where the keys match

df_merge_col=pd.merge(df1,df2,on='id')

print(df_merge_col)