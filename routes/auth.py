from fastapi import APIRouter, HTTPException
from models.user_model import UserCreate, UserLogin
from controller.auth_controller import register_user, login_user

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    try:
        return register_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(user: UserLogin):
    try:
        return login_user(user)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
