import pandas as pd
import numpy as np
from scipy.stats import trim_mean


def get_medias(df_dados_brutos):
    #medias simples:
    media_populacao = df_dados_brutos['Populacao'].mean()
    media_homicidios = df_dados_brutos['Taxa homicicios'].mean()
    #medias aparadas:
    proporcao_corte = 0.1 #corte de 10% de cada ponta
    media_aparada_populacao = trim_mean(df_dados_brutos['Populacao'],
    proportiontocut=proporcao_corte)
    media_aparada_homicidios = trim_mean(df_dados_brutos['Taxa homicicios'],
    proportiontocut=proporcao_corte)
    #mediana:
    mediana_populacao = df_dados_brutos['Populacao'].median()
    mediana_homicidios = df_dados_brutos['Taxa homicicios'].median()
    # media ponderada = soma(valor x peso) / soma(peso)
    # onde valor é a taxa_homicidio e o peso é populacao
    # calcular a média ponderada de homicídios onde o peso de cada cidade é sua população
    media_ponderada = np.average(df_dados_brutos['Taxa homicicios'], weights=df_dados_brutos['Populacao'])
    df_medias = pd.DataFrame({
        'Populacao': [media_populacao, media_aparada_populacao, mediana_populacao, np.nan],
        'Taxa homicicios': [media_homicidios, media_aparada_homicidios, mediana_homicidios, media_ponderada]
    }, index=['Média','Média Aparada', 'Mediana', 'Media Ponderada'])
    return df_medias



df_dados_brutos = pd.read_csv('taxa_homicidios.csv')
print(df_dados_brutos)
df_medias  = get_medias (df_dados_brutos)
print (df_medias.to_string(float_format= "%.2f"))

def estimativas_variabilidade(dados_brutos, media):
    """
   Estimativas de Variabilidade
   Indica o quão espalhados/dispersos os dados estão em relação ao centro (média, mediana, moda)
      Desvios
      Diferença entre os valores observados e uma estimativa de localização (média, mediana, moda)
      - Desvio: tx_homicidio - media
      - Desvio Absoluto: |tx_homicidio - media|
      - Desvio Absoluto Médio: soma dos desvios / num desvios
      - Variância: soma(desvio^2) / num desvios - 1
      - Desvio Padrão: Raiz quadrada da variância
      Estatísticas de Ordem
      Estatísticas baseadas em dados ordenados (order)
      - Amplitude: valor máximo - valor mínimo
      - Percentil: Divide os valores em porcentagens           [10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%]
      - Quantil: Mesmo que percentil, mas com casas decimais   [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
      - Quartil: Divide os valores em quatro partes iguais     [Q1 = 25%, Q2 = 50%, Q3 = 75%]
      - Amplitude Interquartil: Q3 - Q1
      - Mediana: Divide os valores em duas partes iguais       [med = Q2]
         Percentis
   """
    print(estimativas_variabilidade.__doc__)
    dados_brutos = dados_brutos.sort_values()
    #desvios
    desvio = dados_brutos - media
    #desvio absolutos
    desvio_absoluto = np.abs(desvio)
    #desvio absoluto médio
    desvios_absoluto_medio = np.mean(desvio_absoluto)
    #variancia (ddof = delata degree of freedom)
    variancia = np.var(dados_brutos, ddof= 1)
    #desvio pãdrao
    desvio_padrao = np.std(dados_brutos, ddof= 1)
    df_desvios_individuais = pd.DataFrame({
        'Dados Brutos': dados_brutos,
        'Desvio (taxa homicidio - média)' : desvio,
        'Desvio Absoluto |taxa homicidio - média|': desvio_absoluto
    })
    df_media_desvios = pd.DataFrame({
        'Métrica Estatística' : [
            'Média',
            'Desvio Padrão',
            'Variância',
            'Desvio Absoluto Médio (DAM)'
        ],
        'Valor Calculado': [
            media, 
            desvio_padrao,
            variancia,
            desvio_absoluto
        ]
    })
    print(df_desvios_individuais.round(2))
    print("\n")
    print(df_media_desvios)
    print("\n")
    #quantil (decimais)
    decimais = [0.05, 0.25, 0.5, 0.75, 0.95]
    df_quantis = pd.DataFrame(dados_brutos.quantile(decimais))
    print(df_quantis.transpose)
    # percentil
    df_percentis = pd.DataFrame(dados_brutos.quantile(decimais))
    # novos_indices = []
    # for p in decimais:
    #    novos_indices.append(f'{p * 100}%')
    # df_percentis.index = novos_indices
    df_percentis.index = [f'{p  *100}%' for p in decimais]
    print(df_percentis.transpose())


estimativas_variabilidade(df_dados_brutos['Taxa homicidios'], np.mean(df_dados_brutos['Taxa homicidios']))
