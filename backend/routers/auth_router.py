from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.user_schema import *
from core.database import get_db
from services.auth_service import *
from core.dependencies import get_current_user
from models.user_model import User
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(data: UserRegister, db: Session = Depends(get_db)):    

    return register_user(db, data.email, data.password)


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login_user(db, form_data.username, form_data.password)

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):

    return current_user