from sympy import *
import numpy as np
init_printing()
t = symbols('t')
r, theta, phi = symbols('r, theta, phi', cls = Function)

r = r(t)
theta = theta(t)
phi = phi(t)

"""
x = eval(input('x =  '))
y = eval(input('y =  '))
z = eval(input('z =  '))
"""

x = r*cos(theta)*sin(phi)
y = r*sin(theta)*sin(phi)
z = r*sin(phi)

r = np.array((x, y, z))
r_ = np.array((r, theta, phi))
A = np.zeros((3, 3))

for i in range(3):
    for j in range(3):
        A[i, j] += diff(r[i], r_[j])

pprint(A)

v = x_**2 + y_**2# + z_**2
pprint(simplify(v))




