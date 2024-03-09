from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MultiFileBase(BaseModel):
    filename: str
    mimetype: str
    filesize: int
    upload_date: Optional[datetime] = None
    file_path: str

class MultiFileCreate(MultiFileBase):
    pass

class MultiFileUpdate(MultiFileBase):
    pass

class MultiFileInDB(MultiFileBase):
    mfid: int
    uid: int

    class Config:
        orm_mode = True
