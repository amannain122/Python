import pandas as pd
import numpy as np
import matplotlib as plt
import scipy as sc
from sklearn import datasets, linear_model
from sklearn.datasets import load_diabetes, fetch_openml
from sklearn.pipeline import make_pipeline
import seaborn as sns

store=pd.read_csv("Store.csv",index_col=0,na_values=["??"])
store.describe()
store.info()
store._get_numeric_data()
store._get_categorical_data()

# %% to convert categorical to numerical
# USE ONE HOT ENCODING


# %% Call main() only with if__name__=='__main__': main()
# ===================================
# math
# random
# decimal
# csv
# pickle - model saving module
# tinkter