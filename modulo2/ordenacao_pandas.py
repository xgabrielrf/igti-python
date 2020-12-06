import numpy as np #pip install numpy==1.19.3
import matplotlib.pyplot as plt #pip install matplotlib
import pandas as pd #pip install pandas

#Carregando o arquivo e colocando date como index
df = pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
df = df.set_index('date')

#O sort, por padrão, faz a ordenação de forma crescente
print(f'Ordenando por temperatura crescente: \n{df.sort_values(by="temperatura")}')

print(f'\nOrdenando por temperatura decrescente: \n{df.sort_values(by="temperatura", ascending=False)}')

print(f'\nOrdenando por classification e depois por temperatura:\
    \n{df.sort_values(by=["classification","temperatura"])}')

print(f'\nOrdenando por índice decrescente: \n{df.sort_index(ascending=False)}')