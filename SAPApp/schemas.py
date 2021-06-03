# -*- coding:UTF-8 -*-
from typing import List
from pydantic import BaseModel
from datetime import datetime
from pydantic import BaseModel, validator


class RecordBase(BaseModel):
    instance_id: int
    source: str
    is_synchronized: bool
    event_ts: str


class RecordCreate(RecordBase):
    pass


class Record(RecordBase):
    record_id: int

    class Config:
        orm_mode = True
