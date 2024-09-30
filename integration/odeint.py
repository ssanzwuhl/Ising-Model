import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy import concatenate
from matplotlib.animation import FuncAnimation
import numpy as np


class System:
	def __init__(self, state, mass, charge, width, dt, T):
		"""Parameters:
			initial state
			state = [[x1, y1, vx1, vy1],
					 [x2, y2, vx2, vy2],
						...], where len(state0) = N
			mass = [m1, m2, ...] mass vector
			charge = [q1, q2, ...] mass vector
			width = twice the width of the box where the problem is set
			dt = time interval over which we are integrating """
		#I'd like to use a Particle class, but I will try to do this 
		#using a state matrix. If i were to use a particle class
		#I should build a state matrix the same way, but in a 
		#state0 = [[*p.r, *p.v] for p in particles] 
		#being particles an already initiated list of Particle instances
		self.N = len(state)
		r = np.ravel(state[:, :2])
		v = np.ravel(state[:, 2:])
		self.state = np.array((*r, *v))#[x1, y1, ..., vx1, vy1, ...]
		self.width = width
		self.mass = mass
		self.charge = charge
		self.dt = dt 
		self.T = T

	def force(self, p1, p2):
		"""Computes the interaction force between 
		2 particles, p1 and p2."""
		return np.zeros(2) #Simulating a free particle

	def acceleration(self):
		"""Returns an acceleration matrix,
		where every row vector in this matrix
		is the acceleration vector of its 
		respective particle"""
		acceleration = np.zeros(2*self.N) #A null vector consisting of 
									 #2N elements, ax_i and ay_i
		for i in range(0, self.N):
			pi = [self.state[2*i], self.state[2*i+1], self.state[2*i + 2*self.N],
														self.state[2*i+1+2*self.N]]
			#Here one would write also a bounce function to take
			#the boundaries of the problem into account
			#print(pi)
			for j in range(0, i):
				pj = [self.state[2*j], self.state[2*j+1], self.state[2*j + 2*self.N],
														self.state[2*j+1+2*self.N]]
				#print(pj, end='aaaaaaaaaaaaaaaaaaaa')
				F = self.force(pi, pj)
				mi = self.mass[i//2]
				mj = self.mass[j//2]
				acceleration[i:i+2] += F/mi
				acceleration[j:j+2] -= F/mj
		return acceleration	

	def dstatedt(self, t, state):
		print(state)
		a = self.acceleration() #a is an acceleration vector of the whole system
		dstate = np.zeros(4*self.N) #[0, 0, ..., 0, 0, ...] those are
		dstate[:2*self.N] += state[2*self.N:]
		#It looks as if it were adding the position, but I don't know
		#how to deal with that at the moment. I will do this though.
		dstate[2*self.N:] += a
		print(dstate)
		print('\n')
		return dstate

	def euler(self):
		"""Euler method"""
		for i in np.arange(0, self.T, self.dt):
			self.state += self.dstatedt() * self.dt

	def integrate(self):
		"""Computes entire trajectory of the two particles"""
		return solve_ivp(self.dstatedt, (0, self.T), self.state)
		#TODO: write dstate as a function that returns 



		
#P1 = [float(x) for x in range(4)]
#P2 = [float(x) for x in range(4, 8)]
P1 = np.random.random(4)
P2 = np.random.random(4)
state0 = np.array([P1, P2])
mass = [4, 8]
charge = [1, -1]
width = 20	
dt = 0.05

sim = System(state0, mass, charge, width, dt, 100)

solution = sim.integrate()

#print(solution.y)
