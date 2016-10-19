# -*- coding:utf-8 -*-
import sys
import requests,json
from requests import get
from flask import Flask, render_template,request,session
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.secret_key = 'forget it you can never guess'
Base = declarative_base()

class Uget(Base):
    __tablename__ = 't66y'
    ID = Column(String(20), primary_key=True)
    TITLE = Column(String(1200))
    LINK = Column(String(1200))
    AUTHOR = Column(String(120))
    TIME = Column(String(200))
    
    
engine = create_engine('mysql+mysqldb://root:900502@localhost:3306/t66y?charset=utf8')
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/',methods=["GET","POST"])
def index():
    page=1
    uget= session.query(Uget).limit(20).all()
    session.close()
    return render_template('index.html',uget=uget,page=page)


@app.route('/page/<int:page>',methods=["GET","POST"])
def abc(page):
    uget= session.query(Uget).offset(20*page-20).limit(20).all()
    session.close()
    return render_template('index.html',uget=uget,page=page)

if __name__ == '__main__':
    app.run()
		



