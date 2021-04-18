# -*- coding: utf-8 -*-
"""

Exercise 06 

"""

from ase.io import read
import matplotlib.pyplot as plt
import numpy as np

traj = read('md.xyz@:')

d = []
time = []


for image in traj:
    # print(image.get_distance(0, 1))
    d.append(image.get_distance(0, 1))

    
time = np.linspace(0,len(traj), len(traj))
plt.plot(time, d, 'o--', color = 'red')

cosine = -0.05 * np.cos(0.195672763099312 * time) + 1

plt.plot(time, cosine)

plt.xlabel('Time (fs)') # label of the x-axis
plt.ylabel('Diastance ($\\AA$)') # label of the y-axis