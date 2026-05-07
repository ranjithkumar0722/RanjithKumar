import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'Experiment_10\sales_data.csv')

print("Initial Data Exploration")
print("Dataset Shape:", df.shape)
print(df.head())
print(df.info())
print("Missing Values Before Cleaning:\n", df.isnull().sum())
print(df.describe())

df.columns = df.columns.str.strip()

df = df.drop_duplicates()

df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

df = df.ffill()

df = df.dropna()

df = df.reset_index(drop=True)

print("\n--- Data Exploration After Cleaning ---")
print("Missing Values After Cleaning:\n", df.isnull().sum())
print("Final Dataset Shape:", df.shape)
print(df.info())