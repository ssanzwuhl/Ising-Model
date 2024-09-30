from itertools import count
import numpy as np
from copy import deepcopy
import matplotlib as mpl
import matplotlib.pyplot as plt

#Numerical solution of the ising model. This system's Hamiltonian
#is -J*sum(s_i s_j) - H*sum(s_i), being s_i the spin of the particle i.
#It is summed over the for nearest j particles of the particle i.


class IsingModel:
    def __init__(self, N, T, J=1, H=0):
        self.config = np.random.choice((1, -1), size=(N, N)) #Initialize
            #Ising model with NxN particles with 1 or -1 spin
        self.T = T #system's temperature
        self.N = N #Systems side
        self.J = J #System's interaction energy
        self.H = H #System's external field

    
    def single_update(self): #Update a single time
        #If a change in the i=[i, j] particle's spin leads to a negative
        #increment of the system's energy, then it flips it spin. If the 
        #energy change is positive, it flips with a probability 
        #P = exp(-\beta \Delta E)
        i = np.random.randint(self.N)
        j = np.random.randint(self.N)
        s = self.config[i, j]

        #With periodic boundary conditions, calculate the spin of the 
        #neighbouring particles. Named N E S W after the 4 possible 
        #directions (north, east, south, west)

        N = self.config[(i+1)%self.N, j]
        S = self.config[(i-1)%self.N, j]
        E = self.config[i,( j+1)%self.N]
        W = self.config[i, (j-1)%self.N]

        DeltaE = self.J*s*(N + S + E + W) #If the particle spins,
                                        #the change in the energy
        DeltaEff = 0 #The real change in energy

        if DeltaE < 0:
            self.config[i, j] *= -1
            DeltaEff = DeltaE

        else: 
            if np.random.random() < np.exp(-DeltaE/self.T):
                self.config[i, j] *= -1
                DeltaEff = DeltaE

        return DeltaEff

    def evolve(self, n_iterations=400):
        fig, ax = plt.subplots()
        im = ax.imshow(self.config)
        for i in range(n_iterations):
            ax.cla()
            ax.imshow(self.config, cmap=mpl.cm.winter)
            print('miau')
#            im.set_data(self.config)
#            display.display(plt.gcf())
#            display.clear_output(wait=True)
#            self.single_update()

N = 150
T = 0.15
J = 15
model = IsingModel(N, T, J=J)

fig, ax = plt.subplots()

n_iterations = 100000
data = []
update = 1000
#for step in range(n_iterations):
for step in count(1):
    model.single_update()
    if step%update == 0:
        ax.set_xticks([])
        ax.set_yticks([])
        ax.cla()
        ax.imshow(model.config)
        plt.pause(0.01)


#print("Animation begins")
#for step, frame in enumerate(data):
#    if step%100 == 0:
#        ax.cla()
#        ax.imshow(frame)
#        plt.pause(0.01)

print("Animation completed")
plt.show()
