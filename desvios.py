import pandas as pd 
import numpy as np
from faker import Faker

# instância do Faker para gerar nomes
fake = Faker('pt_BR')

# condições dos dados [População]
media_notas = 70
desvio_padrao_notas = 10
num_alunos = 100
notas = np.random.normal(loc = media_notas, scale= desvio_padrao_notas, size=num_alunos)
print(f"notas random: {notas}")
# Limita as notas entre 0 e 100
# o que for menor que 0 vira 0 e o que é maior que 100 vira 100
notas = np.clic(notas, 0, 100)

# --- Cálculo das médias ---
# 1. Média
media = np.mean(notas)
# 2. Mediana
mediana = np.median(notas)
# 3. Desvio (Simples)
desvios = notas - media
# 4. Desvio absoluto
# ex. 60 (notas) - 70 (media) = |10|(desvio)
desvios_absolutos = np.abs(notas - media)
# 5. Variância Individual
# ex. 80(nota) - 70(media) = 10*10 = 100(variância)
variancias_individuais = (notas - media) **2
variancia = np.var (notas, ddof=1) #para variância amostral (n-1)
# 6. Desvio Padrão
desvio_padrao = np.std(notas)
# 7. Desvio absoluto (Mediana)
desvios_abs_em_relacao_mediana_individuais = np.abs(notas - mediana)


  