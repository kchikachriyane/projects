import matplotlib.pyplot as plt
import numpy as np

def plot_stress_comparison(surplus, shocked_surplus):
    """
    Explicitly creates Figure 4 to show the impact of the +200bps shock.
    """
    # This names the window specifically so it won't be skipped
    fig = plt.figure("Figure 4: Stress Test Comparison", figsize=(10, 6))
    ax = fig.add_subplot(111)
    
    # Data for terminal year (Year 30)
    base_final = surplus[-1, :]
    shocked_final = shocked_surplus[-1, :]
    
    # Plotting
    ax.hist(base_final, bins=50, alpha=0.5, label='Base Case (3%)', color='skyblue', edgecolor='black')
    ax.hist(shocked_final, bins=50, alpha=0.5, label='Stressed Case (+200bps)', color='salmon', edgecolor='black')
    
    # Lines for means
    ax.axvline(np.mean(base_final), color='blue', linestyle='--', linewidth=2, 
               label=f"Mean Base: {np.mean(base_final):.1f}")
    ax.axvline(np.mean(shocked_final), color='red', linestyle='--', linewidth=2, 
               label=f"Mean Stressed: {np.mean(shocked_final):.1f}")
    
    ax.set_title("Economic Capital Impact: Base vs. +200bps Interest Rate Shock", fontsize=12)
    ax.set_xlabel("Surplus Value (Assets - Liabilities)")
    ax.set_ylabel("Frequency")
    ax.legend(loc='upper right')
    ax.grid(axis='y', alpha=0.3)
    
    print("📊 Figure 4 rendered successfully.")