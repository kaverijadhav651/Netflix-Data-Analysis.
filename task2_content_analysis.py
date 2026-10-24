
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load cleaned dataset
df = pd.read_csv("cleaned_netflix_data.csv")

# Step 2: Count Movies and TV Shows
content_counts = df["type"].value_counts()

print("Netflix Content Analysis")
print("------------------------")
print(content_counts)

# Step 3: Calculate percentages
percentages = df["type"].value_counts(normalize=True) * 100

print("\nContent Percentages:")
print(percentages.round(2))

# Step 4: Create a bar chart
plt.figure(figsize=(8, 5))
sns.barplot(x=content_counts.index, y=content_counts.values)

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("content_type_bar_chart.png")
plt.show()

# Step 5: Create a pie chart
plt.figure(figsize=(7, 7))

plt.pie(
    content_counts.values,
    labels=content_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Netflix Content Distribution")
plt.tight_layout()
plt.savefig("content_type_pie_chart.png")
plt.show()

# Step 6: Display conclusion
print("\nConclusion:")

print(
    f"Movies account for "
    f"{percentages.get('Movie', 0):.2f}% of the content."
)

print(
    f"TV Shows account for "
    f"{percentages.get('TV Show', 0):.2f}% of the content."
)

print("\nTask 2 Completed Successfully!")
