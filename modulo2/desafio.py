import numpy as np
import pandas as pd

df = pd.read_csv("https://pycourse.s3.amazonaws.com/bike-sharing.csv")

# a. Qual o tamanho desse dataset?
#print(df.shape)

# b. Qual a média da coluna windspeed?
#print(np.mean(df['windspeed']))

# c. Qual a média da coluna temp?
print(np.mean(df['temp']))

# d. Quantos registros existem para o ano de 2011?
# e. Quantos registros existem para o ano de 2012?
# f. Quantas locações de bicicletas foram efetuadas em 2011?
# g. Quantas locações de bicicletas foram efetuadas em 2012?
# h. Qual estação do ano contém a maior média de locações de bicicletas?
# i. Qual estação do ano contém a menor média de locações de bicicletas?
# j. Qual horário do dia contém a maior média de locações de bicicletas?
# k. Qual horário do dia contém a menor média de locações de bicicletas?
# l. Que dia da semana contém a maior média de locações de bicicletas?
# m. Que dia da semana contém a menor média de locações de bicicletas?
# n. Às quartas-feiras (weekday = 3), qual o horário do dia contém a maior média de locações de bicicletas?
# o. Aos sábados (weekday = 6), qual o horário do dia contém a maior média de locações de bicicletas?
