#!/usr/bin/python3
"""Recreate a BaseModel from another one by using a dictionary representation.
Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances.
"""
import json


class FileStorage:
    """__file_path
    __objects
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects""" 

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""

        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        data = {}
        for k, v in self.__objects.items():
            data[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)
    
    def reload(self):
        """deserializes the JSON file to __objects"""

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for k, v in data.items():
                    class_name = v['__class__']
                    self.__objects[k] = eval(class_name)(**v)
        else:
            pass

