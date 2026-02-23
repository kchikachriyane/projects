import numpy as np

def calculate_bel(interest_rate_paths, cash_flows=None):
    """
    Best Estimate Liabilities (BEL):
    Discounts future cash flows using stochastic interest rate paths.
    """
    # interest_rate_paths shape: (Years, Scenarios)
    n_years, n_scenarios = interest_rate_paths.shape
    
    # If no cash flows are provided, we create a synthetic set (e.g., 50 units/year)
    if cash_flows is None:
        cash_flows = np.full(n_years, 50.0)
        
    bel_paths = np.zeros((n_years, n_scenarios))
    
    # Logic: At each year 't', we discount all future cash flows back to 't'
    for t in range(n_years):
        remaining_cf = cash_flows[t:]
        # Get rates from year t onwards
        future_rates = interest_rate_paths[t:, :]
        
        for s in range(n_scenarios):
            # Time indices relative to year t
            durations = np.arange(len(remaining_cf))
            # Standard continuous discounting
            discount_factors = np.exp(-future_rates[:, s] * durations)
            bel_paths[t, s] = np.sum(remaining_cf * discount_factors)
            
    return bel_paths