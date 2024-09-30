from system import System
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


"""def force(p1, p2):
        #Always forces in between particles
        c = 3e8

        k = 9e9
        epsilon = 1/(4*np.pi*k)
        mu = 1/epsilon/c**2

        v1 = np.array((*p1[2:], 0.))
        v2 = np.array((*p2[2:], 0.))
        r = p2[:2] - p1[:2] #[:2] are the positions of the particles,
						#[2:] are the speeds
        rr = np.linalg.norm(r)

        q2 = -1 #q1 = 1

        E = k*q2*r/rr**3
        B = 1/c**2 * np.array((0, 0, np.cross(v2, E)))
        F = np.array((0, 0, np.cross(v1, B))) + E
        return F
"""
def force(p1, p2):
    return 0

#np.random.seed(0)

N = 3
state0 = np.random.random((N, 4)) #Random initial condition
mass = np.array([5]*N)
charge = np.random.random(N)
width = 1
dt = 1/30
T = 10

#Calculating center of mass speed
V = state0[:, 2]
m = np.reshape(mass, (N, 1))
MVcm = np.dot(m.T, V)
Vcm = MVcm/sum(m)

state0[:, 2] -= Vcm #This way the system stays put

sim = System(state0, force, mass, charge, width, dt, T)

solution = sim.integrate_odeint() #A (T, N, 4) matrix. Every T is a
								  #frame, every N is a particle and
								  #every 4 is a 'configurational' variable
								  #quote marks being because speed is 
								  #not a phase variable and configu-
								  #rational variables are only the po-
								  #sitions.

fig, ax = plt.subplots()

xmax = max(solution[:, :, 0].ravel())
xmin = min(solution[:, :, 0].ravel())
ax.set_xlim((xmin, xmax)) #Gets the highest and lowest x value

ymax = max(solution[:, :, 1].ravel())
ymin = min(solution[:, :, 1].ravel())
ax.set_ylim((ymin, ymax)) #Gets the highest and lowest y value

line, = ax.plot(solution[0, :, 0], solution[0, :, 1], 'bo')

def animate(i):
    line.set_data(solution[i, :, 0], solution[i, :, 1])
    return line,

ani = FuncAnimation(fig, animate, frames=int(T//dt), interval=int(1/dt))
ani.save(r'animation.gif', fps=1/dt)
plt.show()
