from utils.hash import hash_role

def has_role(token_data: dict, role_name: str) -> bool:
    return token_data.get("role") == hash_role(role_name)