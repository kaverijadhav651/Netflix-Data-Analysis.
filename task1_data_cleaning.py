
import pandas as pd

# Step 1: Load the Netflix dataset
df = pd.read_csv("netflix_data.csv")

print("Original Dataset Shape:", df.shape)

# Step 2: Display first five records
print("\nFirst Five Records:")
print(df.head())

# Step 3: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Check duplicate records
print("\nDuplicate Records:", df.duplicated().sum())

# Step 5: Remove duplicate records
df = df.drop_duplicates()

# Step 6: Remove extra spaces from text columns
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

# Step 7: Convert date_added into datetime format
df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

# Step 8: Display cleaned dataset information
print("\nCleaned Dataset Shape:", df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Step 9: Export cleaned dataset
df.to_csv("cleaned_netflix_data.csv", index=False)

print("\nTask 1 Completed Successfully!")
print("Cleaned dataset saved successfully.")

