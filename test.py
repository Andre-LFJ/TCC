import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 0.0000198651 *x**3 - 0.00488498 *x**2 + 0.136412 *x + 0.0107898
x = np.linspace(0, 30, 1000)  # valores de x para o gráfico
y = f(x)                       # valores de y correspondentes

plt.plot(x, y)                 # plota a função
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da função f(x)')
plt.show()
