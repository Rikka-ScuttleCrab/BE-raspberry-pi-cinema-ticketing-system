from fastapi import APIRouter, Depends, HTTPException
from api.response import success_response, error_response
from sqlalchemy.orm import Session
from api.deps import get_db, get_current_user_token

from core.security.role import has_role
from api.admin.services.authService import (
    get_all_users_service,
    update_user_service,
    create_role, 
    signup
)
from api.admin.schemas.auth import (
    AuthResponse,
    RoleCreate,
    SignupRequest,
    UpdateUserRequest
)


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/")
def get_all_users(
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", status_code=403)

    raw = get_all_users_service(db)

    data = [
        AuthResponse.model_validate(u).model_dump(mode="json")
        for u in raw
    ]

    return success_response(data=data, message="GET ALL USERS SUCCESS")

@router.post("/roles")
def create_role_api(
    req: RoleCreate,
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        raise HTTPException(status_code=403, detail="Không có quyền")

    role = create_role(db, req.role_name)

    return {
        "role_id": role.id,
        "role_name": role.role_name
    }


@router.post("/sign-up")
def signup_api(
    request: SignupRequest, 
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        raise HTTPException(status_code=403, detail="Không có quyền")
    user, error = signup(
        db,
        request.username,
        request.email,
        request.password,
    )

    if error:
        raise HTTPException(status_code=400, detail=error)

    return {
        "message": "Đăng ký thành công",
        "user_id": user.id
    }

@router.put("/{user_id}")
def update_user(
    user_id: int,
    payload: UpdateUserRequest,
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", status_code=403)

    try:
        user = update_user_service(db, user_id, payload)

        if not user:
            return error_response("User not found", status_code=404)

        return success_response(
            data={
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "working": user.working
            },
            message="UPDATE USER SUCCESS"
        )

    except ValueError as e:
        return error_response(str(e), status_code=400)