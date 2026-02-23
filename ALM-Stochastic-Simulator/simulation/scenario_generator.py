import numpy as np
from simulation.scenario_generator import generate_correlated_shocks
def generate_correlated_shocks(n_scenarios, n_years, correlation_matrix):
    """
    Generates correlated random normals for multiple asset classes.
    correlation_matrix: 2x2 matrix for [Interest Rates, Equities]
    """
    # Cholesky Decomposition
    L = np.linalg.cholesky(correlation_matrix)
    
    # Generate independent shocks
    z_independent = np.random.standard_normal((2, n_scenarios, n_years))
    
    # Transform to correlated shocks
    z_correlated = np.einsum('ij,j...->i...', L, z_independent)
    
    return z_correlated[0], z_correlated[1] # Rate shocks, Equity shocks