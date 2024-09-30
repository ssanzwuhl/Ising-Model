import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, odeint
import numpy as np


class System:
	def __init__(self, state, force, mass, charge, width, dt, T):
		"""Parameters:
			initial state
			state = [[x1, y1, vx1, vy1],
					 [x2, y2, vx2, vy2],
						...], where len(state0) = N
			force = force(p1, p2, *kw) takes two particles as input
										and returns the interaction
										between them
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
		state = np.array(state)
		r = np.ravel(state[:, :2])
		v = np.ravel(state[:, 2:])
		self.state = np.array((*r, *v))#[x1, y1, ..., vx1, vy1, ...]
		self.width = width
		self.mass = mass
		self.charge = charge
		self.dt = dt 
		self.T = T
		#self.force = force #A user defined function
							#to calculate the interaction
							#force between two particles


	def particle(self, state, i):
		"""Returns the ith particle"""
		N = len(state)//4
		pi = np.array([state[2*i], state[2*i+1], state[2*i + 2*N],
				state[2*i+1+2*N]])
		return pi

	def force(self, p1, p2):
		r = p1[:2] - p2[:2]
		return r

	def acceleration(self, state):
		"""Returns an acceleration matrix,
		where every row vector in this matrix
		is the acceleration vector of its 
		respective particle"""
		acceleration = np.zeros(2*self.N) #A null vector consisting of 
										  #2N elements, ax_i and ay_i
		for i in range(0, self.N):
			pi = self.particle(state, i)
			#Here one would write also a bounce function to take
			#the boundaries of the problem into account
			for j in range(0, i):
                            #print("Particle {} with particle {}".format(i, j))
                            pj = self.particle(state, j)
                            F = self.force(pi, pj)
                            mi = self.mass[i]
                            mj = self.mass[j]
                            acceleration[2*i:2*i+2] -= F/mi
                            acceleration[2*j:2*j+2] += F/mj
		return acceleration	

	def dstatedt(self, t, state):
		
		a = self.acceleration(state) #a is an acceleration vector of the whole system
		dstate = np.zeros(4*self.N) #[0, 0, ..., 0, 0, ...] those are
		dstate[:2*self.N] += state[2*self.N:]
		dstate[2*self.N:] += a
		self.counter += 1
		return dstate

	def euler(self):
		"""Euler method"""
		for i in np.arange(0, self.T, self.dt):
			self.state += self.dstatedt() * self.dt

	def integrate(self):
		"""Computes entire trajectory of the two particles"""
		solution = solve_ivp(self.dstatedt, (0, self.T), self.state, dense_output=True)
		return solution
	
	def integrate_new(self):
		"""Computes entire trajectory of the two particles, 
			returning it as a T x N x 4 matrix, being T
			the amount of instants the solver considered"""
		solution = solve_ivp(self.dstatedt, (0, self.T), self.state)
		Y = solution.y
		#print(self.particle(solution.y[:, 0], 0))
		#print(Y)
		sol = np.zeros((len(Y[0]), self.N, 4))
		for i, instant in enumerate(Y.T):
			for p in range(self.N):
				sol[i, p] += self.particle(instant, p)

		print("Done!")
		return sol
		
	def integrate_odeint(self):
		self.counter = 0
		"""Computes entire trajectory of the two particles, 
			returning it as a T x N x 4 matrix, being T
			the amount of instants the solver considered"""
		solution = odeint(self.dstatedt, self.state,
							 np.arange(0, self.T, self.dt), tfirst=True)

		sol = np.zeros((len(solution[:, 0]), self.N, 4))
		for i, instant in enumerate(solution):
			for p in range(self.N):
				sol[i, p] += self.particle(instant, p)

		print("Done!")
		return sol

if __name__ == "__main__":
	def force(i, j):
		return np.zeros(2)
	np.random.seed(0)
	P1 = np.random.random(4)
	P2 = np.random.random(4)
	state0 = [P1, P2]
	mass = [4, 8]
	charge = [1, -1]
	width = 20	
	T = 10
	dt = 0.5
	sim = System(state0, force, mass,  charge, width, dt, T)
	#solution = sim.integrate_new()
	solution = sim.integrate_odeint()
	print(solution.shape)
	#print(solution.y)
