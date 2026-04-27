import jwt
from datetime import datetime, timedelta
from config.dataConfig import settings

def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(seconds=settings.ACCESS_TOKEN_EXPIRE_SECONDS)

    payload = data.copy()
    payload.update({
        "exp": expire,
        "type": "access"
    })

    token = jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM
    )
    return token


def create_refresh_token(data: dict):
    # refresh token thường sống lâu hơn
    expire = datetime.utcnow() + timedelta(days=30)

    payload = data.copy()
    payload.update({
        "exp": expire,
        "type": "refresh"
    })

    token = jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM
    )
    return token


def verify_token(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None