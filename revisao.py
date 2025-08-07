import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = 'data\sp500_data.csv.gz'
df = pd.read_csv(data)

# Remover coluna específica
df = df.drop(columns=['ADS'])

# Renomear coluna específica
df = df.rename(columns={'Unnamed: 0': 'Data'})

# Transformar o campo data para datetime e settar ele como indice
df['Data'] = pd.to_datetime(df['Data'])
df = df.set_index('Data')
print(df.head())

# Encontrar a maior e menor data
data_inicio = df.index.min()
data_fim = df.index.max()
print(f"Quantidade de variações coletadas: {len(df)}")
print(f"Período de coleta: {data_inicio.strftime('%d/%m/%Y')} à {data_fim.strftime('%d/%m/%Y')}")

# guardar o ativo sendo usado
ativo = 'IBM'

# Encontrar o valor máximo e mínimo do ativo
maior_valor = df[ativo].max()
data_maior = df[ativo].idxmax()
menor_valor = df[ativo].min()
data_menor = df[ativo].idxmin()
print("-" * 30)
print(f"Ativo: {ativo}")
print(f"Maior variação diária: {maior_valor:.4f}")
print(f"Ocorreu no dia: {data_maior.strftime('%d/%m/%Y')}")
print(f"Menor variação diária: {menor_valor:.4f}")
print(f"Ocorreu no dia: {data_menor.strftime('%d/%m/%Y')}")
print("-" * 30)
# MEDIDAS DE TENDÊNCIA CENTRAL
media = df[ativo].mean()
mediana = df[ativo].median()
moda = df[ativo].mode()
print(f"Medidas de tendência central para {ativo}:")
print(f"Média: {media:.4f}")
print(f"Mediana: {mediana:.4f}")
if (len(moda) > 0):
    print(f"Modas: {moda.to_string(index=False)}")
else:
    print(f"O ativo {ativo} é amodal")
df_frequencia = df[ativo].value_counts()
print(df_frequencia.head())
print("-" * 30)

# Estimativas de Variabilidade
desvio_absoluto = np.abs(df[ativo] - media)
desvio_absoluto_medio = np.mean(desvio_absoluto)
variancia = np.var(df[ativo], ddof=1)
desvio_padrao = np.std(df[ativo], ddof=1)
print(f"Estimativas de variabilidade para: {ativo}")
print(f"Desvio Absoluto Médio: {desvio_absoluto_medio:.4f}")
print(f"Variância: {variancia:.4f}")
print(f"Desvio Padrão: {desvio_padrao:.4f}")
print("-" * 30)

# GRÁFICOS
serie_as_dataframe = pd.DataFrame(df[ativo])
fig, (histograma, caixa, densidade) = plt.subplots(3, 1, figsize=(8, 18))

# Histograma
# plt.figure() # Cria a primeira figura (janela)
sns.histplot(data = serie_as_dataframe, ax = histograma)
histograma.set_xlabel("variação percentual diária")
histograma.set_ylabel("Ocorrências")
histograma.set_title("Histograma")

# Boxplot
#plt.figure() # Cria a segunda figura (janela)
sns.boxplot(data = serie_as_dataframe, ax = caixa)
caixa.set_ylabel("variação percentual diária")
caixa.set_title("Boxplot")

# Densidade
# plt.figure()
sns.kdeplot(data = serie_as_dataframe, ax = densidade)
plt.xlabel("variação percentual diária")
plt.ylabel("Ocorrências")
plt.title("Densidade")
plt.tight_layout()
plt.show()  