import numpy as np
import pandas as pd

df = pd.read_csv("https://pycourse.s3.amazonaws.com/bike-sharing.csv")

# a. Qual o tamanho desse dataset?
#print(df.shape)

# b. Qual a média da coluna windspeed?
#print(np.mean(df['windspeed']))

# c. Qual a média da coluna temp?
#print(np.mean(df['temp']))

# d. Quantos registros existem para o ano de 2011? 
#df['datetime'] = pd.to_datetime(df['datetime'])
#print(df.loc[df['datetime'] <= '31/12/2011', ['datetime']])

# e. Quantos registros existem para o ano de 2012?
#df['datetime'] = pd.to_datetime(df['datetime'])
#print(df.loc[df['datetime'] > '31/12/2011', ['datetime']])

# f. Quantas locações de bicicletas foram efetuadas em 2011?
#df['datetime'] = pd.to_datetime(df['datetime'])
#print(np.sum(df.loc[df['datetime'] <= '31/12/2011', ['total_count']]))

# g. Quantas locações de bicicletas foram efetuadas em 2012?
#df['datetime'] = pd.to_datetime(df['datetime'])
#print(np.sum(df.loc[df['datetime'] > '31/12/2011', ['total_count']]))

# h. Qual estação do ano contém a maior média de locações de bicicletas?
#maior_valor = 0
#for season in range(1,5):
#    total = np.sum(df.loc[df["season"] == season, ["total_count"]])
#    total_split = str(total).split()
#    print(f'Na estacao {season}, {total_split[1]}')
#    if int(maior_valor) < int(total_split[1]):
#        maior_valor = total_split[1]
#        estacao = season
#print('\n1: inverno, 2: primavera, 3: verão, 4: outono')
#print(f'\nE o maior valor foi {maior_valor} na estacao {estacao}')
##RESPOSTA: E o maior valor foi 1061129 na estacao 3 - VERÃO

# i. Qual estação do ano contém a menor média de locações de bicicletas?
#menor_valor = 999999999999
#for season in range(1,5):
#    total = np.sum(df.loc[df["season"] == season, ["total_count"]])
#    total_split = str(total).split()
#    print(f'Na estacao {season}, {total_split[1]}')
#    if int(menor_valor) > int(total_split[1]):
#        menor_valor = total_split[1]
#        estacao = season
#print('\n1: inverno, 2: primavera, 3: verão, 4: outono')
#print(f'\nE o menor valor foi {menor_valor} na estacao {estacao}')
##RESPOSTA: E o menor valor foi 471348 na estacao 1 - INVERNO

# j. Qual horário do dia contém a maior média de locações de bicicletas?
#maior_valor = 0
#for hour in range(0,24):
#    total = np.sum(df.loc[df["hour"] == hour, ["total_count"]])
#    total_split = str(total).split()
#    print(f'Na hora {hour}, {total_split[1]}')
#    if int(maior_valor) < int(total_split[1]):
#        maior_valor = total_split[1]
#        hora = hour
#print(f'\nE o maior valor foi {maior_valor} na hora {hora}')
##RESPOSTA: E o maior valor foi 336860 na hora 17

# k. Qual horário do dia contém a menor média de locações de bicicletas?
#menor_valor = 99999999
#for hour in range(0,24):
#    total = np.sum(df.loc[df["hour"] == hour, ["total_count"]])
#    total_split = str(total).split()
#    print(f'Na hora {hour}, {total_split[1]}')
#    if int(menor_valor) > int(total_split[1]):
#        menor_valor = total_split[1]
#        hora = hour
#print(f'\nE o menor valor foi {menor_valor} na hora {hora}')
##RESPOSTA: E o menor valor foi 4428 na hora 4

# l. Que dia da semana contém a maior média de locações de bicicletas?
#maior_valor = 0
#for weekday in range(0,7):
#    total = np.sum(df.loc[df["weekday"] == weekday, ["total_count"]])
#    total_split = str(total).split()
#    print(f'Na semana {weekday}, {total_split[1]}')
#    if int(maior_valor) < int(total_split[1]):
#        maior_valor = total_split[1]
#        semana = weekday
#dia_semana = {
#    0: 'domingo',
#    1: 'segunda-feira',
#    2: 'terça-feira',
#    3: 'quarta-feira',
#    4: 'quinta-feira',
#    5: 'sexta-feira',
#    6: 'sábado'}
#print(f'\nE o maior valor foi {maior_valor} em {dia_semana[semana]}')
##RESPOSTA: E o maior valor foi 487790 em sexta-feira

# m. Que dia da semana contém a menor média de locações de bicicletas?
menor_valor = 999999
for weekday in range(0,7):
    total = np.sum(df.loc[df["weekday"] == weekday, ["total_count"]])
    total_split = str(total).split()
    print(f'Na semana {weekday}, {total_split[1]}')
    if int(menor_valor) > int(total_split[1]):
        menor_valor = total_split[1]
        semana = weekday
dia_semana = {
    0: 'domingo',
    1: 'segunda-feira',
    2: 'terça-feira',
    3: 'quarta-feira',
    4: 'quinta-feira',
    5: 'sexta-feira',
    6: 'sábado'}
print(f'\nE o menor valor foi {menor_valor} em {dia_semana[semana]}')
#RESPOSTA: E o menor valor foi 444027 em domingo

# n. Às quartas-feiras (weekday = 3), qual o horário do dia contém a maior média de locações de bicicletas?
# o. Aos sábados (weekday = 6), qual o horário do dia contém a maior média de locações de bicicletas?
