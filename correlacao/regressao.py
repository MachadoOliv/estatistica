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

#parcial 
#Definis os limites dos eixos X e Y
ax.set_xlim(0,23)
ax.set_ylim(295,450)
#Definir os rótulos
ax.set_xlabel('Exposure')
ax.set_ylabel('PERF')
#Plotar a linha
ax.plot(dataframe['Exposure'], model.predict(dataframe[predictors]), '-')
#Adicionar o texto b0
ax.text(0.4, model.intercept_,r'$b_0$', size = 'larger')
x = pd.DataFrame({'Exposure': [7.5,17.5]})
y = model.predict(x)
ax.plot((7.5, 7.5, 17.5), (y[0], y[1], y[1]), '--')
# Exibir Deltay e Deltax no gráfico
ax.text(5, np.mean(y), r'$\Delta Y$', size = 'larger')
ax.text(12, y[1] - 10, r'$\Delta X$', size = 'larger')
#Adicionar anotação para o coeficiente angular
ax.text(12, 390, r'$b_1 = \frac{\Delta Y}{\Delta X}$', size = 'larger')

#Valores ajustados e resíduos 
# Gera os valores ajustados do modelo 
fitted = model.predict(dataframe[predictors])
#calcula os resíduos
residuals = dataframe[outcome] - fitted
#Exibe o gráfico de correlação
res = dataframe.plot.scatter(x = 'Exposure', y = 'PEFR', ax = res)
res.plot(dataframe.Exposure, fitted)
#Para cada valor de índice 
for x, yatual, yfitted in zip(dataframe.Exposure, dataframe.PEFR, fitted):
    print(f'x: {x} - yreal: {yatual} - yreta {yfitted}')
    res.plot((x, x ), (yatual, yfitted), '--', color = 'C1')
plt.tight_layout()
plt.show()
