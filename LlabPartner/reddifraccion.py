import matplotlib.pyplot as plt
import numpy as np

def field(x, N):
    f = 0
    for n in range(N):
        f += np.cos(n*x)

    return 2*f

X = np.linspace(-3*np.pi,3*np.pi, 200)

print(np.shape(field(X, 6)))


for N in range(2, 150):
    F = field(X, N)
    plt.plot(X, F/max(F), '-')

plt.show()
