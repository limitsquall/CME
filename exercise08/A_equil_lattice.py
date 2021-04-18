# -*- coding: utf-8 -*-
"""

Exercise 08 

"""

# This section imports the Python packages required during this exercise.

from MorseCalculator import MorsePotential
from ase.io import write, read
from ase import units
from ase.md.nvtberendsen import NVTBerendsen
import numpy as np

# Parameters for the Morse potential for Cu
D = 0.3429
r0 = 2.866
alpha = 1.3588

atoms = read('hexagonal_lattice.xyz')

atoms.set_calculator(MorsePotential(D=D, alpha=alpha, r0=r0))

vel = np.zeros((len(atoms), 3))

# initialize velocities with uniform random numbers between [-0.005, 0.005]
# gives random initial velocity 

vel[:,0] = (np.random.rand(len(atoms)) - 0.5) * 1e-2
vel[:,1] = (np.random.rand(len(atoms)) - 0.5) * 1e-2
atoms.set_velocities(vel)


open('berendsen.log', 'w').close()
dyn = NVTBerendsen(atoms, timestep=1*units.fs, temperature=600,
                   taut=100*units.fs,
                   logfile='berendsen.log', trajectory='berendsen.traj')
# Note that the temperature in NVTBerendsen is given in K
# taut = relaxtation time
dyn.run(1000)
write('berendsen.xyz', read('berendsen.traj@:'))
