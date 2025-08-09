import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# pip install
from sklearn.linear_model import LinearRegression

EXPOSICAO_ALGODAO='C:/Users/efg/repo_projeto/estatistica/data/LungDisease.csv'
dataframe = pd.read_csv(EXPOSICAO_ALGODAO)
print(dataframe.head())

dataframe.plot.scatter(x= 'Exposure', y='PEFR')
plt.show() 