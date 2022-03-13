from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric
from sqlalchemy.orm import relationship, backref

from daos.status_dao import StatusDAO
from db import Base


class OrderDAO(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)  # Auto generated primary key
    customer_id = Column(String)
    order_address = Column(String)
    total_price = Column(Integer)
    order_date = Column(Date)
    delivery_date = Column(Date)
    # reference to status as foreign key relationship. This will be automatically assigned.
    status_id = Column(Integer, ForeignKey('status.id'))
    # https: // docs.sqlalchemy.org / en / 14 / orm / basic_relationships.html
    # https: // docs.sqlalchemy.org / en / 14 / orm / backref.html
    status = relationship(StatusDAO.__name__, backref=backref("orders", uselist=False))

    def __init__(self, customer_id, order_address, total_price, order_date, delivery_date, status):
        self.customer_id = customer_id
        self.order_address = order_address
        self.total_price = total_price
        self.order_date = order_date
        self.delivery_date = delivery_date
        self.status = status
