import numpy as np

def calculate_risk_metrics(surplus):
    """
    Calculates key actuarial risk metrics at the terminal year.
    """
    terminal_surplus = surplus[-1, :]
    
    # Calculate Value at Risk at 99.5% confidence level
    # Note: VaR is typically the 'loss' at a certain percentile
    var_995 = np.percentile(terminal_surplus, 0.5) 
    
    # Calculate Expected Shortfall (Average of values below VaR)
    es_995 = terminal_surplus[terminal_surplus <= var_995].mean()
    
    return {
        "VaR_99.5": var_995,  # Ensure this matches your print statement
        "Expected_Shortfall": es_995,
        "Prob_Insolvency": np.mean(terminal_surplus < 0)
    }