import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sb

# import matplotib.pyplot as plt
hotel_data=pd.read_csv("hotel.csv",index_col=0,na_values=["??","????","#"])
hotel2=hotel_data.copy()
hotel3=hotel_data.copy()

#NA Values
hotel3.isnull().sum()
missing=hotel3[hotel3.isnull().any(axis=1)]
#stats
stats=hotel3.describe()
hotel3["country"].value_counts()

#refill
hotel3["agent"].fillna(hotel3["company"].mean(),inplace=True)
hotel3["company"].fillna(hotel3["company"].median(),inplace=True)

#Drop Coutries as only 464 na values and can't assign 
hotel3.dropna(subset="country",inplace=True)
