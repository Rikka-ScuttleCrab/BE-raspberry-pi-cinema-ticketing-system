from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_, func
from datetime import date
from models.users.user import User
from models.users.role import Role
from utils.hash import sha256_hash, hash_role, default_role



def get_all_users_service(db: Session):

    users = (
        db.query(User)
        .options(joinedload(User.role))
        .order_by(User.id.desc())
        .all()
    )

    result = []

    for u in users:
        result.append({
            "id": u.id,
            "username": u.username,
            "email": u.email,
            "role_name": u.role.role_name if u.role else None,
            "working": u.working
        })

    return result



def create_role(db: Session, role_name: str):
    role_name = role_name.strip().lower()
    role_id = hash_role(role_name)

    role = db.query(Role).filter(Role.id == role_id).first()
    if role:
        return role

    role = Role(
        id=role_id,
        role_name=role_name
    )

    db.add(role)
    db.commit()
    db.refresh(role)

    return role

def signup(db: Session, username: str, email: str, password: str):

    username = username.strip()
    email = email.strip().lower()

    existing_user = db.query(User).filter(
        or_(
            User.username == username,
            User.email == email
        )
    ).first()

    if existing_user:
        return None, "User đã tồn tại"

    role_id = hash_role(default_role)

    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        return None, "Role mặc định chưa được tạo"

    password_hash = sha256_hash(password)

    user = User(
        username=username,
        email=email,
        password_hash=password_hash,
        role_id=role_id,
        day_create=date.today()
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user, None

def update_user_service(db: Session, user_id: int, data, current_user_id=None):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None

    update_data = data.model_dump(exclude_unset=True)


    if "email" in update_data:
        existing = db.query(User).filter(
            func.lower(User.email) == update_data["email"].lower(),
            User.id != user_id
        ).first()

        if existing:
            raise ValueError("Email already exists")

        user.email = update_data["email"]

    if "username" in update_data:
        user.username = update_data["username"]

    if "password" in update_data:
        if not update_data["password"]:
            raise ValueError("Password cannot be empty")

        user.password_hash = sha256_hash(update_data["password"])

    if "role_name" in update_data:

        new_role_name = update_data["role_name"].strip().lower()

        role = db.query(Role).filter(
            func.lower(Role.role_name) == new_role_name
        ).first()

        if not role:
            raise ValueError("Role not found")

        current_role_name = user.role.role_name.lower() if user.role else None

        if current_user_id == user_id:
            if current_role_name == "admin" and new_role_name != "admin":
                raise ValueError("Admin cannot downgrade own role")

        user.role_id = role.id

    if "working" in update_data:

        working_value = update_data["working"]

        if not isinstance(working_value, bool):
            raise ValueError("working must be boolean")

        if current_user_id == user_id and working_value is False:
            raise ValueError("Cannot disable yourself")

        user.working = working_value

    user.day_update = date.today()

    db.commit()
    db.refresh(user)

    return user