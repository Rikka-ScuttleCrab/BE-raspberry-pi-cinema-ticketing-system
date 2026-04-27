from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.deps import get_db
from services.authService import SignIn
from api.schemas.auth import LoginRequest

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/sign-in")
def sign_in_api(request: LoginRequest, db: Session = Depends(get_db)):

    data, error = SignIn(
        db,
        request.username,
        request.password
    )

    if error:
        raise HTTPException(status_code=401, detail=error)

    return data