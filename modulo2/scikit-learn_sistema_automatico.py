import pandas as pd #pip install pandas
import numpy as np #pip install numpy
import matplotlib.pyplot as plt #pip install matplotlib

#Install sckit-learn:
#pip install NumPy 
#pip install SciPy 
#pip install Joblib
#pip install threadpoolctl
#pip install --pre --extra-index https://pypi.anaconda.org/scipy-wheels-nightly/simple scikit-learn


#Carregando o arquivo e colocando date como index
df = pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

x, y = df[['temperatura']].values, df[['classification']].values
#print(f'x: \n{x}')
#print(f'y: \n{y}')

from sklearn.preprocessing import LabelEncoder

#fit: pega um array de input, faz um determinado cálculo e absorve o parâmetro dos cálculos
#transform: aplica a transformação
le = LabelEncoder()
y = le.fit_transform(y.ravel())
#print(f'\ny: \n{y}')

#LogistcRegression: Gera uma função que vai descriminar da melhor
#maneira possível as classes (quente. muito quente, confortável e frio)
from sklearn.linear_model import LogisticRegression

#Classificador
#Ele será treinado com os valores de x comparando ao y, já transformado em números
clf =  LogisticRegression()
clf.fit(x,y)

#Agora serão gerados 100 valores entre 0 e 45 para comparar e identificar
#qual a classificação da temperatura
#Além disso, já transforma em um vetor coluna "(-1, 1)"
x_test = np.linspace(start=0., stop=45., num=100).reshape(-1, 1)

#Fazendo a predição
y_pred = clf.predict(x_test)
#print(f'\nPredição de y: \n{y_pred}')
#Transformando para os valores originais
y_pred = le.inverse_transform(y_pred)
#print(f'\nPredição de y com valores originais: \n{y_pred}')

#Agora será criado um dicionário para linkar chave/valor, temperatura/classificação
output = {
    'new_temp': x_test.ravel(),
    'new_class': y_pred.ravel()
}

output = pd.DataFrame(output)

#Gráfico de barras
#output['new_class'].value_counts().plot.bar(figsize=(10, 5), rot=0, title='# de novos valores gerados')

#Gráfico de caixas
#output.boxplot(by='new_class', figsize=(10,5))
#plt.show()

def classify_temp():
    '''Classificação do input do usuário'''
    
    ask = True
    while ask:
        #input de temperatura
        temp = input('\nInsira a temperatura (C°): ')

        #Transforma para numpy array
        temp = np.array(float(temp)).reshape(-1,1)

        #Classifica
        class_temp = clf.predict(temp)

        #Transformação para valores originais
        class_temp = le.inverse_transform(class_temp)

        #Classificação
        print(f'A Classificação da temperatura {temp.ravel()[0]} é de: {class_temp[0]}')

        #Pergunta
        ask = input('\nEnvie qualquer informação que não vazia para terminar: ') == ''

classify_temp()