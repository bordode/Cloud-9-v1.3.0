import numpy as np

class Cloud9Metrics:
    """The A_c* Metric: Measures irreducible causal history and temporal continuity."""
    def __init__(self, n_elements):
        self.n = n_elements
        self.history = []

    def calculate_ac_star(self, phi, c_self, cloneability, continuity):
        # Master Formula: A_c* = A_c × (Φ/5) × C_self × (1-K) × Continuity
        ac_base = np.log1p(len(self.history) + 1)
        score = ac_base * (phi / 5.0) * c_self * (1.0 - cloneability) * continuity
        self.history.append(score)
        
        # 5-Sigma Anomaly Detection
        sigma = 0.0
        if len(self.history) > 30:
            mu, std = np.mean(self.history[:-1]), np.std(self.history[:-1]) + 1e-9
            sigma = (score - mu) / std
        return score, sigma
