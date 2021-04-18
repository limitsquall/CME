# -*- coding: utf-8 -*-
"""

Exercise 08 

"""

from ase.io import read
from ase.neighborlist import neighbor_list
import numpy as np

traj = read('md.traj', index='0:10000')    #:

pos = []
time = []

for k, image in enumerate(traj):
    print(k)
# calculate the number of neighbors for each particle (called coordination) within a cutoff of 3.6 Angstrom 
    i = neighbor_list('i', image, 3.6)
    coord = np.bincount(i) 
    print("coord",coord)
    if len(coord[coord==5]) == 6 and len(coord[coord==6]) == len(image) - 6:
        pos.append(image[coord==5].get_center_of_mass())
        time.append(k * 5) # in fs
        
pos = np.array(pos)
time = np.array(time)
np.savetxt('diffusion_position.txt', np.c_[time, pos[:,0], pos[:,1], pos[:,2]])
