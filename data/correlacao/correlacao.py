import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

#caminho para o data set
ATIVOS_CSV = 'data\sp500_data.csv.gz'
SETORES_CSV ='data\sp500_sectors.csv'

df_ativos= pd.read_csv(ATIVOS_CSV, index_col= 0 )
print(df_ativos.head())
df_setores = pd.read_csv(SETORES_CSV)
print(df_setores.head())

#telecomunicações
df_telecom = df_setores[df_setores['sector'] == 'telecommunications_services']['symbol']
print(df_telecom.head())

#ativos telecomunicações
telecom_ativos = df_ativos.loc[df_ativos.index>='2012-07-01', df_telecom]
print(telecom_ativos.head())

#correlação
dados_correlacionados = telecom_ativos.corr()
print(dados_correlacionados.head())