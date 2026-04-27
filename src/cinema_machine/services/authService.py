from sqlalchemy.orm import Session
from sqlalchemy import or_
from models.users.user import User
from utils.hash import sha256_hash
from utils.token_service import create_access_token, create_refresh_token


def SignIn(db: Session, identifier: str, password: str):

    password_hash = sha256_hash(password)

    user = db.query(User).filter(
        or_(
            User.username == identifier,
            User.email == identifier
        ),
        User.password_hash == password_hash
    ).first()

    if not user:
        return None, "Sai thông tin đăng nhập"

    if user.working is False:
        return None, "Tài khoản đã bị vô hiệu hóa"

    access_token = create_access_token({
        "sub": str(user.id),
        "role": user.role_id
    })

    refresh_token = create_refresh_token({
        "sub": str(user.id)
    })

    user.refresh_token = refresh_token
    db.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }, None