# Car Insurance Premium Analysis — Power BI Dashboard

An interactive Power BI dashboard analyzing **1,000 synthetic car insurance policies**, identifying the key drivers of insurance premiums across driver age, accident history, vehicle age, and annual mileage.

---

## Dashboard Overview

The report consists of two pages:

### Page 1 — Risk & Mileage Analysis
- **Previous Accidents vs Premium by Driver Age** — dual-axis chart showing the correlation between accident history and premium levels across age groups
- **Annual Mileage by Car Age** — trend analysis of mileage exposure across vehicle lifecycle
- **KPIs** — Total Previous Accidents: **2,568** | Total Premium Portfolio: **$493,740**

### Page 2 — Premium Distribution
- **Premium by Driver Age** — bar chart revealing premium peaks in the 40–45 age band
- **Premium by Car Age** — scatter plot showing premium dispersion across vehicle age (0–35 years)

---

## Dataset

| Feature | Description |
|---|---|
| **Driver Age** | Age of the policyholder (16–70) |
| **Driving Experience** | Years of active driving experience |
| **Previous Accidents** | Historical accident count |
| **Annual Mileage** | Yearly distance driven (km) |
| **Car Manufacturing Year** | Vehicle age proxy |
| **Insurance Premium ($)** | Target variable — calculated via linear formula |

- **Rows:** 1,000 synthetic policies
- **Source:** Synthetic dataset inspired by real-world non-life insurance pricing factors
- **Use case:** Feature importance analysis, premium driver identification, linear regression modeling

---

## Key Findings

- **Driver age 40–45** shows the highest premium concentration, reflecting peak mileage and accumulated risk exposure
- **Previous accidents** correlate positively with premiums across all age groups, consistent with experience-based rating principles
- **Car age** shows high premium variance in the 5–10 year band, suggesting a non-linear relationship between vehicle depreciation and risk
- **Annual mileage** peaks for cars aged 5–8 years, aligning with primary usage periods

---

## Tools Used

- **Power BI Desktop** — data modeling, DAX measures, interactive visualizations
- **DAX** — custom measures for KPI calculations and aggregations

---

## Skills Demonstrated

`Non-Life Insurance Pricing` `Premium Driver Analysis` `Data Visualization` `Power BI` `DAX` `Insurance Analytics` `Risk Assessment`

---

## How to View

1. Download `insurance_premium.pbix`
2. Open with **Power BI Desktop** (free download at [powerbi.microsoft.com](https://powerbi.microsoft.com))
3. Navigate between pages using the bottom tab bar

---

## Author

**Riyane KCHIKACH**
MSc Actuarial Science & Finance — University Hassan I, Settat
[LinkedIn](https://www.linkedin.com/in/riyanekchikach/) | [Email](mailto:riyanekchikach02@gmail.com)
