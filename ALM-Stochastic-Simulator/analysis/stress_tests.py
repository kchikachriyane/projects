import numpy as np

def run_interest_rate_shock(rates, asset_function, liability_function, shock_size=0.02):
    """
    Applies a parallel shift to the interest rate paths 
    and re-calculates the surplus.
    """
    # 1. Apply the shock (+200bps)
    shocked_rates = rates + shock_size
    
    # 2. Re-value Assets and Liabilities under the new rates
    shocked_assets = asset_function(shocked_rates)
    shocked_liabilities = liability_function(shocked_rates)
    
    # 3. Compute New Surplus
    shocked_surplus = shocked_assets - shocked_liabilities
    
    return shocked_surplus