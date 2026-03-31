# Notebook Summary



## Markdown Cells

### Spam classifier 
- CountVectorizer builds bag-of-words features from the emails so the model sees word counts, not raw text.
- train_test_split holds out part of the data to measure performance on unseen examples.
- MultinomialNB is a fast baseline for word-count features; it learns token likelihoods per class.
- accuracy_score reports the fraction of correct predictions; with only four samples, results vary a lot.
- For better performance, expand the dataset and consider cleaning (lowercasing, stopwords) or TF-IDF.



## Code Cells

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample data: short toy corpus plus spam/ham labels
emails = ["Free money now", "Meeting at 3 PM", "Win a lottery", "Project update"]
labels = [1, 0, 1, 0]  # 1 = Spam, 0 = Not Spam

# Vectorize text: learn vocabulary and convert each email into word-count features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

# Split data into train/test so we can evaluate on held-out examples
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.30, random_state=42)

# Train a multinomial Naive Bayes classifier on the training vectors
model = MultinomialNB()
model.fit(X_train, y_train)

# Test model on unseen test vectors and compute accuracy
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
