from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session

from core.database import get_db
from core.security import SECRET_KEY, ALGORITHM
from repositories.user_repository import get_user_by_id

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id = payload.get("user_id")

        if user_id is None:
            raise HTTPException(401, "Invalid token")

    except:
        raise HTTPException(401, "Invalid token")

    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(401, "User not found")

    return user