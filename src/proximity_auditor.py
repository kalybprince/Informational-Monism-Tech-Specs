# TR-001 Proximity Auditor v1.0
# Reference implementation for the 1.12 Bridge and 1.81 Substrate

import math

# Universal Constants from the TR-001 Registry
AXIOM_PROXIMITY = 1.12      # The Bridge (Optimal Seating)
NEWTON_GREGORY_LIMIT = 12   # The Wall (Geometric Cap)
LEGACY_NOISE_RATIO = 1.618  # The Error (Turbulent Expansion)

def audit_system_integrity(nodes):
    """
    Scans the system for Thermal Registration Errors and 
    geometric frustration within the 12-Link Wall.
    """
    total_thermal_debt = 0.0
    
    for node in nodes:
        neighbors = node.get_active_connections()
        num_neighbors = len(neighbors)
        
        # 1. Check for the "Snap" (N > 12)
        if num_neighbors > NEWTON_GREGORY_LIMIT:
            print(f"ALERT: Node {node.id} has {num_neighbors} links. 'The Snap' detected.")
            node.status = "DECOHERENT"
            
        # 2. Check for Proximity Compression (The 1.12 Bridge)
        for neighbor in neighbors:
            # Distance / Radius ratio
            proximity_ratio = calculate_radial_ratio(node, neighbor)
            
            if proximity_ratio < AXIOM_PROXIMITY:
                # Calculate the Entropy Tax based on the compression 
                # toward the 1.618 error zone.
                deviation = AXIOM_PROXIMITY - proximity_ratio
                thermal_tax = deviation * math.log(num_neighbors)
                
                total_thermal_debt += thermal_tax
                print(f"REGISTRATION ERROR: Node {node.id} <-> {neighbor.id}")
                print(f"Ratio: {proximity_ratio:.3f} | Tax: {thermal_tax:.4f}")

    return total_thermal_debt
