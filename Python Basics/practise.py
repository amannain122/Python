import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing Data
data1=pd.read_csv("gapminder.csv",index_col=0,na_values=["??"])
data2=data1.copy()
data3=data2.copy()

#Find NAN values
data3.isnull().sum()

nan=data3[data3.isnull()]
#Stats
stat=data3.describe()
values=data3.value_counts()

#TOP and Bottom od df
top=data3.head()
bottom=data3.tail() 
