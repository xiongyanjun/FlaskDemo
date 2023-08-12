from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

import time

engine = create_engine('postgresql://postgres:123456@192.168.133.233:5432/postgres')  # 用户名:密码@localhost:端口/数据库名

Base = declarative_base()
DBSession = sessionmaker(bind=engine)


class User(Base):
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


class Admin(Base):
    # 表的名字:
    __tablename__ = 't_admin'

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


def create_table():
    # 创建表
    Base.metadata.create_all(engine)


def insert_data():
    # 插入操作
    # 创建会话
    session = DBSession()
    # 创建新User对象:
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    new_user = User(name='hsh4', sex='男', nation='汉', birth='19991012', id_address='广州大学',
                    id_number='441242142142',
                    create_time=local_time)
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()


def update_data():
    # 更新操作
    session = DBSession()  # 创建会话
    users = session.query(User).filter_by(name="hsh4").first()  # 查询条件
    users.id_number = users.id_number + "abcd"  # 更新操作
    session.add(users)  # 添加到会话
    session.commit()  # 提交即保存到数据库
    session.close()  # 关闭会话


if __name__ == '__main__':
    update_data()
