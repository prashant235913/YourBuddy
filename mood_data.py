import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
nltk.download('stopwords')
nltk.download('wordnet')


mood_data = [
    {
        "Mood": "Sadness",
        "Likes": [
            "Warm beverages like tea or coffee",
            "Comfort foods like soup or chocolate",
            "Cozy blankets",
            "Calming scents",
            "Muted and soothing colors (e.g., blues, soft purples)",
            "Watching a sad movie",
            "Reflecting on past memories"
        ],
        "Dislikes": [
            "Loud environments",
            "Bright lights",
            "Crowded places",
            "Being alone in a noisy place",
            "Negative news or stories"
        ]
    },
    {
        "Mood": "Happiness",
        "Likes": [
            "Bright and vibrant colors",
            "Favorite foods and desserts",
            "Energetic and upbeat music",
            "Engaging in outdoor activities or hobbies",
            "Spending time with loved ones",
            "Celebrating achievements",
            "Engaging in creative activities",
            "Random acts of kindness"
        ],
        "Dislikes": [
            "Negative or sad conversations",
            "Dull or monotonous tasks",
            "Rainy and gloomy weather",
            "Traffic jams",
            "Feeling disconnected from loved ones"
        ]
    },
    {
        "Mood": "Stress",
        "Likes": [
            "Relaxing activities like meditation or deep breathing",
            "Calming scents like lavender",
            "Quiet and peaceful environments",
            "Engaging in light exercise or yoga",
            "Listening to calming music",
            "Engaging in mindfulness practices",
            "Time management techniques"
        ],
        "Dislikes": [
            "Chaotic or noisy environments",
            "Demanding tasks",
            "Meeting tight deadlines",
            "Public speaking",
            "Conflict and arguments"
        ]
    },
    {
        "Mood": "Excitement",
        "Likes": [
            "High-energy activities like dancing or sports",
            "Vibrant and bold colors",
            "Fast-paced and energetic music",
            "Trying out new experiences or challenges",
            "Social events and parties",
            "Planning for adventures"
        ],
        "Dislikes": [
            "Boredom",
            "Routine tasks",
            "Long waiting times",
            "Missing out on fun activities"
        ]
    },
    {
        "Mood": "Calmness",
        "Likes": [
            "Tranquil surroundings like nature or a quiet room",
            "Instrumental or ambient music",
            "Mindfulness or relaxation exercises",
            "Reading a book or journaling",
            "Practicing deep breathing",
            "Taking peaceful walks"
        ],
        "Dislikes": [
            "Stressful situations",
            "Loud noises",
            "Constant interruptions",
            "Feeling rushed"
        ]
    },
    {
        "Mood": "Frustration",
        "Likes": [
            "Engaging in problem-solving activities",
            "Physical activity like jogging or hitting a punching bag",
            "Venting frustrations to a friend or writing them down",
            "Listening to energetic music",
            "Creating art as an outlet"
        ],
        "Dislikes": [
            "Obstacles",
            "Setbacks",
            "Feeling stuck",
            "Dealing with inefficiencies"
        ]
    },
    {
        "Mood": "Apathy",
        "Likes": [
            "Simple and routine activities",
            "Minimalistic environments",
            "Solitary activities like walking or sitting in a peaceful spot",
            "Observing surroundings",
            "Minimalistic art and design"
        ],
        "Dislikes": [
            "Demands",
            "Social obligations",
            "Overwhelming choices",
            "Overstimulating environments"
        ]
    },
    {
        "Mood": "Nostalgia",
        "Likes": [
            "Engaging in activities or watching movies from the past",
            "Listening to nostalgic music",
            "Revisiting old photos or mementos",
            "Sharing stories from the past",
            "Looking through old diaries"
        ],
        "Dislikes": [
            "Rapid changes",
            "Unfamiliarity",
            "Losing cherished memories"
        ]
    },
    {
        "Mood": "Fear",
        "Likes": [
            "Being in familiar and safe environments",
            "Having a support system nearby",
            "Engaging in calming activities like deep breathing or meditation",
            "Soft and dim lighting",
            "Watching lighthearted comedies"
        ],
        "Dislikes": [
            "Unknown or unpredictable situations",
            "Feeling isolated",
            "Loud or sudden noises",
            "Confrontational or aggressive situations",
            "Watching horror movies"
        ]
    }
]


def tokenize_and_lowercase(text):
    tokens = word_tokenize(text)
    lowercase_tokens = [token.lower() for token in tokens]
    return lowercase_tokens

def remove_punctuation(tokens):
    tokens_without_punctuation = [token for token in tokens if token not in string.punctuation]
    return tokens_without_punctuation

def remove_stopwords(tokens):
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens

def lemmatize_tokens(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens

preprocessed_data = []

for mood_entry in mood_data:
    mood = mood_entry["Mood"]
    likes = mood_entry["Likes"]
    dislikes = mood_entry["Dislikes"]

    preprocessed_likes = []
    preprocessed_dislikes = []

    for like in likes:
        tokens = tokenize_and_lowercase(like)
        tokens = remove_punctuation(tokens)
        tokens = remove_stopwords(tokens)
        tokens = lemmatize_tokens(tokens)
        preprocessed_likes.append(" ".join(tokens))

    for dislike in dislikes:
        tokens = tokenize_and_lowercase(dislike)
        tokens = remove_punctuation(tokens)
        tokens = remove_stopwords(tokens)
        tokens = lemmatize_tokens(tokens)
        preprocessed_dislikes.append(" ".join(tokens))

    preprocessed_entry = {
        "Mood": mood,
        "Likes": preprocessed_likes,
        "Dislikes": preprocessed_dislikes
    }

    preprocessed_data.append(preprocessed_entry)
print(preprocessed_data)
