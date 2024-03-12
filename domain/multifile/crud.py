from sqlalchemy.orm import Session
from . import model, schema

def create_multifile(db: Session, multifile: schema.MultiFileCreate, user_id: int):
    db_multifile = model.MultiFile(**multifile.dict(), uid=user_id)
    db.add(db_multifile)
    db.commit()
    db.refresh(db_multifile)
    return db_multifile

def update_multifile(db: Session, mfid: int, multifile: schema.MultiFileUpdate):
    db_multifile = db.query(model.MultiFile).filter(model.MultiFile.mfid == mfid).first()
    if db_multifile:
        update_data = multifile.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_multifile, key, value)
        db.commit()
        db.refresh(db_multifile)
    return db_multifile

def delete_multifile(db: Session, mfid: int):
    db_multifile = db.query(model.MultiFile).filter(model.MultiFile.mfid == mfid).first()
    if db_multifile:
        db.delete(db_multifile)
        db.commit()
    return db_multifile
