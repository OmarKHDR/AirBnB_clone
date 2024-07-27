#!/usr/bin/env python3
""" should work just as a DB"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def __init__(self) -> None:
        pass

    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects[obj.__class__.__name__ + '.' +obj.id] = obj.to_dict()
    
    def save(self):
        jsonstr = json.dumps(self.__objects)
        with open(self.__file_path, 'w') as f:
            f.write(jsonstr)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                jsonstring = f.read()
                if jsonstring == '':
                    return
                self.__objects = json.loads(jsonstring)

        except IOError:
            return
