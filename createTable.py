from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from sqlalchemy.schema import CreateTable

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, \
PrimaryKeyConstraint, BigInteger, Text, DateTime ,Float
from sqlalchemy.orm import relationship

from dotenv import load_dotenv
from datetime import datetime
import os

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    __table_args__ = (
         PrimaryKeyConstraint('uid', name='User_pkey'),
    )  # 주의: 콤마를 추가하여 단일 항목이라도 튜플로 만들어줍니다.
    uid = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    userId = Column(String(20))
    password = Column(Text)
    nickName = Column(String(20))
    email = Column(String(30))
    rmData = Column(Boolean, default=False)
    images = relationship("MultiFile", back_populates="user")
    
class MultiFile(Base):
    __tablename__ = 'MultiFile'
    __table_args__ = (
        PrimaryKeyConstraint('mfid', name='Multifile_pkey'),
    )  # 주의: 콤마를 추가하여 단일 항목이라도 튜플로 만들어줍니다.
    mfid = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    filename = Column(String(255))  # 파일 이름
    mimetype = Column(String(255))  # 파일 타입(MIME 타입)
    filesize = Column(BigInteger)  # 파일 사이즈
    upload_date = Column(DateTime, default=datetime.utcnow)  # 업로드 날짜
    file_path = Column(Text)  # 파일 저장 위치
    uid = Column(BigInteger, ForeignKey('User.uid'))  # User 테이블의 uid를 외래 키로 참조
    

if __name__ == '__main__':
    
    engine = create_engine("mysql+pymysql://testuser:test0814@localhost:3307/testDB?charset=utf8mb4")
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)