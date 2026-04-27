from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from api.deps import get_db, get_current_user_token
from api.response import success_response, error_response
from core.security.role import has_role

from api.admin.schemas.showtime import (
    ShowtimeCreate,
    ShowtimeUpdate,
    ShowtimeResponse
)

from api.admin.services.showtimeService import (
    get_all_showtimes_service,
    create_showtime_service,
    update_showtime_service
)

router = APIRouter(prefix="/showtimes", tags=["Admin - Showtimes"])


# =========================
# GET ALL (PAGINATION)
# =========================
@router.get("/")
def get_all_showtimes(
    page: int = Query(1, ge=1),
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", 403)

    raw = get_all_showtimes_service(db, page=page)

    data = [
        ShowtimeResponse.model_validate(i).model_dump(mode="json")
        for i in raw["items"]
    ]

    return success_response(
        data={
            "page": page,
            "total": raw["total"],
            "total_pages": (raw["total"] + 29) // 30,
            "items": data,
        },
        message="GET SHOWTIMES SUCCESS"
    )


# =========================
# CREATE
# =========================
@router.post("/")
def create_showtime(
    body: ShowtimeCreate,
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", 403)

    try:
        s = create_showtime_service(db, body)

        return success_response(
            data={"id": s.id},
            message="CREATE SHOWTIME SUCCESS"
        )

    except ValueError as e:
        return error_response(str(e))


# =========================
# UPDATE
# =========================
@router.put("/{showtime_id}")
def update_showtime(
    showtime_id: int,
    body: ShowtimeUpdate,
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", 403)

    try:
        s = update_showtime_service(db, showtime_id, body)

        if not s:
            return error_response("Showtime not found", 404)

        return success_response(
            data={"id": s.id},
            message="UPDATE SHOWTIME SUCCESS"
        )

    except ValueError as e:
        return error_response(str(e))