#!/usr/bin/python3
#Write a class BaseModel that defines all common attributes/methods for other classes:
#Use uuid.uuid4() to generate unique id
#The goal is to have unique id for each BaseModel
#Updates the public instance attribute updated_at with the current datetime
#Returns a dictionary containing all keys/values of __dict__ of the instance

import uuid
import datetime

class BaseModel:
    """The represent the base model.

    It represent the BaseModel of all other classes in the project AirBnB_clone.

    Attributes:
      id (str): with an uuid when an instance is created.

    """

    def __init__(self):

        """This initialize a new BaseModel.

        Args:
            id (str): The identity of the BaseModel.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):

        """Updates the public instance attribute updated_at with the current datetime."""

        self.updated_at = datetime.now()

    def to_dict(self):

        """Returns a dictionary containing all keys/values of __dict__ of the instance."""

        return {
            "id": self.id
            "created_at": self.created_at()
            "updated_at": self.updated_at()
        }

    def __str__(self):

        """Should print: [<class name>] (<self.id>) <self.__dict__>."""

        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)
