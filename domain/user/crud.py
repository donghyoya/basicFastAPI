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