
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the cleaned dataset
df = pd.read_csv("cleaned_netflix_data.csv")

# Step 2: Analyze content ratings
rating_counts = df["rating"].dropna().value_counts()

print("Top Content Ratings:")
print(rating_counts.head(10))

# Step 3: Visualize content ratings
plt.figure(figsize=(10, 6))

sns.barplot(
    x=rating_counts.head(10).values,
    y=rating_counts.head(10).index
)

plt.title("Top 10 Netflix Content Ratings")
plt.xlabel("Number of Titles")
plt.ylabel("Rating")
plt.tight_layout()

plt.savefig("content_ratings.png")
plt.show()

# Step 4: Analyze genres
genre_series = (
    df["listed_in"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)

genre_counts = genre_series.value_counts()

print("\nTop 10 Genres:")
print(genre_counts.head(10))

# Step 5: Visualize genres
plt.figure(figsize=(10, 6))

sns.barplot(
    x=genre_counts.head(10).values,
    y=genre_counts.head(10).index
)

plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()

plt.savefig("top_10_genres.png")
plt.show()

# Step 6: Compare ratings across content types
rating_comparison = pd.crosstab(
    df["rating"],
    df["type"]
)

print("\nRatings by Content Type:")
print(rating_comparison)

# Step 7: Create a comparison chart
rating_comparison.plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("Content Ratings: Movies vs TV Shows")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("rating_comparison.png")
plt.show()

# Step 8: Display conclusion
print("\nTask 5 Completed Successfully!")
print("Rating and genre analysis is complete.")