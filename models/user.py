#!/usr/bin/env python3
from models.base_model import BaseModel
from models import storage
"""user"""

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
