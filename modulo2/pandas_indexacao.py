import pandas as pd #pip install pandas

#help(pd) #Atenção no decimal, pois por padrão o separador é str='.'
#         Mas no nosso país utilizamos, por padrão, str=','

df = pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
print(df)

print(f'\nFiltrando por coluna date: \n{df["date"]}')

#Lembrando que ao passar mais de um valor, deve-se ser feito via lista df[  ['', '']  ] 
print(f'\nFiltrando por coluna date e classification: \n{df[["date","classification"]]}')

#loc e iloc funcionam como no tratamento de listas (ou do numpy)
#ou seja, se utilizar df.loc[:,"temperatura":], ele irá pegar do índice temperatura pra frente.
print(f'\nBusca por índice: \n{df.iloc[:,1]}')

print(f'\nBusca por nome/label: \n{df.loc[:,"temperatura":]}')

print(f'\nTransformando a coluna date em datetime: ')
df['date'] = pd.to_datetime(df['date'])
print(df.dtypes)

print(f'\nSetando o índice: ')
df = df.set_index('date')
print(df)

print(f'\nRetornando valores em determinada condição: \n{df[df["temperatura"] >= 25]}')

print(f'\nRetornando valores com condição e apenas uma coluna:\
     \n{df.loc[df.index <= "2020-03-01", ["classification"]]}')
