import pandas as pd
import numpy as np

user_usage=pd.read_csv('https://raw.githubusercontent.com/shanealynn/Pandas-Merge-Tutorial/master/user_usage.csv')
# user device data
user_device=pd.read_csv('https://raw.githubusercontent.com/shanealynn/Pandas-Merge-Tutorial/master/user_device.csv')
device=pd.read_csv('https://raw.githubusercontent.com/shanealynn/Pandas-Merge-Tutorial/master/android_devices.csv')
data1=pd.merge(user_usage,user_device[['use_id', 'platform', 'device']],on='use_id',how='outer',indicator=True)
print(data1.head())