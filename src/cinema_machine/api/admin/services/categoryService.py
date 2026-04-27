from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.movies.category import Category

def get_all_categories_service(db: Session, page: int = 1, page_size: int = 30):

    offset = (page - 1) * page_size

    total = db.query(Category).count()
    
    categories = (
        db.query(Category)
        .order_by(Category.id.desc())
        .offset(offset)
        .limit(page_size)
        .all()
    )

    result = []

    for c in categories:

        result.append({
            "id": c.id,
            "name": c.name,
            "description": c.description,
        })

    return {
        "items": result,
        "total": total
    }
    
def create_category_admin_service(db: Session, data):

    existing = db.query(Category).filter(Category.name == data.name).first()

    if existing:
        raise ValueError("Category name already exists")

    try:
        category = Category(
            name=data.name,
            description=data.description,
        )

        db.add(category)
        db.commit()
        db.refresh(category)

        return category

    except Exception:
        db.rollback()
        raise




def update_category_admin_service(db: Session, category_id: int, data):

    try:
        category = db.query(Category).filter(Category.id == category_id).first()

        if not category:
            return None

        update_data = data.model_dump(exclude_unset=True)

        if "name" in update_data:

            existing = db.query(Category).filter(
                func.lower(Category.name) == update_data["name"].lower(),
                Category.id != category_id
            ).first()

            if existing:
                raise ValueError("Category name already exists")

        for key in ["name", "description"]:
            if key in update_data:
                setattr(category, key, update_data[key])

        db.commit()
        db.refresh(category)

        return category

    except IntegrityError:
        db.rollback()
        raise ValueError("Category name already exists")

    except Exception:
        db.rollback()
        raise