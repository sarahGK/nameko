from nameko_sqlalchemy import Session
from nameko.rpc import rpc

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String)


class MyService(object):
    name = 'myservice'
    session = Session(Base)


    @rpc
    def get_username(self, user_id):
        user = self.session.query(User).get(user_id)
        if user is not None:
            return user.username
