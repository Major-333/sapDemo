# -*- coding:UTF-8 -*-
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float, BOOLEAN, DateTime
from sqlalchemy.orm import relationship
import datetime
from database import Base


class Record(Base):
    __tablename__ = "record"

    record_id = Column(Integer, primary_key=True)
    instance_id = Column(Integer)
    source = Column(String(50))
    is_synchronized = Column(Boolean)
    event_ts: datetime = Column(String(50))
