#!/usr/bin/python3
""" importing
"""
import models
import os.path
import json
from models.base_model import BaseModel

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
		"""  sets in __objects the obj with key <obj class name>.id"""
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
		reload_dict = {}
		try:
			with open(FileStorage.__file_path, mode="r") as a_file:
				reload_dict = (json.load(a_file))
		except FileNotFoundError:
			pass
