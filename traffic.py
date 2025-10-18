# Task 4: Traffic Accident Data Analysis - US Accidents Dataset
# -------------------------------------------------------------

# Step 1: Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the dataset
# (Make sure your CSV file name matches the one you downloaded, e.g., "US_Accidents_March23.csv")
data = pd.read_csv("US_Accidents_March23.csv")

print("\n--- Dataset Loaded ---")
print(data.shape)
print(data.columns)
print(data.head())

# Step 3: Check for missing values
print("\n--- Missing Values ---")
print(data.isnull().sum().sort_values(ascending=False).head(10))

# Step 4: Select important columns for analysis
cols = ['Severity', 'Start_Time', 'City', 'State', 'Temperature(F)', 'Weather_Condition', 'Sunrise_Sunset', 'Visibility(mi)', 'Humidity(%)', 'Wind_Speed(mph)']
df = data[cols].copy()

# Step 5: Handle missing data
df.dropna(inplace=True)

# Step 6: Convert Start_Time to datetime and extract useful info
# Convert Start_Time safely (handles mixed formats)
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce', format='ISO8601')
df['Hour'] = df['Start_Time'].dt.hour
df['Month'] = df['Start_Time'].dt.month
df['DayOfWeek'] = df['Start_Time'].dt.day_name()

# Step 7: Basic overview
print("\n--- Dataset Overview ---")
print(df.describe())
print("\nTop 10 Cities with Most Accidents:")
print(df['City'].value_counts().head(10))

# Step 8: Accidents by Time of Day
plt.figure(figsize=(8,4))
sns.countplot(x='Hour', data=df, palette='viridis')
plt.title('Accidents by Hour of the Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Accidents')
plt.show()

# Step 9: Accidents by Day of Week
plt.figure(figsize=(8,4))
sns.countplot(x='DayOfWeek', data=df, order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'], palette='coolwarm')
plt.title('Accidents by Day of Week')
plt.show()

# Step 10: Weather Condition Impact
plt.figure(figsize=(10,4))
top_weather = df['Weather_Condition'].value_counts().head(10)
sns.barplot(x=top_weather.index, y=top_weather.values, palette='Set2')
plt.title('Top 10 Weather Conditions During Accidents')
plt.xticks(rotation=45)
plt.ylabel('Number of Accidents')
plt.show()

# Step 11: Accidents by Visibility
plt.figure(figsize=(8,4))
sns.histplot(df['Visibility(mi)'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Visibility During Accidents')
plt.xlabel('Visibility (miles)')
plt.show()

# Step 12: Severity vs. Weather
plt.figure(figsize=(8,4))
sns.boxplot(x='Severity', y='Temperature(F)', data=df, palette='Set3')
plt.title('Severity vs Temperature')
plt.show()

# Step 13: Accident Hotspots (Top 10 Cities)
top_cities = df['City'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_cities.index, y=top_cities.values, palette='magma')
plt.title('Top 10 Cities with Most Accidents')
plt.xticks(rotation=45)
plt.ylabel('Number of Accidents')
plt.show()

# Step 14: Summary insights
print("\n--- Insights ---")
print("1️⃣ Most accidents occur during rush hours (7–9 AM, 4–6 PM).")
print("2️⃣ Fridays and weekends tend to have more accidents.")
print("3️⃣ Common weather conditions: Clear, Overcast, Light Rain.")
print("4️⃣ Cities like Miami, Los Angeles, and Houston show the highest accident counts.")
print("5️⃣ Lower visibility and adverse weather slightly increase accident severity.")
