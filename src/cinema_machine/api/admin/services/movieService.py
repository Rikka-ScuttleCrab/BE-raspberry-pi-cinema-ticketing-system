from datetime import date
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import OperationalError
from models.movies.movie import Movie
from models.movies.poster import Poster
from models.movies.trailer import Trailer
from models.movies.category import Category


def get_all_movies_service(db: Session, page: int = 1, page_size: int = 30):

    today = date.today()
    offset = (page - 1) * page_size

    total = db.query(Movie).count()
    
    movies = (
        db.query(Movie)
        .options(
            joinedload(Movie.posters),
            joinedload(Movie.trailers),
            joinedload(Movie.categories),
        )
        .order_by(Movie.id.desc())
        .offset(offset)
        .limit(page_size)
        .all()
    )

    result = []

    for m in movies:

        if m.release_date > today:
            status = "sap_chieu"
        elif m.release_date <= today <= m.end_date:
            status = "dang_chieu"
        else:
            status = "ngung_chieu"

        result.append({
            "id": m.id,
            "title": m.title,
            "actors": m.actors,
            "age_rating": m.age_rating,
            "duration_min": m.duration_min,
            "description": m.description,
            
            "status": status,

            "categories": [c.name for c in m.categories],
            
            "release_date": m.release_date,
            "end_date": m.end_date,
            
            "posters": [
                {
                    "name": p.name,
                    "path": p.path
                }
                for p in m.posters
            ],

            "trailers": [
                {
                    "name": t.name,
                    "path": t.path
                }
                for t in m.trailers
            ]
        })

    return {
        "items": result,
        "total": total
    }
    
def create_movie_admin_service(db: Session, data):

    try:
        category_names = data.categories or []

        existing_categories = []

        if category_names:
            existing_categories = db.query(Category).filter(
                Category.name.in_(category_names)
            ).all()

            existing_names = [c.name for c in existing_categories]

            not_found = set(category_names) - set(existing_names)

            if not_found:
                raise ValueError(f"Category không tồn tại: {list(not_found)}")

        movie = Movie(
            title=data.title,
            age_rating=data.age_rating,
            duration_min=data.duration_min,
            actors=data.actors,
            description=data.description,
            release_date=data.release_date,
            end_date=data.end_date
        )
        
        if existing_categories:
            movie.categories = existing_categories
            
        db.add(movie)
        db.flush()

        for p in data.posters:
            if not p.name or not p.path:
                raise ValueError("Poster phải có name và path")

            db.add(Poster(
                movie_id=movie.id,
                name=p.name,
                path=p.path
            ))

        for t in data.trailers:
            if not t.name or not t.path:
                raise ValueError("Trailer phải có name và path")

            db.add(Trailer(
                movie_id=movie.id,
                name=t.name,
                path=t.path
            ))

        db.commit()
        db.refresh(movie)

        return movie

    except Exception:
        db.rollback()
        raise

def update_movie_admin_service(db: Session, movie_id: int, data):

    try:
        movie = db.query(Movie).filter(Movie.id == movie_id).first()

        if not movie:
            return None

        update_data = data.model_dump(exclude_unset=True)

        # update field cơ bản
        for key in [
            "title", "age_rating", "duration_min",
            "actors", "description", "release_date", "end_date"
        ]:
            if key in update_data:
                setattr(movie, key, update_data[key])

        if "posters" in update_data:

            db.query(Poster).filter(
                Poster.movie_id == movie.id
            ).delete()

            for p in update_data["posters"]:
                if not p["name"] or not p["path"]:
                    raise ValueError("Poster phải có name và path")

                db.add(Poster(
                    movie_id=movie.id,
                    name=p["name"],
                    path=p["path"]
                ))

        if "trailers" in update_data:

            db.query(Trailer).filter(
                Trailer.movie_id == movie.id
            ).delete()

            for t in update_data["trailers"]:
                if not t["name"] or not t["path"]:
                    raise ValueError("Trailer phải có name và path")

                db.add(Trailer(
                    movie_id=movie.id,
                    name=t["name"],
                    path=t["path"]
                ))
                
        if "categories" in update_data:

            category_names = update_data["categories"]

            existing_categories = db.query(Category).filter(
                Category.name.in_(category_names)
            ).all()

            existing_names = [c.name for c in existing_categories]

            not_found = set(category_names) - set(existing_names)

            if not_found:
                raise ValueError(f"Category không tồn tại: {list(not_found)}")

        movie.categories = existing_categories

        db.commit()
        db.refresh(movie)

        return movie

    except Exception:
        db.rollback()
        raise
    
    
