import numpy as np

class CosmologicalShellProbe:
    """Simulates matter assembly on a 15.4 kpc spherical shell."""
    def __init__(self, radius=15.4):
        self.R = radius
        self.particles = np.random.randn(400, 3)
        self.particles /= np.linalg.norm(self.particles, axis=1)[:, None]
        self.particles *= radius

    def get_complexity(self):
        # Returns structural complexity metrics for the cosmic shell
        dist_matrix = np.linalg.norm(self.particles[:, None] - self.particles, axis=2)
        phi_proxy = np.mean(np.abs(np.corrcoef(dist_matrix[:50])))
        return phi_proxy
      
