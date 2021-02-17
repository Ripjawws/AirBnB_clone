#!/usr/bin/python3
""" importing
"""
import models
import os.path
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""
AirBnB Clone
"""


class FileStorage:
    """ class file storage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """  sets in __objects the obj with key obj class name.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        my_dict = {}
        for k, v in self.__objects.items():
            my_dict[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                des_json = json.load(f)
                for key, value in des_json.items():
                    # Separate name_class from id and split the separator
                    k = key.split('.')
                    # search "__class__": "BaseModel"
                    class_name = k[0]
                    # set in __objects the key, value
                    self.new(eval("{}".format(class_name))(**value))
