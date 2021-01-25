from pandas import DataFrame
import matplotlib.pyplot as plt

dados = {
    'x': [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],
    'y': [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]
}

df = DataFrame(dados, columns=['x','y'])
print(df.head())

#Definir o modelo a utilizar
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2)
kmeans.fit(df)
centroides = kmeans.cluster_centers_
print(centroides)

#Realizar o plot
plt.scatter(
    df['x'],
    df['y'],
    c= kmeans.labels_.astype(float),
    s=50,
    alpha=0.5
)
plt.scatter(
    centroides[:,0],
    centroides[:,1],
    c='red',
    s=50
)
plt.xlabel('x')
plt.ylabel('y')
plt.show()