# -*- coding: utf-8 -*-
"""

Exercise 03 - Calculation of Lattice Constants of fcc crystals

"""

# This section imports the Python packages required during this exercise.

import matplotlib.pyplot as plt
import numpy as np
from ase.lattice.cubic import FaceCenteredCubic
from ase.io import write

def MorsePotential(atoms, D, alpha, r0):
    """
    Implementation of the Morse Potential. Needed since previous implementation was too slow.
    """
    dist = atoms.get_all_distances(mic=True).reshape(-1) # calculates all interatomic distances of the system using the minimum image convention
    dist = dist[dist != 0] # excludes self-interaction (list of interatomic distances includes distance of atom to itself)
    expf = np.exp(alpha * r0 * (1.0 - dist / r0)) # calculation of exponential factor of morse
    energy = 0.5 * np.sum(D * expf * (expf - 2)) # evaluates Morse term for all distances and sums over the resulting energies, 0.5 is needed to account for double counting.
    return energy
    
# Parameters for the Morse potential for Cu
D = 0.3429
r0 = 2.866
alpha = 1.3588

lc = np.linspace(3.4, 3.8, 10) # we calculate the energy of the system for each of these lattice constants 
energies = []

for a in lc: # iterates over all lattice constants
    structure = FaceCenteredCubic(latticeconstant=a, symbol='Cu', pbc=True, size=(1,1,1)) # creates a fcc crystal
    energies.append(MorsePotential(structure, D, alpha, r0) / len(structure)) # calculates and appends the current energy per atom to the array of energies
    if a == lc[0]:
        write('Cu.xyz', structure, append=False) # writes the first configuration to the trajectory file
    else:
        write('Cu.xyz', structure, append=True) # appends all other configurations to trajectory file

energies = np.array(energies) # converts the list to an array (that can be saved using np.savetxt)

plt.plot(lc, energies, 'o--') # plots the energies vs distances
print(lc, energies)
plt.show()
np.savetxt('Cu.txt', np.c_[lc, energies], header='# lattice constant, energy per atom') # saves the calculated data in a txt file.
