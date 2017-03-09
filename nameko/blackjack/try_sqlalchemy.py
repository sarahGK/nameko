"""from nameko_sqlalchemy import Session
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from nameko.rpc import rpc
#from .models import Model,DeclarativeBase

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'
  id = sa.Column(sa.Integer,primary_key=True) 
  username = sa.Column(sa.String)

class MyService(object):
  name = 'myservice'
  session = Session(Base)

  @rpc
  def get_username(self,user_id):
    user = self.session.query(User).get(user_id)
    if user is not None:
      return user.username


from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  fullname = Column(String)
  password = Column(String)

  def __repr__(self):
    return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)
"""
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
 
 
Base = declarative_base()
 
 
class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)
 
 
class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Use default=func.now() to set the default hiring time
    # of an Employee to be the current time when an
    # Employee record was created
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    # Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
    department = relationship(
        Department,
        backref=backref('employees',
                         uselist=True,
                         cascade='delete,all'))
 
 
from sqlalchemy import create_engine
engine = create_engine('sqlite:///orm_in_detail.sqlite')
 
from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
