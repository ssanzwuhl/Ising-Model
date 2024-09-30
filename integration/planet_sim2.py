import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from time import sleep

v0 = [5, 10, 1, 0]

def acc(v, t):
    u = v[:2]
    r = np.linalg.norm(u)
    udot = v[2:]
    
    udotdot = - c * r**-3 * u
    return np.r_[udot, udotdot]    

t = np.linspace(0, 200, 500)

G = 1
M = 10
c = G * M

p_path = spi.odeint(acc, v0, t)

fig, ax = plt.subplots(1, 1)

print(fig, ax)

pt = np.matrix.transpose(p_path)
ax.set_xlim(min(pt[0]), max(pt[0]))
ax.set_ylim(min(pt[1]), max(pt[1]))
print(pt)
for i in range(len(pt[0])):
    plt.scatter(pt[0][i], pt[1][i], color = 'red')
    plt.draw()
    plt.pause(1/60)
