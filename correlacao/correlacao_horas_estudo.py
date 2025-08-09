import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

dataframe = pd.DataFrame({
    'alunos': ['Matheus', 'Fernando', 'Ana', 'Beatriz', 'Bruna'],
    'horas': [ 2, 4, 6, 8, 10],
    'notas': [ 50, 70, 85, 95, 100]
})
print(dataframe)

plt.figure(figsize=(10, 6))
plt.xlim(0,12)
plt.ylim(40,120)
sns.regplot(x = 'horas', y='notas', data = dataframe, truncate= False )

plt.xlabel('Horas de Estudo')
plt.ylabel('Notas de Prova')
plt.title ('Gráfico de Regressão: Horas de Estudo vs Desempenho nas provas')
plt.show()