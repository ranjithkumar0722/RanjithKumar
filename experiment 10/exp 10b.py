import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Experiment_10\sales_data.csv')
df = df.drop_duplicates()
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
df = df.dropna()

df = df.sort_values('Date')

# --- 1. Line Chart (Matplotlib) ---
plt.figure(figsize=(10, 4))
plt.plot(df['Date'], df['Sales'], marker='o', color='blue')
plt.title('Daily Sales Trend (Line Chart)')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.show()

# --- 2. Bar Chart (Seaborn) ---
plt.figure(figsize=(8, 4))
sns.barplot(x='Product_Category', y='Sales', data=df)
plt.title('Sales by Product Category (Bar Chart)')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.show()

# --- 3. Histogram (Matplotlib) ---
plt.figure(figsize=(8, 4))
plt.hist(df['Sales'], bins=10, color='green', edgecolor='black')
plt.title('Distribution of Sales (Histogram)')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency (Number of Orders)')
plt.show()