import hashlib
from config.dataConfig import settings

def sha256_hash(text: str) -> str:
    return hashlib.sha256(text.strip().lower().encode()).hexdigest()


def hash_role(role_name: str) -> str:
    normalized = role_name.strip().lower()

    raw = normalized + settings.SECRET_ROLE_KEY

    return hashlib.sha256(raw.encode()).hexdigest()

default_role = settings.DEFAULT_ROLE

