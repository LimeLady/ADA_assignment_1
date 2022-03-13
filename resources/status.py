import datetime
from flask import jsonify
from daos.order_dao import OrderDAO
from db import Session


class Status:
    @staticmethod
    def update(o_id, status):
        session = Session()
        order = session.query(OrderDAO).filter(OrderDAO.id == o_id)[0]
        order.status.status = status
        order.status.last_update = datetime.datetime.now()
        session.commit()
        return jsonify({'message': 'The order status was updated'}), 200
