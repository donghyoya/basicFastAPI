from sqlalchemy.orm import Session
from . import model, schema
import hashlib

def get_user(db: Session, userId: int):
    return db.query(model.User).filter(model.User.uid == userId).first()

def get_user_by_email(db: Session, email:str):
    return db.query(model.User).filter(model.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).filter(model.User.rmData == False)\
        .offset(skip).limit(limit).all()
        
# 비밀번호를 암호화한다
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
    
# 암호화 검증
def verify_password(original_password: str, hashed_password: str) -> bool:
    return hash_password(original_password) == hashed_password

def create_user(db: Session, user: schema.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = model.User(userId=user.userId, 
                         email=user.email, password=hashed_password,
                         nickName=user.nickName
                         )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login(db: Session, id: str, pwd: str) -> bool:
    user = db.query(model.User).filter(model.User.userId == id, model.User.password == pwd).first()
    if user and verify_password(pwd, user.password):
        return True
    else:
        return False
