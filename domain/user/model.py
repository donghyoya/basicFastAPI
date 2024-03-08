from sqlalchemy import  Column, String, \
PrimaryKeyConstraint, BigInteger, Text, \
Boolean
from sqlalchemy.orm import relationship

from default.config.database import Base

class User(Base):
    __tablename__ = 'User'
    __table_args__ = (
         PrimaryKeyConstraint('uid', name='User_pkey'),
     )
    uid = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    userId = Column(String(20))
    password = Column(Text)
    nickName = Column(String(20))
    email = Column(String(30))
    rmData = Column(Boolean,default=False)
    images = relationship("MultiFile", back_populates="user")