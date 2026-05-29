import pandas as pd
import joblib

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sqlalchemy import text

from database import engine


# =========================
# LOAD MOVIES
# =========================
movies_query = """
SELECT
    m.id,
    m.title,
    m.age_rating,
    GROUP_CONCAT(c.name) AS category,
    m.actors
FROM movies m
LEFT JOIN movie_category mc
ON m.id = mc.movie_id
LEFT JOIN categories c
ON mc.category_id = c.id
GROUP BY m.id
"""

movies = pd.read_sql(text(movies_query), engine)

# =========================
# LOAD INTERACTIONS
# =========================
interactions_query = """
SELECT
    selected_movie_id,
    recommended_movie_id,
    purchased
FROM user_movie_interactions
"""

interactions = pd.read_sql(
    text(interactions_query),
    engine
)

# =========================
# MERGE SELECTED
# =========================
data = interactions.merge(
    movies.add_prefix("selected_"),
    left_on="selected_movie_id",
    right_on="selected_id"
)

# =========================
# MERGE RECOMMENDED
# =========================
data = data.merge(
    movies.add_prefix("recommended_"),
    left_on="recommended_movie_id",
    right_on="recommended_id"
)

# =========================
# FEATURE ENGINEERING
# =========================
data["same_category"] = (
    data["selected_category"] ==
    data["recommended_category"]
).astype(int)

data["same_actor"] = (
    data["selected_actors"] ==
    data["recommended_actors"]
).astype(int)

data["same_age_rating"] = (
    data["selected_age_rating"] ==
    data["recommended_age_rating"]
).astype(int)

# =========================
# INPUT
# =========================
X = data[
    [
        "same_category",
        "same_actor",
        "same_age_rating"
    ]
]

# =========================
# OUTPUT
# =========================
y = data["purchased"]

# =========================
# SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# TRAIN
# =========================
model = XGBClassifier()

model.fit(X_train, y_train)

# =========================
# TEST
# =========================
predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("Accuracy:", accuracy)

# =========================
# SAVE MODEL
# =========================
joblib.dump(model, "model.pkl")

print("MODEL TRAINED SUCCESS")