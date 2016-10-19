#coding:utf-8
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

class User(Base):
    __tablename__ = 't66y'
    ID = Column(String(20), primary_key=True)
    TITLE = Column(String(1200))
    LINK = Column(String(1200))
    AUTHOR = Column(String(120))
    TIME = Column(String(200))
    
    
engine = create_engine('mysql+mysqldb://root:900502@localhost:3306/t66y')
DBSession = sessionmaker(bind=engine)

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# user = session.query(User).filter(User.ID=='5').one()
user = session.query(User).limit(6).all()
# 打印类型和对象的name属性:
print  user[2].TIME
# 关闭Session:
session.close()