import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = "data\sp500_data.csv.gz"
df = pd.read_csv(data)
# Remover coluna específica 
df = df.drop(columns = ['ADS'])
#Renomear coluna específica 
df= df.rename (columns={'Unnamed: 0': 'Data'})
#print(df.head(5))

# Tranformar o campo data para datetime e settar ele como indice
df['Data'] = pd.to_datetime(df['Data'])
df = df.set_index('Data')
#print(df.head())
# Encontrar a maior e a menor data
data_inicio = df.index.min()
data_fim = df.index.max()
#print(f"Quantidade de varições coletadas: {len(df)}")
#print(f"Período de coleta: {data_inicio.strftime('%d/%m/%Y/')} à {data_fim.strftime('%d/%m/%Y')}")

# Guardar o ativo sendo usado 
ativo = 'IBM'

# Encontrar o valor máximo e mínimo do ativo 
maior_valor = df[ativo].max()
data_maior = df[ativo].idxmax()
menor_valor = df[ativo].min()
data_menor = df[ativo].idxmin()
print('-' * 30)
print(f"Ativo analizado: {ativo}")
print(f"maior vaiação diaria: {maior_valor:.4f}")
print(f"Ocorreu no dia: {data_maior.strftime('%d/%m/%Y')}")
print(f"menor vaiação diaria: {menor_valor:.4f}")
print(f"Ocorreu no dia: {data_menor.strftime('%d/%m/%Y')}")

#medidas de tendencia central
media = df[ativo].mean()
mediana = df[ativo].median()
moda = df[ativo].mode()
print(f"Medidas de tendência central para {ativo}:")
print(f"Média: {media:.4f}")
print(f"Mediana : {mediana:.4f}")
if(len(moda) > 0):
    print(f"Modas: {moda}")
else:
    print(f"O ativo {ativo} é amodal")