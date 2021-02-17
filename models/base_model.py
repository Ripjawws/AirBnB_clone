#!/usr/bin/python3
"""Class BaseModel"""

import models
from datetime import datetime
import json
import uuid
import models

""" class base model """


class BaseModel:
    """Base Class with public instance attributes and methods"""

    def __init__(self, *args, **kwargs):
        """Instantiates the attributes of the BaseModel class"""
        if kwargs:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(item, "%Y-%m-%dT%H:%M:%S.%f")
                if key not in ['__class__']:
                    setattr(self, key, item)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Return the human readable print format"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        """return the dictionary of the instance
        """
        inst_dict = dict(self.__dict__)
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict
