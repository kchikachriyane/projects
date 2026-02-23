import numpy as np
import matplotlib.pyplot as plt
from models.vasicek import VasicekModel
from models.equity import EquityModel
from simulation.assets import price_bond_portfolio, total_asset_projection
from models.liabilities import calculate_bel
from simulation.alm_engine import ALMEngine
from analysis.solvency import calculate_risk_metrics
from analysis.stress_tests import run_interest_rate_shock
from visuals.plots import plot_stress_comparison
from analysis.export_results import export_simulation_results

# --- [STEP 0] HELPER FUNCTIONS ---
def generate_correlated_shocks(n_scenarios, n_years, correlation_matrix):
    L = np.linalg.cholesky(correlation_matrix)
    z_independent = np.random.standard_normal((2, n_years + 1, n_scenarios))
    z_correlated = np.einsum('ij,j...->i...', L, z_independent)
    return z_correlated[0], z_correlated[1]

def update_visual_status(step_name, step_num):
    plt.figure("Simulation Status", figsize=(6, 2))
    plt.clf()
    plt.barh(['Progress'], [step_num], color='deepskyblue')
    plt.xlim(0, 8)
    plt.title(f"Step {step_num}: {step_name}")
    plt.pause(0.01)

# --- START ---
plt.ion()

# [STEP 1] ESG
update_visual_status("ESG Generation", 1)
rate_shocks, equity_shocks = generate_correlated_shocks(5000, 30, np.array([[1.0, -0.3], [-0.3, 1.0]]))
vasicek = VasicekModel(a=0.15, b=0.04, sigma=0.01, r0=0.03)
rates = vasicek.simulate_with_shocks(30, 5000, rate_shocks)

plt.figure("Figure 1: Vasicek Paths", figsize=(10, 6))
plt.plot(rates[:, :15])
plt.title("Vasicek Model — Stochastic Interest Rate Paths")

# [STEP 2 & 3] Assets & Liabilities
update_visual_status("Valuation", 2)
equity_engine = EquityModel(mu=0.07, sigma=0.15, s0=1000)
stock_paths = equity_engine.simulate_with_shocks(30, 5000, equity_shocks)
bond_values = price_bond_portfolio(rates)
asset_values = total_asset_projection(bond_values, stock_paths, weight_bond=0.8)
liability_values = calculate_bel(rates)

# [STEP 4] ALM Engine
update_visual_status("Projections", 4)
engine = ALMEngine(asset_values, liability_values)
surplus, funding_ratio = engine.compute_projections()

plt.figure("Figure 2: Surplus Projections", figsize=(10, 6))
plt.plot(surplus[:, :15])
plt.axhline(0, color='black', lw=1)
plt.title("Stochastic Surplus Projection")

# --- STEP 5: Risk Analysis ---
update_visual_status("Calculating Solvency Metrics", 5)
metrics = calculate_risk_metrics(surplus)

# FIGURE 3: Terminal Distribution (Now with Title)
plt.figure("Figure 3: Year 30 Distribution", figsize=(10, 6))
plt.hist(surplus[-1, :], bins=50, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(metrics['VaR_99.5'], color='red', linestyle='--', label='99.5% VaR')

# Add this line specifically
plt.title("Distribution of Terminal Surplus (Year 30)", fontsize=12, fontweight='bold')

plt.xlabel("Surplus Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(axis='y', alpha=0.3)

# [STEP 6 & 7] Stress Test & Figure 4
update_visual_status("Stress Testing", 7)
shocked_surplus = run_interest_rate_shock(rates, price_bond_portfolio, calculate_bel, 0.02)
# This will now correctly open "Figure 4"
plot_stress_comparison(surplus, shocked_surplus)

# [STEP 8] BI Export
update_visual_status("Exporting CSV", 8)
export_simulation_results(surplus, funding_ratio)

plt.ioff()
print("🏁 All 8 Steps Complete. Figure 4 should be visible now.")
plt.show()