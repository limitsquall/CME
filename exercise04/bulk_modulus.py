# -*- coding: utf-8 -*-
"""

Exercise 04 - Calculates the cohesive energy and the bulk modulus for selected materials

"""

# This section imports the Python packages required during this exercise.

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import ase.units

# this defines the mathematical function that is used to fit the data points

def parabola(x, a, b, c):
    return a*x**2 + b*x + c

colors = ['b', 'g', 'r', 'k'] # colors 

for k, material in enumerate(['Cu.txt', 'Ag.txt', 'Ni.txt', 'Pb.txt']): #'Ag.txt', 'Ni.txt', 'Pb.txt'
    lc, energy = np.loadtxt(material, unpack=True) # loads the calculated data from the current txt file.
    volume = lc**3 / 4. # calculate the atomic volume per atom from the lattice constants
    plt.plot(volume, energy, 'o', label=material, color=colors[k], ms=3) # plots the volume per atom constant over the energy, the label specifies what will be printed in the legend
    popt, pcov = scipy.optimize.curve_fit(parabola, volume, energy, p0=[1, 1, -3]) # fits a parabolic curve to the data points
    print('a:',format(popt[0]))
    print('b:',popt[1])
    print('c:',popt[2])
    Vmin = -popt[1]/(2 * popt[0]) # is the minimal volume of the fit
    K = 2 * popt[0] * Vmin / ase.units.GPa # is the bulk modulus, see exercise sheet
    Ec = -popt[1]**2/(4*popt[0]) + popt[2] # calculates the cohesive energy, see exercise sheet
    xdata = np.linspace(volume[0], volume[-1], 1000) # only used for plotting
    # print(volume)
    plt.plot(xdata, parabola(xdata, *popt), '-',
             label='K={:.2f} GPa, E$_c$ = {:.2f} eV'.format(K, Ec), color=colors[k], linestyle='dotted') # plots the fit
    
plt.xlabel('Volume per atom [$\\AA^3$]') # label of the x-axis
plt.ylabel('Energy per atom [eV]') # label of the y-axis
plt.legend() # plots the legend
plt.savefig('Volume_vs_Energy.png', dpi=300) # saves the figure in a file
plt.show() # show the current graph