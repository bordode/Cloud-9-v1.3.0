import numpy as np
from dataclasses import dataclass

@dataclass
class A_cResult:
    t: int
    A_c_star: float
    sigma_anomaly: float
    Phi: float
    C_self: float
    cloneability: float

class AssemblyIndexCalculator:
    """Calculates the Assembly Index Star (A_c*) for neuromorphic/cosmic data."""
    def __init__(self, n_neurons: int):
        self.n = n_neurons
        self.baseline_scores = []

    def compute_ac_star(self, Phi, C_self, cloneability, continuity):
        # A_c* = A_c × (Φ/Φ_max) × C_self × (1 − cloneability) × continuity
        A_c_base = np.log1p(self.n) 
        score = A_c_base * (Phi / 5.0) * C_self * (1 - cloneability) * continuity
        
        sigma = 0.0
        if len(self.baseline_scores) > 20:
            mu, std = np.mean(self.baseline_scores), np.std(self.baseline_scores)
            sigma = (score - mu) / (std + 1e-9)
            
        self.baseline_scores.append(score)
        return score, sigma
      
