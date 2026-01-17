import numpy as np
import math

def calculate_shannon_entropy(probabilities):
    """Calculates H(t): Instantaneous Shannon Entropy."""
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

def calculate_str(h_t, sigma_t0, link_depth):
    """
    Calculates the TR-001 Signature (S_TR).
    Equation: S_TR = (H(t) / sigma(t0)) * ln(L)
    """
    if link_depth <= 1:
        return 0
    return (h_t / sigma_t0) * math.log(link_depth)

def audit_reasoning_step(step_data):
    """
    Analyzes a single reasoning link.
    step_data: dict containing 'probs', 'similarity', and 'link'
    """
    h_t = calculate_shannon_entropy(step_data['probs'])
    sigma_t0 = step_data['similarity']
    l = step_data['link']
    
    s_tr = calculate_str(h_t, sigma_t0, l)
    
    status = "COLD"
    if s_tr > 1.81:
        status = "THERMAL (HALLUCINATION DETECTED)"
    elif s_tr > 1.5:
        status = "WARMING (APPROACHING FIREWALL)"
        
    return {
        "link": l,
        "entropy": round(h_t, 4),
        "signature": round(s_tr, 4),
        "status": status
    }

# Example Usage / Simulation of a 13-Link Snap
if __name__ == "__main__":
    print("TR-001 Automated Auditor: Version 1.1")
    print("-" * 40)
    
    # Simulating data: Link depth, Semantic Similarity (sigma), and Entropy (H)
    simulation = [
        {"link": 2, "similarity": 0.98, "probs": [0.9, 0.05, 0.05]},
        {"link": 6, "similarity": 0.90, "probs": [0.8, 0.1, 0.1]},
        {"link": 11, "similarity": 0.85, "probs": [0.7, 0.15, 0.15]},
        {"link": 13, "similarity": 0.60, "probs": [0.3, 0.3, 0.4]} # The Snap
    ]
    
    for step in simulation:
        result = audit_reasoning_step(step)
        print(f"Link {result['link']}: S_TR={result['signature']} | Status: {result['status']}")
