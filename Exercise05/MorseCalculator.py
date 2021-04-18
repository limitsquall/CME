import numpy as np
from ase.calculators.calculator import Calculator


class MorsePotential(Calculator):
    """Morse potential.

    Default values chosen to be similar as Lennard-Jones.
    """

    implemented_properties = ['energy', 'forces']
    default_parameters = {'D': 1.0,
                          'alpha': 6.0,
                          'r0': 1.0}
    nolabel = True

    def __init__(self, **kwargs):
        Calculator.__init__(self, **kwargs)

    def calculate(self, atoms=None, properties=['energy'],
                  system_changes=['positions', 'numbers', 'cell',
                                  'pbc', 'charges', 'magmoms']):
        Calculator.calculate(self, atoms, properties, system_changes)

        D = self.parameters.D
        alpha = self.parameters.alpha
        r0 = self.parameters.r0

        # energy evaluation
        dist = self.atoms.get_all_distances(mic=True).reshape(-1) # calculates all interatomic distances of the system using the minimum image convention
        dist = dist[dist != 0] # excludes self-interaction (list of interatomic distances includes distance of atom to itself)
        expf = np.exp(alpha * r0 * (1.0 - dist / r0)) # calculation of exponential factor of morse
        energy = 0.5 * np.sum(D * expf * (expf - 2)) # evaluates Morse term for all distances and sums over the resulting energies

        # force evaluation
        preF = 2 * D * alpha
        dist_vec =  self.atoms.get_all_distances(mic=True, vector=True)
        dist = self.atoms.get_all_distances(mic=True)
        dist[dist==0] = 1e-9
        expf = np.exp(alpha * r0 * (1.0 - dist / r0))
        F2 = preF * expf * (expf - 1) / dist
        F2 = - dist_vec * F2[:, :, np.newaxis]
        forces = np.sum(F2, axis=1)
        
        self.results['energy'] = energy
        self.results['forces'] = forces
        