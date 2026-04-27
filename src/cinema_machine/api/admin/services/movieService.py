from datetime import date
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import OperationalError
from models.movies.movie import Movie
from models.movies.poster import Poster
from models.movies.trailer import Trailer

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
                {"path": p.path}
                for p in m.posters
            ],

            "trailers": [
                {"path": t.path}
                for t in m.trailers
            ]
        })

    return {
        "items": result,
        "total": total
    }
    
def create_movie_admin_service(db: Session, data):

    try:
        # 🔥 VALIDATE
        validate_media(data.poster_path, data.poster_name, "poster")
        validate_media(data.trailer_path, data.trailer_name, "trailer")

        movie = Movie(
            title=data.title,
            age_rating=data.age_rating,
            duration_min=data.duration_min,
            actors=data.actors,
            description=data.description,
            release_date=data.release_date,
            end_date=data.end_date
        )

        db.add(movie)
        db.flush()

        # ✅ POSTER
        if data.poster_path and data.poster_name:
            db.add(Poster(
                path=data.poster_path,
                name=data.poster_name,
                movie_id=movie.id
            ))

        # ✅ TRAILER
        if data.trailer_path and data.trailer_name:
            db.add(Trailer(
                path=data.trailer_path,
                name=data.trailer_name,
                movie_id=movie.id
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

        # 🔥 lấy existing
        existing_poster = db.query(Poster).filter(Poster.movie_id == movie.id).first()
        existing_trailer = db.query(Trailer).filter(Trailer.movie_id == movie.id).first()

        # 🔥 VALIDATE
        validate_media_update(
            update_data.get("poster_path"),
            update_data.get("poster_name"),
            existing_poster,
            "poster"
        )

        validate_media_update(
            update_data.get("trailer_path"),
            update_data.get("trailer_name"),
            existing_trailer,
            "trailer"
        )

        # update field cơ bản
        for key in [
            "title", "age_rating", "duration_min",
            "actors", "description", "release_date", "end_date"
        ]:
            if key in update_data:
                setattr(movie, key, update_data[key])

        # 🔥 POSTER
        if existing_poster:
            if "poster_path" in update_data:
                existing_poster.path = update_data["poster_path"]

            if "poster_name" in update_data:
                existing_poster.name = update_data["poster_name"]

        else:
            if update_data.get("poster_path") and update_data.get("poster_name"):
                db.add(Poster(
                    path=update_data["poster_path"],
                    name=update_data["poster_name"],
                    movie_id=movie.id
                ))

        # 🔥 TRAILER
        if existing_trailer:
            if "trailer_path" in update_data:
                existing_trailer.path = update_data["trailer_path"]

            if "trailer_name" in update_data:
                existing_trailer.name = update_data["trailer_name"]

        else:
            if update_data.get("trailer_path") and update_data.get("trailer_name"):
                db.add(Trailer(
                    path=update_data["trailer_path"],
                    name=update_data["trailer_name"],
                    movie_id=movie.id
                ))

        db.commit()
        db.refresh(movie)

        return movie

    except Exception:
        db.rollback()
        raise
    
    
    
    
    
    
    
def validate_media(path, name, field_name="poster"):
    if path and not name:
        raise ValueError(f"{field_name}_name is required when {field_name}_path is provided")

    if name and not path:
        raise ValueError(f"{field_name}_path is required when {field_name}_name is provided")
    

def validate_media_update(path, name, existing, field_name="poster"):

    # không truyền gì → OK
    if path is None and name is None:
        return

    # nếu chưa có record mà chỉ truyền 1 field → lỗi
    if not existing:
        if path is None or name is None:
            raise ValueError(
                f"{field_name}_path và {field_name}_name phải có đủ khi tạo mới"
            )