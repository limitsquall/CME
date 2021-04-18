# -*- coding: utf-8 -*-
"""

Exercise 08 

"""

# This section imports the Python packages required during this exercise.

from MorseCalculator import MorsePotential
from ase.io import write, read
from ase import units
from ase.md.verlet import VelocityVerlet

# Parameters for the Morse potential for Cu
D = 0.3429
r0 = 2.866
alpha = 1.3588

atoms = read('berendsen.traj', index=-1)
atoms.set_calculator(MorsePotential(D=D, alpha=alpha, r0=r0))

del atoms[39]

open('md.log', 'w').close() # clean current log file
dyn = VelocityVerlet(atoms, dt=5 * units.fs,
                     trajectory='md.traj', logfile='md.log')

dyn.run(10000)
write('md.xyz', read('md.traj@:'))

# Here is some code missing!
