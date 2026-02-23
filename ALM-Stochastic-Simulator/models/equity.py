import numpy as np

class EquityModel:
    def __init__(self, mu, sigma, s0):
        self.mu = mu        # Expected annual return
        self.sigma = sigma  # Annual volatility
        self.s0 = s0        # Initial stock price

    def simulate_with_shocks(self, T, n_scenarios, external_shocks, dt=1.0):
        """Simulates equity paths using correlated shocks from Cholesky decomposition."""
        n_steps = int(T / dt)
        t_axis = np.linspace(0, T, n_steps + 1).reshape(-1, 1)
        
        # Cumsum the external shocks to simulate the correlated Wiener process
        W = np.cumsum(external_shocks * np.sqrt(dt), axis=0)
        W[0, :] = 0  
        
        # GBM formula: S(t) = S(0) * exp((mu - 0.5*sigma^2)t + sigma*W(t))
        prices = self.s0 * np.exp((self.mu - 0.5 * self.sigma**2) * t_axis + self.sigma * W)
        return prices