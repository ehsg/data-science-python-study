import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

#Amostra Aleatória Simples
amostra = np.random.choice([0, 1], size=150, replace=True, p=[0.5, 0.5])
print(len(amostra[amostra==1]))
print(len(amostra[amostra==0]))


#Amostra Estratificada
iris = pd.read_csv('iris.csv')
iris['class'].value_counts()
x, _, y, _ = train_test_split(iris.iloc[:, 0:3], iris.iloc[:, 4], test_size=0.5, stratify=iris.iloc[:, 4])
print(y.value_counts())
infert = pd.read_csv('infert.csv')
infert['education'].value_counts()
x1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1], test_size=0.6, stratify=infert.iloc[:, 1])
print(y1.value_counts())
