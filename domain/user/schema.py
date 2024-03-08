from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    loginId: Optional[str]
    password: Optional[str]
    nickName: Optional[str] = None
    email: Optional[str] = None
    wallet_address: Optional[str] = None
    profileImage: Optional[str] = None
    klipToken: Optional[str] = None

class UserCreate(UserBase):
    loginId: str
    password: str
    nickName: str
    email: str
    wallet_address: str
    profileImage: str

class UserLogin(BaseModel):
    loginId: Optional[str]
    password: Optional[str]

class rmDataCheck(BaseModel):
    loginId: Optional[str]
    klipToken: Optional[str]
    rmData: Optional[bool]