
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the cleaned dataset
df = pd.read_csv("cleaned_netflix_data.csv")

# Step 2: Remove rows where country information is missing
df = df.dropna(subset=["country"])

# Step 3: Split countries when multiple countries are listed
df["country"] = df["country"].str.split(",")

# Step 4: Create a separate row for each country
df = df.explode("country")

# Step 5: Remove extra spaces
df["country"] = df["country"].str.strip()

# Step 6: Count content by country
country_counts = df["country"].value_counts()

print("Top 10 Countries by Netflix Content:")
print(country_counts.head(10))

# Step 7: Plot the top 10 countries
top_countries = country_counts.head(10).sort_values()

plt.figure(figsize=(10, 6))

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)

plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig("top_10_countries.png")
plt.show()

# Step 8: Display conclusion
print("\nConclusion:")
print(
    f"{country_counts.index[0]} has the highest number "
    f"of Netflix titles in this analysis."
)

print("\nTask 3 Completed Successfully!")
