import pandas as pd
import numpy as np

car_data=pd.read_csv('toyota.csv',index_col=0,na_values=['??'])

# COPY - SHALLOW // filename.copy(deep=False)
#      - DEEP // filename.copy(deep=True)  

print(car_data.index)#Row names
print(car_data.columns)#Coloumn names
print(car_data.size)#Total elements
print(car_data.shape)#Total R and C's

#Indexing 
print(car_data.head(5))
print(car_data.tail(5))
