# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 12:27:22 2020

@author: limit
"""

from ase.io import read
import matplotlib.pyplot as plt
import numpy as np

time, etot, pe, ke, T = np.loadtxt('md_energy.log', skiprows=1, unpack=True)

print(len(time))

plt.plot(time, etot, label='Etot')
plt.plot(time, pe, label='Epot')
plt.plot(time, ke, label='Ekin')

def temperature(ke, k, N):
    return 2 / 3 / N / k * ke / 6241509000000000000

for i in ke:
    k = 1.38064852 * 10e-23
    N = 2
    p = temperature(ke, k, N)
 
print(p)
    
#plt.plot(time, temperature(ke, k, N))


#plt.plot(time, temperature(ke,)

