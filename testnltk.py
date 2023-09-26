import nltk

nltk.download('punkt')  # Download NLTK resources

sentence = "This is a test sentence."

# NLTK
words = nltk.word_tokenize(sentence)
print("NLTK Tokenization:", words)
