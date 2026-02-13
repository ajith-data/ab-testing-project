🚀 End-to-End A/B Testing Analysis using Python & Power BI

📌 Project Overview

This project performs a complete A/B Testing analysis to determine which webpage version (Button Color A vs B) performs better in terms of click-through rate (CTR).

The analysis includes:

*Data validation

*Exploratory Data Analysis (EDA)

*Statistical hypothesis testing

*Business dashboard visualization

🎯 Objective

To evaluate whether changing the button color impacts user click behavior and provide a statistically validated business recommendation.

🧹 Step 1: Data Validation & EDA (Python CLI Menu)

Built a structured Command-Line Interface (CLI) EDA system to ensure data quality before analysis.

✔ Data Checks Performed:

*Null value validation

*Duplicate user detection

*Unique value verification

*Click distribution analysis

*Device, location & referral segmentation

*Time spent behavior analysis

*This ensured the dataset was clean and reliable before hypothesis testing.

📊 Step 2: Statistical A/B Testing (Python)

Applied a Two-Proportion Z-Test using statsmodels.

🔍 Calculations:

*Conversion Rate (Group A vs Group B)

*Z-statistic

*P-value

*Absolute Difference

*Uplift %

*95% Confidence Interval

📌 Final Result:

*Group B (Green Button) achieved a significantly higher conversion rate.

*P-value < 0.05 → Statistically Significant

✅ Business Recommendation: Implement Version B

📈 Step 3: Interactive Dashboard (Power BI)

Designed an interactive Power BI dashboard to translate statistical insights into business decisions.

Dashboard Features:

*Conversion Rate Comparison

*Total Users & Total Clicks

*CTR by Device

*CTR by Location

*Uplift %

*Statistical Significance Indicators

*Dynamic Slicers (Device, Location, Referral Source)

🛠 Tools & Technologies

*Python

*Pandas

*NumPy

*Statsmodels

*Matplotlib

*Power BI

*Hypothesis Testing

*Statistical Analysis

## Key Insight

This project demonstrates how statistical validation combined with interactive visualization supports data-driven decision making in real-world business scenarios.
