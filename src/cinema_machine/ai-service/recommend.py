import pandas as pd
import joblib

from sqlalchemy import text

from database import engine

model = joblib.load("model.pkl")


def recommend(movie_id):

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

    movies = pd.read_sql(
        text(movies_query),
        engine
    )

    selected_movie = movies[
        movies["id"] == movie_id
    ].iloc[0]

    recommendations = []

    for _, candidate in movies.iterrows():

        if candidate["id"] == movie_id:
            continue

        same_category = int(
            selected_movie["category"] ==
            candidate["category"]
        )

        same_actor = int(
            selected_movie["actors"] ==
            candidate["actors"]
        )

        same_age_rating = int(
            selected_movie["age_rating"] ==
            candidate["age_rating"]
        )

        features = [[
            same_category,
            same_actor,
            same_age_rating
        ]]

        score = model.predict_proba(features)[0][1]

        recommendations.append({
            "movie_id": int(candidate["id"]),
            "title": candidate["title"],
            "score": float(score)
        })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations[:5]