import pandas as pd #pip install pandas
import matplotlib.pyplot as plt

#Carregando o arquivo e colocando date como index
df = pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

#figsize: Altera o tamanho da figura
#grid: Coloca o grid na imagem
#style: Com '-o' ele mostra a linha '-' e coloca o dot 'o' nos pontos específicos
#linewidth: Altera a largura do tracejado
#color: Altera a cor do tracejado. "color picker" do google também auxilia com o HEX
#df.plot(figsize=(10,5), grid=True, style='-o', linewidth=2.5, color='black')


#Figura em barras calculado pela classificação
#rot: Grau em que ficarão as labels
#df['classification'].value_counts().plot.bar(figsize=(10,5),rot=0)


#Figura em pizza calculado pela classificação
#autopct: Coloca as informações de % dentro das fatias
#shadow: Faz uma sombra no gráfico
#label: Modifica o nome da label, no caso abaixo, Classification para ''
df['classification'].value_counts().plot.pie(autopct='%1.1f%%', shadow=True, figsize=(10,5), label='')

plt.show()