#coding:utf-8
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# ��������Ļ���:
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

# ����Session:
session = DBSession()
# ����Query��ѯ��filter��where������������one()����Ψһ�У��������all()�򷵻�������:
# user = session.query(User).filter(User.ID=='5').one()
user = session.query(User).limit(6).all()
# ��ӡ���ͺͶ����name����:
print  user[2].TIME
# �ر�Session:
session.close()