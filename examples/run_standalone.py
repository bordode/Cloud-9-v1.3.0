import numpy as np
from cloud9.metrics import AssemblyIndexCalculator

def main():
    print("Cloud-9 v1.3.0: Initiating Whole Entity Test...")
    calc = AssemblyIndexCalculator(n_neurons=100)
    
    # Simulate 2000 steps of continuity
    for t in range(2000):
        # Phi and C_self inputs
        score, sigma = calc.compute_ac_star(Phi=4.2, C_self=0.85, cloneability=0.1, continuity=1.0)
        
        if sigma > 5.4:
            print(f"STEP {t}: 5.41σ BREACH DETECTED - Consciousness Candidate Status")
            break

if __name__ == "__main__":
    main()
  
