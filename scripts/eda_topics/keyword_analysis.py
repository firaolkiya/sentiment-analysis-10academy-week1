from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import re
import pandas as pd

# Extract unique domains from email-like publisher names
def extract_domain(publisher):
    match = re.search(r'@([a-zA-Z0-9.-]+)', publisher)
    if match:
        return match.group(1)
    return publisher

# Load the data
file_path = '../../data/raw/raw_analyst_ratings.csv/raw_analyst_ratings.csv'
df = pd.read_csv(file_path)

# Tokenize and filter out common words
stop_words = set(stopwords.words('english'))
all_words = ' '.join(df['headline']).lower()
tokens = word_tokenize(all_words)
filtered_words = [word for word in tokens if word.isalnum() and word not in stop_words]

# Count frequency of words
word_counts = Counter(filtered_words)
most_common_words = word_counts.most_common(20)

print(most_common_words)
