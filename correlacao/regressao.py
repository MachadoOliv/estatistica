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

#3. Configuração e treinamento do modelo
#Define a variável preditora (independente), que é a Exposure e a variável de resultados que é o PEFR
predictors = ['Exposure']
outcome = 'PEFR'
#Instanciar o modelo
model = LinearRegression()
#Etapa de treinamento 
model.fit(dataframe[predictors], dataframe[outcome])

#4. Exibição dos Coeficientes
#Intercepto
print(f'Intercepto: {model.intercept_:.3f}')
#Coeficiente Angular
print(f'Coeficiente Angular: {model.coef_[0]}')

#5. Geração do gráfico
fig,(reg) = plt.subplots(1,1, figsize = (4,4))
#Gráfico regreção
reg = sns.regplot (x = 'Exposure', y = 'PEFR', data = dataframe, ax = reg)
plt.tight_layout()
plt.show()
