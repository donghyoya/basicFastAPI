from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    loginId: Optional[str]
    password: Optional[str]
    nickName: Optional[str] = None
    email: Optional[str] = None
    
class UserCreate(UserBase):
    loginId: str
    password: str
    nickName: str
    email: str

class UserLogin(BaseModel):
    loginId: Optional[str]
    password: Optional[str]

class rmDataCheck(BaseModel):
    loginId: Optional[str]
    rmData: Optional[bool]