
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the cleaned dataset
df = pd.read_csv("cleaned_netflix_data.csv")

# Step 2: Convert release_year to numeric
df["release_year"] = pd.to_numeric(
    df["release_year"],
    errors="coerce"
)

# Step 3: Remove rows with missing release years
df = df.dropna(subset=["release_year"])

# Step 4: Count titles released each year
yearly_counts = (
    df["release_year"]
    .astype(int)
    .value_counts()
    .sort_index()
)

print("Netflix Content by Release Year:")
print(yearly_counts.tail(15))

# Step 5: Select the latest 30 release years
recent_years = yearly_counts.tail(30)

# Step 6: Create a line chart
plt.figure(figsize=(12, 6))

sns.lineplot(
    x=recent_years.index,
    y=recent_years.values,
    marker="o"
)

plt.title("Netflix Content Trends by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("release_year_trend.png")
plt.show()

# Step 7: Identify the year with the most titles
peak_year = yearly_counts.idxmax()
peak_count = yearly_counts.max()

print("\nYear with the Highest Number of Titles:")
print("Year:", peak_year)
print("Number of Titles:", peak_count)

print("\nTask 4 Completed Successfully!")
