#!/usr/bin/python3
""" importing """
from models.base_model import BaseModel

"""
AirBnB Clone
"""


class Review(BaseModel):
    """ review class """
    place_id = ""
    user_id = ""
    text = ""
