from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, model, schema
from typing import List
from ...default.config.database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/multifiles/", response_model=schema.MultiFileInDB)
def create_multifile(multifile: schema.MultiFileCreate, db: Session = Depends(get_db)):
    return crud.create_multifile(db=db, multifile=multifile, user_id=multifile.uid)

@router.put("/multifiles/{mfid}", response_model=schema.MultiFileInDB)
def update_multifile(mfid: int, multifile: schema.MultiFileUpdate, db: Session = Depends(get_db)):
    return crud.update_multifile(db=db, mfid=mfid, multifile=multifile)

@router.delete("/multifiles/{mfid}", response_model=schema.MultiFileInDB)
def delete_multifile(mfid: int, db: Session = Depends(get_db)):
    return crud.delete_multifile(db=db, mfid=mfid)
