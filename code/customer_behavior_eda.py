# ===========================================
# Customer Shopping Behavior - EDA Script
# ===========================================

# Import required libraries
import pandas as pd
import numpy as np

# Load dataset
file_path = "Customer Shopping Data.csv"  # Change if needed
df = pd.read_csv(file_path)

print("\n===== Dataset Loaded Successfully =====\n")

# Display the first rows
print("📌 First 5 records:")
print(df.head(), "\n")

# Dataset shape
print("📌 Dataset Shape (Rows, Columns):", df.shape, "\n")

# Column Information
print("📌 Column Info:")
print(df.info(), "\n")

# Check missing values
print("📌 Missing Values:")
print(df.isnull().sum(), "\n")

# Numeric Summary
print("📌 Statistical Summary (Numerical Columns):")
print(df.describe(), "\n")

# Dataset overview
total_rows = df.shape[0]
missing_rating = df['Review Rating'].isnull().sum()
unique_products = df['Item Purchased'].nunique()
unique_categories = df['Category'].nunique()

print("===== Quick EDA Highlights =====")
print(f"Total Customers: {total_rows}")
print(f"Missing Review Ratings: {missing_rating}")
print(f"Unique Products: {unique_products}")
print(f"Unique Categories: {unique_categories}")

# Value counts for major categorical fields
print("\n📌 Gender Distribution:")
print(df['Gender'].value_counts(), "\n")

print("📌 Product Category Distribution:")
print(df['Category'].value_counts(), "\n")

print("📌 Payment Methods Used:")
print(df['Payment Method'].value_counts(), "\n")

print("📌 Seasonal Purchases:")
print(df['Season'].value_counts(), "\n")

# Optional: Save cleaned dataset after removing NaN Ratings
df_cleaned = df.copy()
df_cleaned['Review Rating'].fillna(df['Review Rating'].mean(), inplace=True)

df_cleaned.to_csv("Customer_Shopping_Cleaned.csv", index=False)
print("📂 Cleaned dataset saved as: Customer_Shopping_Cleaned.csv")
print("\n===== EDA Completed Successfully! 🚀 =====")
