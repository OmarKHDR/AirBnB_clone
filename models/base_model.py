#!/usr/bin/env python3
"""base class with basic functionality"""
import uuid
from datetime import datetime as dt
from models import storage


timeformat = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            #print("restoring old instance from files....")
            for key in kwargs.keys():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, dt.strptime(kwargs[key], timeformat))
                    continue
                if key == '__class__':
                    continue
                setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = (dt.now())
            self.updated_at = (dt.now())
            storage.new(self)

    def __str__(self):
        nm = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return nm

    def save(self):
        storage.save()
        self.updated_at = (dt.now())

    def to_dict(self):
        dic = self.__dict__.copy()
        dic['updated_at'] = dt.isoformat(self.updated_at)
        dic['created_at'] = dt.isoformat(self.created_at)
        dic['__class__'] = type(self).__name__
        return dic
