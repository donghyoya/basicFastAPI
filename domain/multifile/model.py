from sqlalchemy import  Column, String, \
PrimaryKeyConstraint, BigInteger, Text, \
Boolean
from sqlalchemy.orm import relationship

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, \
PrimaryKeyConstraint, BigInteger, Text, DateTime 
from sqlalchemy.orm import relationship

from datetime import datetime

from default.config.database import Base

class MultiFile(Base):
    __tablename__ = 'MultiFile'
    __table_args__ = (
        PrimaryKeyConstraint('mfid', name='Multifile_pkey')
    )
    mfid = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    filename = Column(String(255))  # 파일 이름
    mimetype = Column(String(255))  # 파일 타입(MIME 타입)
    filesize = Column(BigInteger)  # 파일 사이즈
    upload_date = Column(DateTime, default=datetime.utcnow)  # 업로드 날짜
    file_path = Column(Text)  # 파일 저장 위치
    uid = Column(BigInteger, ForeignKey('User.uid'))  # User 테이블의 uid를 외래 키로 참조