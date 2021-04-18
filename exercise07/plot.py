from ase.io import read
import matplotlib.pyplot as plt
import numpy as np

#time, etot, pe, ke, T = np.loadtxt('langevin.log', skiprows=1, unpack=True)
#plt.plot(time, pe, label='Temp')

a = np.loadtxt('langevin_final.log', skiprows=1)
# print(a[:,0])
plt.plot(a[:,0], a[:,2])

b = np.loadtxt('langevin.log', skiprows=1)
plt.plot(b[:,0], b[:,2])

# plt.plot(time, ke, label='ke')
# plt.plot(time, pe, label='pe')
# plt.xlabel('Time (ps)') # label of the x-axis
# plt.ylabel('Temp ()') # label of the y-axis


