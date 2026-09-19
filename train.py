import pandas as pd
import numpy as np


print("Loading DataFrame from CSV file...")
df = pd.read_csv("kc_house_data.csv")
print("DataFrame loaded successfully.")

print("\n--------------------------------------------\n")
print("DataFrame head:")
print(df.head())
print("\n--------------------------------------------\n")

print("DataFrame shape:")
print(df.shape)
print("\n--------------------------------------------\n")

print("DataFrame columns:")
print(df.columns)
print("\n--------------------------------------------\n")

print("DataFrame info:")
print(df.info())
print("\n--------------------------------------------\n")

print("DataFrame describe:")
print(df.describe())
print("\n--------------------------------------------\n")
print("DataFrame null values count:")
missing = df.isnull().sum()
print(missing)
print("\n--------------------------------------------\n")

print("DataFrame null values percentage:")
missing_percentage = (missing / len(df)) * 100
print(missing_percentage)
print("\n--------------------------------------------\n")
