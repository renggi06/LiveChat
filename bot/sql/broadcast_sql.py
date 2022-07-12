import os
import threading
from pyrogram.types import Message
from . import (
    SESSION,
    BASE
)
from sqlalchemy import Column, TEXT, Numeric


INSERTION_LOCK = threading.RLock()

class Broadcast(BASE):
    __tablename__ = "broadcast"
    id = Column(Numeric, primary_key=True)
    user_name = Column(TEXT)

    def __init__(self, id, user_name):
        self.id = id
        self.user_name = user_name

Broadcast.__table__.create(checkfirst=True)


#  Add user details -
async def add_user(id, user_name):
    with INSERTION_LOCK:
        msg = SESSION.query(Broadcast).get(id)
        if not msg:
            usr = Broadcast(id, user_name)
            SESSION.add(usr)
            SESSION.commit()
        else:
            pass
          
async def full_userbase():
    users = SESSION.query(Broadcast).all()
    SESSION.close()
    return users

async def query_msg():
    try:
        query = SESSION.query(Broadcast.id).order_by(Broadcast.id)
        return query
    finally:
        SESSION.close()
