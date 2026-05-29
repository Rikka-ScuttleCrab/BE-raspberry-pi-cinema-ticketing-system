import requests


AI_BASE_URL = "http://localhost:9000"


def get_recommendations(movie_id: int):

    try:
        response = requests.get(
            f"{AI_BASE_URL}/recommend/{movie_id}"
        )

        if response.status_code != 200:
            return []

        return response.json()

    except Exception as e:
        print("AI SERVICE ERROR:", e)
        return []
    