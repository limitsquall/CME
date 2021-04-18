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


open('md_fire.log', 'w').close() # clean current log file
dyn = VelocityVerlet(atoms, dt=1 * units.fs,
                     trajectory='md_fire.traj', logfile='md_fire.log')

dyn.run(1000)
write('md_fire.xyz', read('md_fire.traj@:'))
# write('langevin.xyz', read('langevin.traj@:')) # uncomment this line for Task 3
