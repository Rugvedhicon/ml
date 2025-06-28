import sklearn
from sklearn.datasets import load_iris
import pandas as pd 
import numpy as np
data=load_iris()
df=pd.DataFrame(data.data,columns=data.feature_names)
print(df.isnull().sum())
print(df.isnull().sum(axis=1))