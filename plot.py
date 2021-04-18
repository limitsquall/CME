# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:13:23 2021

@author: limit
"""

from ase.io import read
import matplotlib.pyplot as plt
import numpy as np

time, posx, posy, posz = np.loadtxt('diffusion_position.txt', unpack=True)
plt.plot(posx, posy)

# a = np.loadtxt('diffusion_position.txt', skiprows=0)
# print(a[:,0])
# plt.plot(a[:,1], a[:,2])


# plt.plot(time, ke, label='ke')
# plt.plot(time, pe, label='pe')
plt.xlabel('x-pos') # label of the x-axis
plt.ylabel('y-pos') # label of the y-axis


