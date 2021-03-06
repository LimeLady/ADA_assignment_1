from sqlalchemy import Column, String, Integer, TIMESTAMP

from db import Base


class StatusDAO(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True) # Auto generated primary key
    status = Column(String) # Should this be Enum type to only be able to insert a set of strings?
    last_update = Column(TIMESTAMP(timezone=False))

    def __init__(self, status, last_update):
        self.status = status
        self.last_update = last_update
