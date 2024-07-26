#!/usr/bin/env python3
"""base class with basic functionality"""
import uuid
from datetime import datetime as dt


class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = dt.now()
        self.updated_at = dt.now()

    def __str__(self):
        nm = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return nm
