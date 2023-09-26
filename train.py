import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Import the preprocessed data from mood_data.py
from mood_data import preprocessed_data

# Step 2: Combine Likes and Dislikes
X = []  # List to hold combined Likes and Dislikes

# Iterate through the list of mood dictionaries
for mood_dict in preprocessed_data:
    likes = mood_dict['Likes']
    dislikes = mood_dict['Dislikes']
    combined_likes_dislikes = likes + dislikes
    X.append(' '.join(combined_likes_dislikes))  # Join tokens into a single string

# Step 3: Create labels
y = [mood_dict['Mood'] for mood_dict in preprocessed_data]

# Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Feature Extraction using CountVectorizer
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Step 6: Build and Train the Classifier
classifier = MultinomialNB()
classifier.fit(X_train_vectorized, y_train)

# Step 7: Predictions and Evaluation
y_pred = classifier.predict(X_test_vectorized)
# print(classification_report(y_test, y_pred))
print(classification_report(y_test, y_pred, zero_division=1))
