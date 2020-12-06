import numpy as np #pip install numpy==1.19.3
import matplotlib.pyplot as plt #pip install matplotlib

x = [-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111, 0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.]
y = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657, 1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]

#Transformando em numpy array
x, y = np.array(x).reshape(-1,1), np.array(y).reshape(-1,1)

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(x,y)

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

print(f'a estimado: {reg.coef_.ravel()[0]}')
print(f'b estimado: {reg.intercept_[0]}')

#Realizando a predição
y_pred = reg.predict(x)

#O score, quanto mais próximo de 1, melhor.
score = reg.score(x,y)
print(score)

plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais')
plt.plot(x, y_pred, label='regressão linear (R2: {:3f})'.format(score))
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regressão linear no scikit-learn')
plt.grid()
plt.show()