#!/usr/bin/env python3
"""base class with basic functionality"""
import uuid
from datetime import datetime as dt


class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = dt.isoformat(dt.now())
        self.updated_at = dt.isoformat(dt.now())

    def __str__(self):
        nm = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return nm

    def save(self):
        self.updated_at = dt.isoformat(dt.now())

    def to_dict(self):
        dic = self.__dict__.copy()
        dic['__class__'] = type(self).__name__
        return dic


a = BaseModel()
print(a.updated_at)