import pandas as pd
import numpy as np
import os

def export_simulation_results(surplus, funding_ratio, folder_path="data/"):
    """
    Exports summary statistics from the simulation for Power BI reporting.
    """
    # Create the data folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    years = np.arange(surplus.shape[0])
    
    # Aggregate 5,000 scenarios into a summary table
    export_df = pd.DataFrame({
        "Year": years,
        "Mean_Surplus": np.mean(surplus, axis=1),
        "P5_Surplus": np.percentile(surplus, 5, axis=1),   # 5th Percentile (Risk)
        "P95_Surplus": np.percentile(surplus, 95, axis=1), # 95th Percentile (Upside)
        "Mean_Funding_Ratio": np.mean(funding_ratio, axis=1),
        "Insolvency_Prob": np.mean(surplus < 0, axis=1)
    })
    
    file_path = os.path.join(folder_path, "alm_dashboard_data.csv")
    export_df.to_csv(file_path, index=False)
    print(f"✅ Step 8 Complete: Results exported to {file_path}")