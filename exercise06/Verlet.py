# -*- coding: utf-8 -*-
"""
Velocity Verlet algorithm as implemented in ASE
"""

import numpy as np
from ase.md.md import MolecularDynamics


class VelocityVerlet(MolecularDynamics):
    def __init__(self, atoms, timestep=None, trajectory=None, logfile=None,
                 loginterval=1, dt=None, append_trajectory=False):
        # FloK: rename dt -> timestep and make sure nobody is affected
        if dt is not None:
            import warnings
            warnings.warn('dt variable is deprecated; please use timestep.',
                          DeprecationWarning)
            timestep = dt
        if timestep is None:
            raise TypeError('Missing timestep argument')

        MolecularDynamics.__init__(self, atoms, timestep, trajectory, logfile,
                                   loginterval,
                                   append_trajectory=append_trajectory)

    def step(self, f=None):

        atoms = self.atoms

        if f is None:
            f = atoms.get_forces()
            
        p = atoms.get_momenta()
        p += 0.5 * self.dt * f
        masses = atoms.get_masses()[:, np.newaxis]
        r = atoms.get_positions()

        atoms.set_positions(r + self.dt * p / masses)
  
        atoms.set_momenta(p, apply_constraint=False)

        f = atoms.get_forces(md=True)

        atoms.set_momenta(atoms.get_momenta() + 0.5 * self.dt * f)
        return f
