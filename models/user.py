#!/usr/bin/env python3
import models
from models.base_model import BaseModel

"""user"""


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
