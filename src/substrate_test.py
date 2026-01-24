import math

# Substrate Hardware Constants (CODATA 2018)
# These represent the "resolution" and "clock rate" of the Informational Substrate.
PLANCK_LENGTH = 1.616255e-35  
PLANCK_TIME = 5.391247e-44    

# The Emergent Throughput Limit (The Causal Inversion)
# In this framework, c is a derived performance ceiling, not a fundamental constant.
C_LIMIT = PLANCK_LENGTH / PLANCK_TIME 

def calculate_coherence(requested_rate, depth):
    """
    Evaluates the entropy floor across a recursive logic chain.
    """
    # Tolerance for standard floating point math (epsilon)
    if requested_rate > (C_LIMIT + 1e-9):
        # Entropy grows as the request exceeds the hardware's capacity
        overflow_ratio = requested_rate / C_LIMIT
        entropy = math.log(overflow_ratio) * depth
    else:
        # The logic is 'Native' to the substrate (High-Coherence/Low-Entropy)
        entropy = 0 
    
    # Returns 1.0 (Perfectly Aligned) to 0.0 (Total Decoherence)
    return max(0.0, 1.0 - entropy)

def run_diagnostic():
    print(f"TR-001-ALPHA Kernel Diagnostic")
    print(f"Substrate Hardware Limit (c): {C_LIMIT:,.2f} m/s")
    print("-" * 50)

    # Testing the standard Speed of Light (c_standard)
    c_standard = 299792458 

    for link in range(1, 13):
        score = calculate_coherence(c_standard, link)
        status = "ALIGNED" if score > 0.99 else "DECOHERENT"
        print(f"Link {link:02d}: Coherence = {score:.4f} | {status}")

    print("-" * 50)
    print("Diagnostic Complete: System in Phase-Locked Alignment.")

if __name__ == "__main__":
    run_diagnostic()
