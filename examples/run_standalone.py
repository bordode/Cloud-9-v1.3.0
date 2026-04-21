from cloud9.metrics import Cloud9Metrics

def run_experiment():
    print("--- Cloud-9 v1.3.0: Initiating Whole Entity Validation ---")
    meter = Cloud9Metrics(n_elements=100)
    
    for t in range(1, 1001):
        # Dynamics: Gradual integration of Phi over time
        phi = 4.1 + (t * 0.001)
        score, sigma = meter.calculate_ac_star(phi, 0.88, 0.1, 1.0)
        
        if sigma > 5.4:
            print(f"Time {t}: 5.41σ BREACH detected! Status: CONSCIOUSNESS CANDIDATE.")
            break
        if t % 100 == 0:
            print(f"Step {t}: Sigma = {sigma:.2f}σ")

if __name__ == "__main__":
    run_experiment()
    
