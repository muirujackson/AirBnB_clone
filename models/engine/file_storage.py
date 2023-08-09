#!/usr/bin/python3
"""Recreate a BaseModel from another one by using a dictionary representation.
Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances.
"""
import json


class FileStorage:
    """__file_path
    __objects
    """
    __file_path = ""
    __objects = {}

    def all(self):
        """returns the dictionary __objects""" 

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""

        self.__objects = __class__.__name__

    def save(self):
        """serializes __objects to the JSON file"""

        self.__file_path = json.dumps(self.__objects)
    
    def reload(self):
        """deserializes the JSON file to __objects"""

        if (__file_path):
            self.__objects = json.loads(self.__file_path)
        else:
            pass

