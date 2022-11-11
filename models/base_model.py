#!/usr/bin/python3
"""module defines base class for all other models"""
from datetime import datetime
import uuid


class BaseModel:
    """base class for our models"""
    def __init__(self, *args, **kwargs):
        """initialization"""
        # args executed at first, but for kwargs, id not present because the object already has an id from args

        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], %Y-%m-%dT%H:%M:%S.%f)
            kwargs['updated_at'] = datetime.strptime(kwargs['updted_at'], %Y-%m-%dT%H:%M:%S.%f)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """updates updated_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns simpler dictionary format of an instance"""
        # __name__ returns child class and not parent class BaseModel

        dictionary = self.__dict__.copy()
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        dictionary["__class__"] = type(self).__name__

        return dictionary

    def __str__(self):
        """return string representation of BaseModel instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
