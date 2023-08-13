#!/usr/bin/python3
"""Importing the necessary classes"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class that store the review parameters"""

    place_id = ""
    user_id = ""
    text = ""
