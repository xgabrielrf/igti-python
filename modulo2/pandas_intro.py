import pandas as pd #pip install pandas

#help(pd) #Atenção no decimal, pois por padrão o separador é str='.'
#         Mas no nosso país utilizamos, por padrão, str=','

df = pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
print(df)

'''
#Necessária a instalação do xlrd para utilização de arquivos Excel:
#pip install xlrd
excel_file = pd.ExcelFile('https://pycourse.s3.amazonaws.com/temperature.xlsx')
df2 = pd.read_excel(excel_file, sheet_name='Sheet1')
print('\n',df2)

#Não há como converter os decimais, ao menos na versão atual do read_excel from pd
excel_file2 = pd.ExcelFile('https://pycourse.s3.amazonaws.com/temperature.xlsx')
df3 = pd.read_excel(excel_file2, sheet_name='Sheet2')#, decimal=',')
print('\n',df3)
'''

print(f'\nPrimeiras 3 linhas: {df.head(3)}')

print(f'\nUltimas 3 linhas: {df.tail(3)}')

print(f'\nTipos: {df.dtypes}')

print(f'\nInfos: {df.info()}')

print(f'\nColunas: {df.columns}')

print('\nRenomeando as colunas: ')
df.columns = ['col1','col2', 'col3']
print(df)