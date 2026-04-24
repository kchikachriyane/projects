# 🏥 Health Insurance Charges Analysis

> An exploratory data analysis (EDA) of health insurance charges based on demographic and regional factors.

---

## 📊 Project Overview

This project analyzes health insurance billing data to uncover patterns and trends in medical charges across different patient profiles. It explores how factors such as **age**, **sex**, **number of children**, and **region** influence insurance costs.

---

## 📁 Dataset

| Feature      | Description                                      |
|--------------|--------------------------------------------------|
| `age`        | Age of the primary beneficiary                   |
| `sex`        | Gender of the insured (male / female)            |
| `children`   | Number of dependents covered                     |
| `region`     | Residential area in the US (NE, NW, SE, SW)     |
| `charges`    | Individual medical costs billed by insurance     |

---

## 🔍 Key Insights

- **Average charge:** $13,270 across all policyholders
- **Total charges:** $17.76M cumulative across the dataset
- **Age trend:** Insurance charges increase consistently with age for all regions
- **Regional variation:** The Southeast shows notably higher charges at younger ages
- **Gender gap:** Male policyholders generate higher total charges (~$9.5M) vs females (~$8.3M)
- **Children filter:** Charges were segmented across 0–5 dependents to isolate family size effects

---

## 📈 Visualizations

### 1. Average Charges by Age & Region
- Line chart comparing 4 US regions (Northeast, Northwest, Southeast, Southwest)
- Shows charge volatility in younger age groups and a general upward trend with age

### 2. Sum of Charges by Sex
- Dot plot showing total charges by gender
- Males incur higher cumulative costs than females

### 3. Sum of Charges by Age & Sex
- Area chart overlaying male and female charge trends across age groups
- Males consistently generate higher charges, with the gap widening after age 40

---

## 🛠️ Tools & Technologies

- **Power BI** — Interactive dashboard & visualizations
- **Python / Pandas** *(if applicable)* — Data cleaning & preprocessing
- **Dataset Source:** [Kaggle – Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)

---

## 🚀 How to Use

1. Clone this repository
2. Open the `.pbix` file in Power BI Desktop (or view screenshots in `/visuals`)
3. Use the **children filter** to slice data by number of dependents
4. Explore regional and demographic trends interactively

---

## 👤 Author

**Riyane KCHIKACH**  
MSc Actuarial Science & Finance — University Hassan I, Settat  
[LinkedIn](https://www.linkedin.com/in/riyanekchikach/) 

---

## 📌 Status

![Status](https://img.shields.io/badge/status-completed-brightgreen)
![Tool](https://img.shields.io/badge/tool-Power%20BI-yellow)
![Domain](https://img.shields.io/badge/domain-Healthcare-blue)
