import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt



M = 10
G = 1

v0 = np.zeros(4)

v0[0] = 0
v0[1] = 0
v0[2] = 1
v0[3] = 0

def acc(v, t0):
    u = v[2:]
    u_norm = np.linalg.norm(u)
    udot = v[:2]

    #udotdot = -G * M * u_norm ** -3 * u
    udotdot = -udot
    return np.r_[udot, udotdot]



fig, ax = plt.subplots(1, 1, figsize = (8, 4))

t = np.linspace(0, 3, 30)

v = spi.odeint(acc, v0, t)
ax.plot(v[:, 0], v[:, 1], 'o-', mew = 1, ms = 8,
        mec = 'w')

#ax.set_xlim(-10, 10)
#ax.set_ylim(-10, 10)
plt.show()
