"""
Histograma:
     Gráfico de barras que representa uma distribuição de frequência.
     - Eixo x (horiz): intervalos (classes) dos dados
     - Eixo y (vertc): frequência (contagem) de itens por intervalo
BoxPlot: 
     Diagrama de caixa que representa os extremos e mais os quartis
     - Min: O menor valor do conjunto de dados
     - Q1: Primeiro quartil dos dados (25%)
     - Q2: Segundo quartil dos dados, a mediana (50%)
     - Q3: Terceiro quartil dos dados (75%)
     - Max: O maior valor do conjunto de dados
Densidade:
     Gráfico que representa uma distribuição suavisada da frequência dos dados
     - Eixo x (horiz): intervalos (classes) dos dados
     - Eixo y (vertc): frequência (contagem) de itens por intervalo
Dispersão:
     Gráfico que representa a relação entre dois conjunto de dados
     - Eixos: Cada eixo representará um dos dois conjunto de dados
     - Pontos: Cada ponto representa a interseção entre as variáveis de ambos os conjuntos.

"""
#pip install matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import graficos_estatisticos

#imprimir o docstring
print(graficos_estatisticos.__doc__)

# importar dados do csv
df_dados_brutos = pd.read_csv('homicidios_por_populacao/taxa_homicidios.csv')

def histograma():
    bins_do_grafico = [3, 5, 8, 14.5]
    histograma = (df_dados_brutos["Taxa homicidios"]).plot.hist(figsize = (6, 4), bins=bins_do_grafico)
    histograma.set_xlabel('Taxa de Homicídios')
    histograma.set_ylabel('Frequência (Número de cidades)')
    plt.show()

def boxplot():
     boxplot = (df_dados_brutos['Taxa homicidios']).pyplot.box()
     plt.show()
def densidade():
     histograma = (df_dados_brutos['Taxa homicidios']).plot.hist(density = True, bins = range(1, 16), figsize = (6, 4))
     df_dados_brutos['Taxa homicidios'].plot.density(ax = histograma)
     histograma.set_xlabel('Taxa de homicídios')
     histograma.set_ylabel('Frequência (densidade)')
     plt.xlim(0, 15)
     plt.show()
def dispersao():
     plt.figure(figsize=(10,6))
     plt.scatter(df_dados_brutos['Taxa homicidios'], df_dados_brutos['Populacao'], alpha=0.7)
     plt.xlabel('Populacao')
     plt.ylabel('Taxa de homícidios')
     plt.title('Gráfico de dispersão: taxa de homicídio vs população')
     plt.grid(True)
     plt.show()
#histograma()
#boxplot()
#densidade()
dispersao()