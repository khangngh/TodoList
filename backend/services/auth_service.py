from repositories.user_repository import *
from core.security import *
from fastapi import HTTPException


def register_user(db, email, password):

    if get_user_by_email(db, email):
        raise HTTPException(400, "Email already registered")

    hashed = hash_password(password)

    return create_user(db, email, hashed)


def login_user(db, email, password):

    user = get_user_by_email(db, email)

    if not user:
        raise HTTPException(401, "Invalid credentials")

    if not verify_password(password, user.hashed_password):
        raise HTTPException(401, "Invalid credentials")

    token = create_access_token({"user_id": user.id})

    return {"access_token": token}