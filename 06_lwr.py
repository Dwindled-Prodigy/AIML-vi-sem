import numpy as np
import matplotlib.pyplot as plt

def local_regression(x0, X, Y, tau):
    x0 = [1, x0]
    X = [[1, i] for i in X]
    X = np.asarray(X)
    xw = X.T * np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau ** 2))
    beta = np.linalg.pinv(xw @ X) @ xw @ Y
    beta = beta @ x0
    return beta

def draw(tau):
    predictions = [local_regression(x0, X, Y, tau) for x0 in domain]
    plt.plot(X, Y, color='black')
    plt.plot(domain, predictions, color='red')
    plt.show()

X = np.linspace(-3, 3, 1000)
domain = X
Y = np.log(np.abs(X ** 2 - 1) + 0.5)

draw(10)
draw(0.1)
draw(0.01)
draw(0.001)
