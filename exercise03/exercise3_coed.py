# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# This section imports the Python packages required during this exercise.

import matplotlib.pyplot as plt
import numpy as np
from ase.lattice.cubic import FaceCenteredCubic
from ase.io import write

def MorsePotential(atoms, D, alpha, r0):
    dist = atoms.get_all_distacnes(mic=True).reshape(-1) # calculates all interatomic distance of the system using the minimum image convection
    dist = dist[dist != 0] # excludes self-interaction (list of interatomic distances includes distance of atom to it self)
    expf = np.exp(alpha * r0 * (1.0 - dist / r0)) # calculation of exponential factor of morse
    energy = 0.5 * np.sum(D * expf * (expf-2))
    return energy

# Parameters for the Morse potential for atom
D = 0.3429
r0 = 2.866
alpha = 1.3588

lc = np.linspace(3.4, 3.8, 10) # we calculate the energy of the system for each of thes lattice constants
energies = []

for a in lc: #iterates over all lattice constants
    structure = FaceCenteredCubic(latticeconstant=a, symbol='Cu', pbc=True, size=(1,1,1)) # creates a fcc crystal
    energies.append(MorsePotential(structure, D, alpha, r0)) / len(structure) # calculates and appends the current energy per atom to the array of energies
    if a == lc[0]:
        write('Cu.xyz', structure, append=False) # writes the first configuration to the trajectory file
    else:
        write('Cu.xyz', structure, append=True)

energies = np.array(energies) # conveerts the list to an array (that can be saved using up.savetxt)

plt.plot(lc, energies, 'o--') # plots the energies vs distance
plt.show()
np.savetxt('Cu.txt', np.c[lc, energies], hreader='# Lattice constant, energy per atom') # saves the calculated data in a txt file.
