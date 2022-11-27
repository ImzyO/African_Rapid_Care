#!/usr/bin/python3
"""module defines base class for all other models"""
import models
from datetime import datetime
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


Base = declarative_base()


class BaseModel:
    """base class for our models"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """initialization"""
        # instanciate an object with data in kwargs if kwargs is present
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            if kwargs.get("created_at", None):
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if kwargs.get("updated_at", None):
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updted_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if kwargs.get("id", None) is None:
                setattr(self, id, str(uuid.uuid4()))
        # instanciate an object if kwargs is not present
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def save(self):
        """updates updated_at attribute"""
        self.updated_at = datetime.utcnow()
        models.database_storage.new(self)
        models.database_storage.save()

    def to_dict(self):
        """returns simpler dictionary format of an instance"""
        # __name__ returns child class and not parent class BaseModel

        dictionary = self.__dict__.copy()
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        dictionary["__class__"] = type(self).__name__
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]

        return dictionary

    def __str__(self):
        """return string representation of BaseModel instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def delete(self):
        """deletes instances from database_storage"""
        models.database_storage.delete(self)
