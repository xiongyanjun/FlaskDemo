import time

from sqlalchemy import *
from app.app import db


class User(db.Base):
    # 表的名字:
    __tablename__ = 't_user'

    # 表的结构:
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    sex = Column(String(4), nullable=False)
    nation = Column(String(20), nullable=False)
    birth = Column(String(8), nullable=False)
    id_address = Column(Text, nullable=False)
    id_number = Column(String(18), nullable=False)
    creator = Column(String(32))
    create_time = Column(String(20), nullable=False)
    updater = Column(String(32))
    update_time = Column(String(20), nullable=False, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                         onupdate=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    comment = Column(String(200))


