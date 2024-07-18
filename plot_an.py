import requests
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import time
stories_df = pd.read_csv('top_stories.csv')
comments_df = pd.read_csv('top_comments.csv')

# Analyze data
average_score = stories_df['score'].mean()
average_comments = stories_df['comments_count'].mean()

# Save summary statistics
with open('summary_statistics.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['average_score', 'average_comments'])
    writer.writerow([average_score, average_comments])

# Plot analysis results
plt.figure(figsize=(10, 5))

# Plot average score of top stories
plt.subplot(1, 2, 1)
sns.histplot(stories_df['score'], kde=True)
plt.title('Distribution of Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')

# Plot average number of comments per story
plt.subplot(1, 2, 2)
sns.histplot(stories_df['comments_count'], kde=True)
plt.title('Distribution of Number of Comments')
plt.xlabel('Number of Comments')
plt.ylabel('Frequency')

plt.tight_layout()
plt.savefig('analysis_results.png')
plt.show()
