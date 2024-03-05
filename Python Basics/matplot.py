import pandas as pd
import matplotlib.pyplot as plt

coffeedata=pd.read_csv("flavors_of_cocoa.csv",index_col=0,na_values=["??,????,##"])
coffeedata2=coffeedata.copy()
coffeedata3=coffeedata.copy()

coffeedata3.isnull().sum()
missing=coffeedata3[coffeedata3.isnull().any(axis=1)]
stats=coffeedata3.describe()
valcounts=coffeedata3.value_counts()

coffeedata3["Review Date"].fillna(coffeedata3["Review Date"].mean(),inplace=True)

