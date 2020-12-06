import numpy as np #pip install numpy==1.19.3
import matplotlib.pyplot as plt #pip install matplotlib

x = [-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111, 0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.]
y = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657, 1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]

plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
#plt.show()

#Para gerar a regressão linear, utilizamos da seguinte função:
# (X^t * X)^-1 * X^t * y, onde (X^t * X)^-1 * X^t é a pseudeo-inversa
# Traduzindo, multiplicamos a transposta de X com X, então a invertemos e multiplicamos com a tranposta de X.
# E tudo isso é facilmente resulvido com: np.linalg.pinv(x)
# E y = a*x + b

#print('\nTransformando para numpy e vetor coluna: ')
x, y = np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)

#print('\nAdicionando bias: estimando o termo b: ')
X = np.hstack((x, np.ones(x.shape)))

print('\nEstimando a e b')
beta = np.linalg.pinv(X).dot(y)
print(f'a estimado: {beta[0][0]}')
print(f'b estimado: {beta[1][0]}')

plt.plot(x, X.dot(beta), label='regressão linear')
plt.legend()
plt.show()
