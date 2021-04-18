# -*- coding: utf-8 -*-
"""

Exercise 08 

"""

# This section imports the Python packages required during this exercise.

from MorseCalculator import MorsePotential
from ase.io import write, read, Trajectory
from ase.optimize import FIRE
import matplotlib.pyplot as plt

# Parameters for the Morse potential for Cu
D = 0.3429
r0 = 2.866
alpha = 1.3588

atoms = read('berendsen.traj', index=-1)
atoms.set_calculator(MorsePotential(D=D, alpha=alpha, r0=r0))

dyn = FIRE(atoms, trajectory='relax.traj')
dyn.run(fmax=0.01)
write('relax.xyz', read('relax.traj@:'))

del atoms[39]

energies = []
displacement = []

traj = Trajectory('move.traj', 'w')

for i in range(30):
    energies.append(atoms.get_potential_energy())
    displacement.append(i * 0.1)
    atoms[37].position[0] += 0.1
    traj.write(atoms)

write('move.xyz', read('move.traj@:'))


plt.plot(displacement, energies, 'o--')
plt.show()