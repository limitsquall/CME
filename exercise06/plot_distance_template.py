# -*- coding: utf-8 -*-
"""

Exercise 06 

"""

from ase.io import read
import matplotlib.pyplot as plt
import numpy as np

def cosine(x, A, omega, B):
    return A * np.cos(omega * x) + B


traj = read('md.xyz@:')

d = []
time = []


for image in traj:
    # print(image.get_distance(0, 1))
    d.append(image.get_distance(0, 1))

print(len(d))
time = np.linspace(0, 200, len(d))

plt.plot(time, d, 'o--', color = 'red')

xdata = np.linspace(0, 200, 100)
plt.plot(xdata, cosine(xdata, -0.5, 0.1956727, 1), label=cosine)

#cosine = -0.05 * np.cos(0.195672763099312 * time * 0.1) + 1

#plt.plot(time, cosine)

plt.xlabel('Time (fs)') # label of the x-axis
plt.ylabel('Diastance ($\\AA$)') # label of the y-axis