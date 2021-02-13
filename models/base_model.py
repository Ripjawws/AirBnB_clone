#!/usr/bin/python3
"""
importing 
"""
import models
import uuid
from datetime import datetime
"""
AirBnB Clone
"""
class BaseModel:
	""" base model class """
	def __init__(self, *args, **kwargs):
		"""Instantiates the attributes of the BaseModel class"""
		if kwargs:
			for k, value in kwargs.items():
				if hasattr(self, "created_at") and type(self.created_at) is str:
					self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
				if hasattr(self, "updated_at") and type(self.updated_at) is str:
					self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
		else:				
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = self.created_at

	def __str__(self):
		""" Return the human readable print format"""
		return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
	
	def save(self):
		""" updates the public instance attribute
		updated_at with the current datetime"""
		self.updated_at = datetime.now()
	
	def to_dict(self):
		""" returns a dictionary containing all
		keys/values of __dict__ of the instance"""
		my_dict = {}
		for k, value in self.__dict__.items():
			if k =='created_at' or k == 'updated_at':
				my_dict[k] = value.isoformat()
			else:
				my_dict[k] = value
		return my_dict