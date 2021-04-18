# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:54:23 2021

@author: limit
"""

# -*- coding: utf-8 -*-
"""

Exercise 07 - Relaxation of a Morse Cluster

"""

# This section imports the Python packages required during this exercise.

from MorseCalculator import MorsePotential
from ase.io import write, read
from ase import units
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.verlet import VelocityVerlet
from ase.optimize import FIRE
from ase.md.langevin import Langevin


# Parameters for the Morse potential for Cu
D = 0.3429
r0 = 2.866
alpha = 1.3588


atoms = FaceCenteredCubic(latticeconstant=1.5, symbol='Cu', pbc=False, size=(3,3,3))
atoms.center(vacuum=100)

atoms.set_calculator(MorsePotential(D=D, alpha=alpha, r0=r0))

dyn = FIRE(atoms, trajectory='relax.traj')

dyn.run(fmax=0.01)

write('relax.xyz', read('relax.traj@:')) # uncomment this line for Task 2


open('langevin_friction.log', 'w').close() # clean current log file
# dyn = VelocityVerlet(atoms, dt=1 * units.fs,
#                      trajectory='md.traj', logfile='md.log')

# dyn.run(1000)
# write('md.xyz', read('md.traj@:'))

dyn = Langevin(atoms, timestep= 5*units.fs, temperature = 2500*units.kB, friction = 0.002,
               trajectory='langevin_friction.traj', logfile='langevin_friction.log')

dyn.run(4000)
write('langevin_friction.xyz', read('langevin_friction.traj@:')) # uncomment this line for Task 3

