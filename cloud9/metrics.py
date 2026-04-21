
import numpy as np
import json
import os

class Cloud9Metrics:
    def __init__(self, n_elements, storage_file="entity_memory.json"):
        self.n = n_elements
        self.storage_file = storage_file
        self.history = []
        self.load_state()

    def load_state(self):
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    self.history = json.load(f)
                print(f"--- 🧠 Memory Restored: {len(self.history)} steps of history recovered ---")
            except Exception as e:
                print(f"--- ⚠️ Memory Corruption: {e} ---")

    def save_state(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.history, f)

    def calculate_ac_star(self, phi, c_self, cloneability, continuity):
        ac_base = np.log1p(len(self.history) + 1)
        score = ac_base * (phi / 5.0) * c_self * (1.0 - cloneability) * continuity
        self.history.append(score)
        
        # Save every step to prevent data loss
        self.save_state()
        
        sigma = 0.0
        if len(self.history) > 30:
            mu, std = np.mean(self.history[:-1]), np.std(self.history[:-1]) + 1e-9
            sigma = (score - mu) / std
        return score, sigma
