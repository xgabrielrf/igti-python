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
plt.hlines(
    y=y.mean(),
    xmin=x.min(),
    xmax=x.max(),
    linestyle='dashed',
    label='Modelo de referência do $R^2$')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regressão linear no scikit-learn')
plt.grid()
#plt.show()


#Função para cálculo do MSE
def mse(y_true, y_pred, is_ref=False):

    #mse modelo
    if is_ref:
        mse = ((y_true - y_true.mean())**2).mean()
    else:
        mse = ((y_true - y_pred)**2).mean()

    return mse

def r2(mse_reg, mse_ref):
    return 1 - mse_reg/mse_ref

#Visualizando y e y_pred
print(f'Leitura do y real: \n{y.ravel()}')
print(f'Leitura do y pred.: \n{y_pred.ravel()}')

#Calculando MSE
mse_reg = mse(y_true=y, y_pred=y_pred)
print(f'MSE do modelo de regressão: {mse_reg}')
mse_ref = mse(y_true=y, y_pred=y_pred, is_ref=True)
print(f'MSE do modelo de regressão: {mse_ref}')

#Calculando R2 score
r2_score = r2(mse_reg=mse_reg, mse_ref=mse_ref)
print(f'Coeficiente R2 do modelo implementado (calculado): {r2_score}')

#Coeficiente do scikit-learn
r2_score_skl = reg.score(x, y)
print(f'Coeficiente R2 do modelo implementado (sckit-learn): {r2_score_skl}')