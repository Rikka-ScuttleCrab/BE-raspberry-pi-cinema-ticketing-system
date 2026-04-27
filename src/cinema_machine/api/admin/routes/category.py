import math
from core.security.role import has_role
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from api.response import success_response, error_response
from api.deps import get_db, get_current_user_token
from api.admin.schemas.category import (
    CategoryAdminResponse,
    CategoryCreateAdmin,
    CategoryUpdateAdmin
)

from api.admin.services.categoryService import (
    get_all_categories_service,
    create_category_admin_service,
    update_category_admin_service
)

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/")
def get_all_categories(
    page: int = Query(1, ge=1),
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", status_code=403)

    raw = get_all_categories_service(db, page=page)

    items = [
        CategoryAdminResponse.model_validate(m).model_dump(mode="json")
        for m in raw["items"]
    ]

    page_size = 30
    total = raw["total"]
    total_pages = math.ceil(total / page_size)

    return success_response(
        data={
            "page": page,
            "page_size": page_size,
            "total": total,
            "total_pages": total_pages,
            "items": items,
        },
        message="GET ALL CATEGORIES SUCCESS"
    )
    
@router.post("/")
def create_category(
    payload: CategoryCreateAdmin,
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", status_code=403)

    try:
        category = create_category_admin_service(db, payload)

        return success_response(
            data={"id": category.id},
            message="CREATE CATEGORY SUCCESS",
            status_code=201
        )

    except ValueError as e:
        return error_response(str(e), status_code=400)


@router.put("/{category_id}")
def update_category(
    category_id: int,
    payload: CategoryUpdateAdmin,
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", status_code=403)

    try:
        category = update_category_admin_service(db, category_id, payload)

        if not category:
            return error_response("Category not found", status_code=404)

        return success_response(
            data={"id": category.id},
            message="UPDATE CATEGORY SUCCESS"
        )

    except ValueError as e:
        return error_response(str(e), status_code=400)