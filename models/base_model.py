#!/usr/bin/python3
"""Write a class BaseModel that defines all common attributes/methods
Use uuid.uuid4() to generate unique id
The goal is to have unique id for each BaseModel
Returns a dictionary containing all keys/values of __dict__ of the instance."""

import uuid
from datetime import datetime
import models


class BaseModel:
    """The represent the base model.

    Attributes:
      id (str): with an uuid when an instance is created.

    """
    def __init__(self, *args, **kwargs):

        """This initialize a new BaseModel.

        Args:
            id (str): The identity of the BaseModel.
        """
        format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "created_at":
                    self.created_at = datetime.strptime(v, format)
                elif k == "updated_at":
                    self.updated_at = datetime.strptime(v, format)
                elif k == "__class__":
                    pass
                else:
                    setattr(self, k, v)
            models.storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):

        """Updates the public instance attribute updated_at."""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):

        """Returns a dictionary containing all keys/values"""

        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj

    def __str__(self):

        """Should print: [<class name>] (<self.id>) <self.__dict__>."""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
