import numpy as np

class VasicekModel:
    def __init__(self, a, b, sigma, r0):
        self.a = a      # Speed of mean reversion
        self.b = b      # Long-term mean rate
        self.sigma = sigma
        self.r0 = r0

    def simulate_paths(self, T, n_scenarios, dt=1.0):
        """Standard simulation with independent shocks."""
        n_steps = int(T / dt)
        rates = np.zeros((n_steps + 1, n_scenarios))
        rates[0, :] = self.r0
        for t in range(1, n_steps + 1):
            rates[t, :] = rates[t-1, :] + self.a * (self.b - rates[t-1, :]) * dt + \
                          self.sigma * np.sqrt(dt) * np.random.normal(0, 1, n_scenarios)
        return rates

    def simulate_with_shocks(self, T, n_scenarios, external_shocks, dt=1.0):
        """Simulation using externally provided correlated shocks."""
        n_steps = int(T / dt)
        rates = np.zeros((n_steps + 1, n_scenarios))
        rates[0, :] = self.r0
        for t in range(1, n_steps + 1):
            # external_shocks provides the random part from the Cholesky matrix
            diffusion = self.sigma * np.sqrt(dt) * external_shocks[t, :]
            rates[t, :] = rates[t-1, :] + self.a * (self.b - rates[t-1, :]) * dt + diffusion
        return rates