from weakref import WeakKeyDictionary

from nameko.extensions import DependencyProvider
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Session(DependencyProvider):

    def __init__(self, declarative_base):
        self.declarative_base = declarative_base
        self.sessions = WeakKeyDictionary()

    def get_dependency(self, worker_ctx):
        db_uri = self.container.config['DATABASE_URL']
        engine = create_engine(db_uri)
        session_cls = sessionmaker(bind=engine)
        self.sessions[worker_ctx] = session = session_cls()
        return session

    def worker_teardown(self, worker_ctx):
        sess = self.sessions.pop(worker_ctx, None)
        if sess is not None:
            sess.close()
