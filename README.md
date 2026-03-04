# Data-driven-retention-strategy
End-to-end data analytics project demonstrating customer segmentation, churn analysis, and strategic business insights for subscription-based services.

## Project Description
This project is an **end-to-end data analytics solution** focused on understanding customer behavior in subscription-based services. The analysis demonstrates how data can be used to:
- Perform customer segmentation  
- Identify churn patterns  
- Generate business insights for retention strategy optimization  
The project simulates real-world business analytics workflows from **data cleaning → analysis → visualization → insight generation**.

---

### Business Problem
Subscription businesses often struggle with customer retention. This project helps answer key business questions such as:
- What is the overall churn rate?
- Which customers segments are most likely to churn?  
- What behavioral patterns influence customer retention?  
- How can businesses improve customer lifetime value?
- Which demographic groups are high risk?

---
## Features
- Data cleaning and preprocessing  
- Customer segmentation analysis  
- Churn rate calculation  
- Behavioral pattern analysis  
- Business insight generation  
- Data visualization and reporting  

---

## Technologies Used
- Python 3.x  
- Pandas — Data manipulation  
- Matplotlib — Visualization  
- VS Code — Development environment

---

## Dataset Overview
The dataset contains gym member records including:
Member_ID                   
Name                        
Age                         
Gender                       
Address                      
Phone_Number                 
Membership_Type              
Join_Date                    
Last_Visit_Date              
Favorite_Exercise            
Avg_Workout_Duration_Min     
Avg_Calories_Burned         
Total_Weight_Lifted_kg       
Visits_Per_Month            
Churn 

---

### Dataset Size
- Total Rows: 150
- Total Columns: 15

---

### Missing Data Overview
The dataset contains missing values in the following columns:

| Column                     | Missing Values |
|----------------------------|---------------|
| Name                       | 23 |
| Age                        | 13 |
| Join_Date                  | 9  |
| Avg_Calories_Burned        | 11 |
| Total_Weight_Lifted_kg     | 8  |
| Visits_Per_Month           | 12 |

All other columns contain complete data.

---

## Data Cleaning
- Filled missing names with "Unknown"
- Imputed missing numerical values using median
- Converted Join_Date to datetime format
- Created Age_Group variable using binning 
##### Median imputation was used for numerical variables to reduce outlier influence.

## Key Findings
- Overall Churn Rate
- Total members: 150
- Churned (Yes): 39
- Retained (No): 111
- Churn rate: 26%
- Retention rate: 74%
  
##### Interpretation:

Out of 150 gym members, 26% have churned, meaning roughly 1 in 4 members leave the gym.
The strongest churn driver identified is low visit frequency, followed by monthly membership plans and members aged 35+.
Gender and workout duration were found to have minimal impact on churn behavior.

### Churn by Membership Type

| Membership Type | Retention % | Churn % |
|-----------------|-------------|----------|
| Monthly         | 70.7%       | 29.3%    |
| Quarterly       | 73.8%       | 26.2%    |
| Yearly          | 81.8%       | 18.2%    |

**Insight:**  
Monthly members churn the most.  
Yearly members churn the least. 
Long-term commitment reduces churn.  
Converting Monthly → Yearly could improve retention.

https://github.com/Chisom-Okoli/Data-driven-retention-strategy/blob/main/churn%20membership%20typr%20chart.png


### Churn by Gender

| Gender | Retention % | Churn % |
|--------|------------|----------|
| Female | 73.3%      | 26.7%    |
| Male   | 74.7%      | 25.3%    |

**Insight:**  
Gender is not a strong churn driver.

---

### Churn by Age Group

| Age Group | Retention % | Churn % |
|------------|-------------|----------|
| 18–25      | 82.1%       | 17.9%    |
| 25–35      | 82.8%       | 17.2%    |
| 35–45      | 71.4%       | 28.6%    |
| 45–55      | 67.6%       | 32.4%    |

**Insight:**  
Churn increases with age.  
Members aged 35+ show significantly higher churn.

---

### Behavioral Analysis

#### Average Visits Per Month

| Churn | Avg Visits |
|--------|------------|
| No     | 16.83      |
| Yes    | 6.74       |

Churned members visit ~60% less frequently.

**Low visit frequency is the strongest churn signal.**

---

#### Average Workout Duration

| Churn | Avg Duration (min) |
|--------|--------------------|
| No     | 72.1               |
| Yes    | 76.8               |

Session duration does not significantly impact churn, frequency matters more than intensity.

---

## Strong vs Weak Churn Indicators

### Strong Indicators
- Low visits per month
- Monthly membership
- Age 35+

### Weak / Non-Significant Indicators
- Gender
- Workout duration
  
---

##  Business Recommendations
###  Early Warning System

Flag members with:
- Visits less than 8 times per month
- Monthly membership
- Age greater than 35

---

### Engagement Strategy

- Automated reminders for inactive members
- Personalized programs for 35+ segment
- Incentives to convert Monthly → Yearly plans

---

###  Recommended KPIs

- Churn Rate %
- Average Visits Per Month
- Membership Upgrade Rate
- 30-Day Inactivity Rate

---

##  Final Conclusion

Visit frequency is the clearest behavioral separator between churned and retained members.

Retention efforts should prioritize increasing member engagement and promoting long-term membership plans.

---












