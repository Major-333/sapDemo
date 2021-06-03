# -*- coding:UTF-8 -*-
from sqlalchemy.orm import Session

import models
import schemas
from datetime import datetime


def create_record(db: Session, record:schemas.RecordCreate):
    db_item = models.Record(
        instance_id=record.instance_id,
        source=record.source,
        is_synchronized=record.is_synchronized,
        event_ts=record.event_ts
    )
    print(db_item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_records(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.Record).offset(skip).limit(limit).all()
