import pandas as pd #pip install pandas
import matplotlib.pyplot as plt

#Carregando o arquivo e colocando date como index
df = pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

print(f'\nAgrupamento e tiragem de média: \n{df.groupby(by="classification").mean()}')

#inplace: sobrescreve o valor da table em que está trabalhando
df2 = df.copy()
print(f'\nRemovendo uma coluna: \n{df2.drop("temperatura", axis=1, inplace=True)}')