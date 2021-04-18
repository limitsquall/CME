# -*- coding: utf-8 -*-
"""

Exercise 03 - Plot of lattice constant vs energy for selected materials

"""

# This section imports the Python packages required during this exercise.

import matplotlib.pyplot as plt
import numpy as np

for material in ['Cu.txt', 'Ag.txt', 'Ni.txt', 'Pb.txt']:
    print(material)
    a = np.loadtxt(material)
    print(a)
    lc, energy = np.loadtxt(material, unpack=True) # loads the calculated data from the current txt file.
    print(lc)
    plt.plot(lc, energy, 'o--', label=material) # plots the lattice constant over the energy, the label specifies what will be printed in the legend
    # 'O--' -> how to show the style
plt.xlabel('Lattice Constant [$\\AA$]') # label of the x-axis
plt.ylabel('Energy per atom [eV]') # label of the y-axis
plt.legend() # plots the legend
print(lc, energy)
plt.savefig('LatticeConstant_vs_Energy.png', dpi=300, bbox_inches='tight') # saves the figure in a file
plt.show() # show the current graph