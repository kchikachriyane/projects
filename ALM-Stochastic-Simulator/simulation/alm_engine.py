import numpy as np

class ALMEngine:
    def __init__(self, asset_paths, liability_paths):
        """
        :param asset_paths: Array of (Time, Scenarios)
        :param liability_paths: Array of (Time, Scenarios)
        """
        self.assets = asset_paths
        self.liabilities = liability_paths

    def compute_projections(self):
        # Equity = Assets - Liabilities
        self.surplus = self.assets - self.liabilities
        # Funding Ratio = Assets / Liabilities
        self.funding_ratio = self.assets / self.liabilities
        return self.surplus, self.funding_ratio