# ALM Stochastic Simulator

A full **Asset-Liability Management (ALM) simulation engine** built in Python, implementing an Economic Scenario Generator (ESG) and Solvency II-aligned risk metrics for non-life insurance portfolios.

---

## What It Does

This simulator models the stochastic evolution of assets and liabilities over a 30-year horizon across **5,000 Monte Carlo scenarios**, enabling actuarial risk assessment, surplus analysis, and stress testing under different market conditions.

---

## Key Features

| Component | Description |
|---|---|
| **Vasicek Interest Rate Model** | Stochastic simulation of interest rate paths with mean reversion |
| **Equity Model** | GBM-based equity simulation with correlated shocks |
| **Cholesky Correlation** | Correlated rate/equity shocks via Cholesky decomposition |
| **Bond & Equity Valuation** | Portfolio valuation with 80/20 bond-equity split |
| **Best Estimate Liabilities (BEL)** | Liability valuation under stochastic discount rates |
| **ALM Engine** | Surplus projection and funding ratio computation |
| **Solvency Metrics** | 99.5% VaR aligned with Solvency II SCR methodology |
| **Stress Testing** | Interest rate shock analysis (+200bps scenario) |
| **BI Export** | CSV export of results for Power BI dashboards |

---

## Methodology

### 1. Economic Scenario Generation (ESG)
Interest rates are modelled using the **Vasicek model**:

```
dr(t) = a(b - r(t))dt + σ dW(t)
```

Parameters: `a = 0.15`, `b = 0.04`, `σ = 0.01`, `r₀ = 0.03`

Equity returns follow **Geometric Brownian Motion (GBM)**:

```
dS(t) = μS(t)dt + σS(t)dW(t)
```

Parameters: `μ = 0.07`, `σ = 0.15`

Rate and equity shocks are **correlated** (ρ = -0.3) using Cholesky decomposition, reflecting the empirical negative relationship between interest rates and equity returns.

### 2. Asset & Liability Valuation
- **Bonds** are priced using simulated discount rate paths
- **Equities** projected via GBM with correlated shocks
- **BEL** (Best Estimate Liabilities) discounted under stochastic rates
- Portfolio: 80% bonds / 20% equities

### 3. ALM Engine
For each of the 5,000 scenarios:
```
Surplus(t) = Asset Value(t) - Liability Value(t)
Funding Ratio(t) = Asset Value(t) / Liability Value(t)
```

### 4. Risk Metrics (Solvency II aligned)
- **99.5% VaR** on terminal surplus distribution (Year 30)
- Stress test: +200bps parallel interest rate shock
- Comparison of base vs. stressed surplus distributions

---

## Project Structure

```
ALM-Stochastic-Simulator/
│
├── main.py                  # Main simulation pipeline
├── models/
│   ├── vasicek.py           # Vasicek interest rate model
│   ├── equity.py            # GBM equity model
│   └── liabilities.py       # BEL calculation
├── simulation/
│   ├── assets.py            # Bond & portfolio valuation
│   └── alm_engine.py        # Surplus & funding ratio engine
├── analysis/
│   ├── solvency.py          # VaR & risk metrics
│   ├── stress_tests.py      # Interest rate shock scenarios
│   └── export_results.py    # CSV export for BI tools
├── visuals/
│   └── plots.py             # Matplotlib visualizations
└── data/                    # Input data
```

---

## Outputs

The simulator produces four figures and one CSV export:

- **Figure 1** — Vasicek stochastic interest rate paths (15 sample scenarios)
- **Figure 2** — Stochastic surplus projections over 30 years
- **Figure 3** — Terminal surplus distribution (Year 30) with 99.5% VaR
- **Figure 4** — Stress test comparison: base vs. +200bps rate shock
- **CSV export** — Full simulation results for Power BI reporting

---

## How to Run

```bash
# Clone the repository
git clone https://github.com/kchikachriyane/ALM-Stochastic-Simulator.git
cd ALM-Stochastic-Simulator

# Install dependencies
pip install numpy matplotlib

# Run the simulation
python main.py
```

---

## Skills Demonstrated

`Actuarial Modeling` `Stochastic Simulation` `Monte Carlo Methods` `Vasicek Model` `Solvency II` `Asset-Liability Management` `Risk Metrics` `VaR Analysis` `Python` `NumPy` `Matplotlib` `Power BI`

---

## Author

**Riyane KCHIKACH**  
MSc Actuarial Science & Finance — University Hassan I, Settat  
[LinkedIn](https://www.linkedin.com/in/riyanekchikach/) | [Email](mailto:riyanekchikach02@gmail.com)
