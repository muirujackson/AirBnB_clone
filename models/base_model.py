#!/usr/bin/python3
#Write a class BaseModel that defines all common attributes/methods for other classes:
#Use uuid.uuid4() to generate unique id
#The goal is to have unique id for each BaseModel
#Updates the public instance attribute updated_at with the current datetime
#Returns a dictionary containing all keys/values of __dict__ of the instance

import uuid
from datetime import datetime
from __init__ import storage

class BaseModel:
    """The represent the base model.

    It represent the BaseModel of all other classes in the project AirBnB_clone.

    Attributes:
      id (str): with an uuid when an instance is created.

    """
    def __init__(self, *args, **kwargs):

        """This initialize a new BaseModel.

        Args:
            id (str): The identity of the BaseModel.
        """

        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "created_at":
                    self.created_at = datetime.strptime(v,'%Y-%m-%dT%H:%M:%S.%f')
                elif k == "updated_at":
                    self.updated_at = datetime.strptime(v,'%Y-%m-%dT%H:%M:%S.%f')
                elif k == "__class__":
                    pass
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):

        """Updates the public instance attribute updated_at with the current datetime."""

        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):

        """Returns a dictionary containing all keys/values of __dict__ of the instance."""

        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj

    def __str__(self):

        """Should print: [<class name>] (<self.id>) <self.__dict__>."""

        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)
