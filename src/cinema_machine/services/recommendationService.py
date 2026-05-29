from sqlalchemy.orm import joinedload
from models.movies.movie import Movie

def recommend_movies_service(db, movie_id):

    selected_movie = (
        db.query(Movie)
        .options(joinedload(Movie.categories))
        .filter(Movie.id == movie_id)
        .first()
    )

    if not selected_movie:
        return {
            "error": "Movie not found"
        }

    selected_categories = {
        c.name
        for c in selected_movie.categories
    }

    selected_actors = set()

    if selected_movie.actors:
        selected_actors = {
            a.strip().lower()
            for a in selected_movie.actors.split(",")
        }

    movies = (
        db.query(Movie)
        .options(joinedload(Movie.categories))
        .filter(Movie.id != movie_id)
        .all()
    )

    recommendations = []

    for movie in movies:

        score = 0

        # CATEGORY SCORE
        movie_categories = {
            c.name
            for c in movie.categories
        }

        common_categories = (
            selected_categories &
            movie_categories
        )

        score += len(common_categories) * 5

        # ACTOR SCORE
        movie_actors = set()

        if movie.actors:
            movie_actors = {
                a.strip().lower()
                for a in movie.actors.split(",")
            }

        common_actors = (
            selected_actors &
            movie_actors
        )

        score += len(common_actors) * 3

        recommendations.append({
            "movie_id": movie.id,
            "title": movie.title,
            "score": score
        })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations[:10]