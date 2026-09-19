"""
XR6 Pro - Core Engine
Authored by: Dr. Mohd Rahmat Nasyaa Bin Zulkifli, PhD (XR6 Labs HQ)
"""

def calculate_energy_efficiency(baseline_watts: float, optimized_watts: float) -> dict:
    if baseline_watts <= 0:
        raise ValueError("Baseline wattage mestilah lebih besar daripada 0.")
    
    reduction = ((baseline_watts - optimized_watts) / baseline_watts) * 100.0
    return {
        "baseline_watts": baseline_watts,
        "optimized_watts": optimized_watts,
        "power_reduction_percentage": round(reduction, 2),
        "status": "Optimal" if reduction > 0 else "Needs Optimization"
    }

