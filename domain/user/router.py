from fastapi import APIRouter, Depends, HTTPException, Body, Query
from . import crud, schema
from sqlalchemy.orm import Session
from typing import List
from default.config import database
from redis import Redis
import secrets


router = APIRouter(
    tags=["user"]
)

def get_db():
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()


@router.post("/createUser",response_model=schema.UserCreate)
async def create_user(user: schema.UserCreate = Body(
    ...,
    example={
        "loginId": "testfastId",
        "password": "dong0814",
        "nickName": "blablabal",
        "email":"noting@test.com",
    },
), db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user_in_db = crud.create_user(db=db, user=user)
    return user_in_db

@router.get("/getUserbyId", response_model=schema.UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/login")
async def login(user_login: schema.UserLogin, db: Session = Depends(database.get_db)):
    user = crud.login(db=db, id=user_login.loginId, pwd=user_login.password)
    if user is None:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # 세션 토큰 생성 및 Redis에 저장
    session_token = secrets.token_urlsafe()
    redis_client = Redis(host='localhost', port=6379, db=0)
    redis_client.set(session_token, user.user_id, ex=3600)  # 예: 1시간 동안 유효한 세션

    return {"session_token": session_token}

@router.post("/logout")
async def logout(session_token: str = Header(None)):
    redis_client = Redis(host='localhost', port=6379, db=0)
    result = redis_client.delete(session_token)
    
    if result == 1:
        return {"message": "Logged out successfully"}
    else:
        raise HTTPException(status_code=404, detail="Session not found or already expired")

@router.get("/getUsers",response_model=List[schema.UserBase])
def getUsers(skip: int = Query(
    default=0,
    example=0
), limit: int = Query(
    default=10,
    example=10
), db: Session = Depends(get_db)):
    users = crud.get_users(skip=skip, limit=limit, db=db)
    if (len(users) == 0):
        raise HTTPException(
            status_code=404,
            detail="No User data",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return users

@router.patch("/appendUser",response_model=bool)
def appendUser(userId: int, db:Session = Depends(get_db)):
    apUser_db = crud.update_rmData_status(userId=userId, status="append",db=db)
    if apUser_db == False:
        raise HTTPException(status_code=404, detail="User not found")
    return apUser_db


@router.delete("/removeUser",response_model=bool)
def removeUser(userId: int,db: Session = Depends(get_db)):
    rmUser_db = crud.update_rmData_status(userId=userId,status="remove", db=db)
    return rmUser_db