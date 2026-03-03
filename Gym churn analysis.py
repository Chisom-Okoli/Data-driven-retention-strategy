import matplotlib.pyplot as plt
import pandas as pd
pd.read_csv
df = pd.read_csv(r'C:\Users\DELL\Downloads\gym_members_dataset.csv')
print(df.head())
print(df.info())
print(df.isnull().sum())
df['Name'] = df['Name'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Avg_Calories_Burned'] = df['Avg_Calories_Burned'].fillna(df['Avg_Calories_Burned'].median())

df['Total_Weight_Lifted_kg'] = df['Total_Weight_Lifted_kg'].fillna(df['Total_Weight_Lifted_kg'].median())

df['Visits_Per_Month'] = df['Visits_Per_Month'].fillna(df['Visits_Per_Month'].median())
df['Join_Date'] = pd.to_datetime(df['Join_Date'])
print(df.isnull().sum())

# Overall churn rate

print (df['Churn'].value_counts())
churn_rate =df['Churn'].value_counts(normalize=True) * 100
print(churn_rate)

# Churn by Membership Type: Segmentation 1

print(pd.crosstab(df['Membership_Type'], df['Churn']))
print(pd.crosstab(df['Membership_Type'], df['Churn'], normalize='index') * 100)

# Churn by Gender
print(pd.crosstab(df['Gender'], df['Churn'], normalize='index') * 100)

# Churn by Age Group
df['Age_Group'] = pd.cut(df['Age'], bins=[18,25,35,45,55,70])
print(pd.crosstab(df['Age_Group'], df['Churn'], normalize='index') * 100)

# Validate sample size
print(pd.crosstab(df['Age_Group'], df['Churn']))
print(df['Churn'].value_counts(normalize=True) * 100)

#Visits per hour by churn
print(df.groupby('Churn')['Visits_Per_Month'].mean())

#Average workout duration
print(df.groupby('Churn')['Avg_Workout_Duration_Min'].mean())

#Membership type distribution in 45-55
group_45_55 = df[df['Age_Group'] == df['Age_Group'].cat.categories[3]]
print(pd.crosstab(group_45_55['Membership_Type'], group_45_55['Churn']))
print(df['Age_Group'].value_counts())
print(df.groupby('Churn')['Visits_Per_Month'].mean())

#Churn by membership type
df['Membership_Type'].value_counts().plot(kind='bar')

plt.title('Membership Type Distribution')
plt.xlabel('Membership Type')
plt.ylabel('Number of Members')

plt.show()

#Churn rate ny Age Group
pd.crosstab(df['Age_Group'], df['Churn']).plot(kind='bar')

plt.title('Churn by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count')

plt.show()

# visits Per Month vs Churn
df.boxplot(column='Visits_Per_Month', by='Churn')

plt.title('Visits Per Month vs Churn')
plt.xlabel('Churn')
plt.ylabel('Visits Per Month')

plt.show()



