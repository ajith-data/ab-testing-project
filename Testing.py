import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest

data = pd.read_csv(r"C:\Users\BLUE BOY\Downloads\AB_Test_Dataset.csv")
df = pd.DataFrame(data)
df.columns = df.columns.str.strip()
while True:
    print("\n===== EDA MENU =====")
    print("1. Top 5 Rows")
    print("2. Last 5 Rows")
    print("3. Describe")
    print("4. Info")
    print("5. Columns")
    print("6. Null Summary")
    print("7. Unique Value Check")
    print("8. User_ID")
    print("9. Group")
    print("10. Button_Color Analysis")
    print("11. Clicked")
    print("12. Device")
    print("13. Location")
    print("14. Time_Spent_Sec")
    print("15. Referral_Source")
    print("16. A/B Test Analysis ")
    print("17. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Top 5 Rows ")
        print("\n",df.head(),"\n")

    elif choice == "2":
        print("Last 5 Rows ")
        print("\n",df.tail(),"\n")

    elif choice == "3":
        print("Describe")
        print("\n",df.describe(),"\n")

    elif choice == "4":
        print("Info")
        print("\n",df.info(),"\n")

    elif choice == "5":
        print("Columns")
        print("\n",df.columns.tolist(),"\n")

    elif choice == "6":
        print("Null Summary")
        print("\n",df.isnull().sum(),"\n")

    elif choice == "7":
        print("\n",df.nunique(),"\n")

    elif choice == "8":
        print("User_ID Basic Check")
        print("Unique User_IDs:", "\n",df["User_ID"].nunique(),"\n")
        print("Duplicate User_IDs:","\n", df["User_ID"].duplicated().sum(),"\n")

    elif choice == "9":
        print("Group")
        print("\n",df["Group"].value_counts(),"\n")

    elif choice =="10":
        print("Button_color_Analysis")
        print("\n",df['Button_Color'].value_counts(),"\n")

    elif choice =="11":
        print("Clicked")
        print("\n",df["Clicked"].value_counts(normalize=True) * 100,"\n")

    elif choice =="12":
        print("Device")
        print("\n",df["Device"].value_counts(),"\n")

    elif choice =="13":
        print("Location")
        print("\n",df["Location"].value_counts(),"\n")

    elif choice =="14":
        print("Time_spent_Sec")
        print("\n",df["Time_Spent_Sec"].describe(),"\n")

    elif choice == "15":
        print("Referral_Source")
        print("\n",df["Referral_Source"].value_counts(),"\n")

    elif choice == "16":
        print("\n========== FULL A/B TEST ANALYSIS ==========\n")
       # Group aggregation
        group_data = df.groupby("Group")["Clicked"].agg(["sum", "count"])
        
        clicks_A = group_data.loc["A", "sum"]
        users_A = group_data.loc["A", "count"]
        
        clicks_B = group_data.loc["B", "sum"]
        users_B = group_data.loc["B", "count"]

        
        p1 = clicks_A / users_A
        p2 = clicks_B / users_B

        print("Conversion Rate A:", round(p1 * 100, 2), "%")
        print("Conversion Rate B:", round(p2 * 100, 2), "%\n")

        #Z-test using statsmodels
        count = np.array([clicks_A, clicks_B])
        nobs = np.array([users_A, users_B])

        z_stat, p_value = proportions_ztest(count, nobs)

        print("Z-Statistic:", round(z_stat, 4))
        print("P-Value:", round(p_value, 6), "\n")
        # Absolute & Relative Difference
        absolute_diff = p2 - p1
        uplift = (absolute_diff / p1) * 100

        print("Absolute Difference:", round(absolute_diff * 100, 2), "%")
        print("Uplift (% improvement of B over A):", round(uplift, 2), "%\n")

        # Confidence Interval (unpooled standard error)
        se_diff = np.sqrt(
            (p1 * (1 - p1) / users_A) +
            (p2 * (1 - p2) / users_B)
        )

        z_critical = 1.96
        ci_lower = absolute_diff - z_critical * se_diff
        ci_upper = absolute_diff + z_critical * se_diff

        print("95% Confidence Interval:")
        print("Lower Bound:", round(ci_lower * 100, 2), "%")
        print("Upper Bound:", round(ci_upper * 100, 2), "%\n")
    
        print("========== FINAL CONCLUSION ==========\n")

        if p_value < 0.05:
            print("Statistically Significant Result")
            print("Reject Null Hypothesis.")
    
            if p2 > p1:
                print("Recommendation: Implement Version B")
            else:
                print("Recommendation: Keep Version A.")
        else:
            print("No Statistically Significant Difference")
            print("Recommendation: Keep current version.")

        print("\n======================================\n")
        labels = ['Group A Clicks', 'Group B Clicks']
        sizes = [clicks_A, clicks_B]
        plt.figure()
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title("Click Distribution Between Group A and Group B")
        plt.show()
        plt.close()

    elif choice =="17":
        print("\n","Program exited successfully","\n")
        break
    else:
        print("\n","Please enter a valid option","\n")
