#Cleaning Data
import pandas as pd

carsdata=pd.read_csv("toyota.csv",index_col=0,na_values=["??","????"])
carsdata2=carsdata.copy()
carsdata3=carsdata.copy()

#Find missing values using isnull() or isna()
carsdata2.isnull().sum()

#Axis=1 --Coloumn  and Axis=0 --for Row
missing=carsdata2[carsdata2.isnull().any(axis=1)]

#Find appropritate data to refill
stats=carsdata2.describe()
mean1=carsdata2.mean()
median1=carsdata2.median()
mode1=carsdata2.mode()


#if not described find in particular with most common using .index[0]
carsdata2["FuelType"].value_counts()
carsdata2["FuelType"].value_counts().index[0]

#Refilling using fillna()

#Add mean/median for numerical values
carsdata2["Age"].fillna(carsdata2["Age"].mean(), inplace=True)
carsdata2["HP"].fillna(carsdata2["HP"].mean(), inplace=True)
carsdata2["KM"].fillna(carsdata2["KM"].median(), inplace=True)

#Add value_count()/mode().index[0] for categorical values
carsdata2["FuelType"].fillna(carsdata2["FuelType"].value_counts().index[0],\
                             inplace=True)
carsdata2["MetColor"].fillna(carsdata2["MetColor"].mode().index[0],inplace=True)

# =============================================================================
# Cleaning all data at once using lamda in apply
# =============================================================================
carsdata3.isnull().sum()
carsdata3=carsdata3.apply(lambda x:x.fillna(x.mean()) if x.dtype=="float" \
                          else x.fillna(x.value_counts().index[0]))

