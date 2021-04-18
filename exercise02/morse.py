# -*- coding: utf-8 -*-
"""

Exercise 02 - the Morse potential

"""

# This section imports the Python packages required during this exercise.

import matplotlib.pyplot as plt
import numpy
import ase
from ase.calculators.morse import MorsePotential
from ase.io import write

# Parameters for the Morse potential
D = 2
r0 = 1.5
alpha = 0.3

# These are the distances between the atoms for which we evaluate the energy 
distances = numpy.linspace(0.0, 10, 50) # creates an array of 24 equidistant points between 0.2 and 2.5
energies = []

# we calculate the energy of the system for each distances in the distances array
for d in distances: # iterates over all distances
    structure = ase.Atoms('H2', positions=[[0, 0, 0], [0, 0, d]]) # creates the particle system for the specific distance
    structure.set_calculator(MorsePotential(epsilon=D, rho0=alpha*r0, r0=r0)) # determines how the interaction is calculated between the particles
    energies.append(structure.get_potential_energy()) # calculates and appends the current energy to the array of energies

    if d == distances[0]:
        write('traj.xyz', structure, append=False) # writes the first configuration to the trajectory file
    else:
        write('traj.xyz', structure, append=True) # appends all other configurations to trajectory file


print(distances, energies)
plt.plot(distances, energies, 'o--') # plots the energies vs distances
plt.savefig("traja.pdf")