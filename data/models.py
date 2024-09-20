
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from data.database import engine

Base = declarative_base()


class Server(Base):
    __tablename__ = 'servers'
    instance_id = Column(String(100), primary_key=True, index=True)
    type = Column(String(50))
    instance_type = Column(String(50))
    used_by = Column(String(200))
    cloudflare_no = Column(Integer)


Base.metadata.create_all(bind=engine)