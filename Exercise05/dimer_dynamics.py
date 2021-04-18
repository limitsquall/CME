# -*- coding: utf-8 -*-
"""

Exercise 05 - Dimer dynamics

"""

# This section imports the Python packages required during this exercise.

import ase
#from MorseCalculator import MorsePotential
import MorseCalculator
import ase.io  
import Verlet
from ase import units
#import ase.calculators.morse

# Parameters for the Morse potential
D = 1.0
r0 = 1.0
alpha = 1.0

atoms = ase.Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.95]])
atoms.set_calculator(MorseCalculator.MorsePotential(D=D, alpha=alpha, r0=r0))

dyn = Verlet.VelocityVerlet(atoms, dt=1 * units.fs,
                     trajectory='md.traj', logfile='md.log')
dyn.run(200)  # take 1 steps

ase.io.write('md.xyz', ase.io.read('md.traj@:'))

print(atoms.get_positions()) # prints the position in units of angstroms
print(atoms.get_velocities() * units.fs) # print the velocities in units of angstroms/fs