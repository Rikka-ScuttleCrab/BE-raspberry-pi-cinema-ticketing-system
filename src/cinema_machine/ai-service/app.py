from fastapi import FastAPI

from recommend import recommend

app = FastAPI()


@app.get("/recommend/{movie_id}")
def get_recommend(movie_id: int):

    return recommend(movie_id)