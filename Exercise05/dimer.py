# -*- coding: utf-8 -*-
"""

Exercise 05

"""

import ase
from MorseCalculator import MorsePotential # imports the MorsePotential from MorseCalculator.py

# Parameters for the Morse potential
D = 1.0
r0 = 1.0
alpha = 1.0

structure = ase.Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.5]]) # creates the particle system for the specific distance
structure.set_calculator(MorsePotential(D=D, alpha=alpha, r0=r0)) # determines how the interaction is calculated between the particles
print(structure.get_forces()) # calculates and prints the forces
