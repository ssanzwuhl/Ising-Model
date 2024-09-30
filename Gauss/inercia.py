from time import time, sleep
import matplotlib.pyplot as plt
from numpy import cumsum, exp


    
data = []
t0 = time()
a = input("miau: ")
cont = 0
#while a == "":
while cont < 20:
    t0 = time()
    #a = input('miau: ')
    sleep(exp(-cont))
    data.append(1/(time()-t0))
    cont += 1
fig, ax = plt.subplots()

ax.plot(data)
ax.plot(cumsum(data))
plt.show()
