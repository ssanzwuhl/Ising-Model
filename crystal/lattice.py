import numpy as np
from copy import copy
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

#Simulation of a 2 d square crystal lattice. Will try to implement random movement
#due to thermal activation.
#todo:
#   Implement lattice
#   Implement periodic boundary conditions
#   Implement harmonic interactions (only compression? Shear stress?
#   Implement non square lattice possibilities? I.e graphene

class Lattice:
    def __init__(self, size, basis):
        '''
        Creates a lattice
            Parameters: 
                (Nx, Ny): A numpy array characterizing the number
                                 of cells along the x and y directions
                (a1, a2): A numpy array of vectors of the vectors in the
                                Bravais lattice basis vectors
        '''
        self.size = size
        self.Nx, self.Ny = self.size
        self.basis = basis
        self.a1, self.a2 = self.basis
        self.atoms = np.array([[0., 0.]]*Nx*Ny) #the atoms are a 1-d array of 2-d arrays
                                                #of dimensions Nx*Ny. Every Nx cells ny += 1
                                                #This is the displacement! The lattice is calculated latter
        self.lattice = np.zeros_like(self.atoms)

    def generate_lattice(self):
        """
        Generates the lattice in question with the equation R = nx a1 + ny a2
        """
        for ny in range(Ny):
            for nx in range(Nx):
                self.lattice[nx+ny*Nx] += nx * a1 + ny * a2

    def random_lattice(self):
        return 2*(np.random.random((self.atoms.shape)) - 0.5)

    def displace(self, size=0.1):
        self.atoms += self.random_lattice() * size

    def force(self, k=0.001):
        """
        Calculate the force between a particle i, j and its neighbours i+/-1, j+/-Nx
        Will only assume harmonic forces
        Assume periodic boundary conditions
        """
        self.forces = np.zeros_like(self.atoms)
        self.forces -= 100*k*self.atoms
        Nx, Ny = self.size
        for ny in range(Ny):
           for nx in range(Nx):
               #if ny==0:
#                   if nx==0:
#                        self.forces[nx + ny*Nx] += k*(self.positions[nx + (ny+1)*Nx]
#                                                    +self.positions[nx + (ny-1)*Nx]
#                                                    +self.positions[nx+1 + ny*Nx ]
#                                                    +self.positions[nx-1 + ny*Nx ]
#                                                    -4*self.positions[nx + ny*Nx])
#
                
                try:
                    self.forces[nx + ny*Nx] += k*(self.positions[nx + (ny+1)*Nx]
                                                +self.positions[nx + (ny-1)*Nx]
                                                +self.positions[nx+1 + ny*Nx ]
                                                +self.positions[nx-1 + ny*Nx ]
                                                -4*self.positions[nx + ny*Nx])
                except IndexError: 
                    pass

    def next_step(self, dt):
        """
        Integrate the evolution of the system using Verlet integration
        """
        self.force(k=10)
        
        self.next = 2*self.atoms - self.prev + self.forces*dt**2
        self.prev = copy(self.atoms)
        self.atoms = copy(self.next)

    def animate_lattice(self, duration=5, fps=1/100):
        #this should depend on an update function,
        #for generality purposes
        self.positions = self.lattice + self.atoms
        line, = ax.plot(self.positions[:, 0], self.positions[:, 1], 'bo')
        line2, = ax.plot(self.lattice[:, 0], self.lattice[:, 1], 'go', ms=4, alpha=0.5)

        self.prev = copy(self.atoms)
        self.atoms = self.prev + self.random_lattice()*0.01

        def animate(i):
            self.next_step(fps)
            self.positions = self.lattice + self.atoms
            line.set_data(self.positions[:, 0], self.positions[:, 1])
            return line,

        ani = FuncAnimation(fig, animate, frames=int(duration/fps), interval=fps)
        plt.show()



if __name__ == '__main__':
    fig, ax = plt.subplots()
    Nx = 10
    Ny = Nx
#    a1 = np.array((.5, np.cos(30)))
#    a2 = np.array((-0.5, np.cos(30)))
    a1, a2 = np.eye(2)
    lattice = Lattice((Nx, Ny), (a1, a2))
    lattice.generate_lattice()
    lattice.animate_lattice()
    #for frame in range(100):
    #    plt.pause(1/500)
    #    lattice.displace(size=0.2)
    #    ax.clear()
    #    ax.plot(lattice.atoms[:, 0], lattice.atoms[:, 1], 'bo')
    #    plt.draw()
    #lattice.animate_lattice()
