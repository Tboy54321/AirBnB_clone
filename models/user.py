#!/usr/bin/python3
"""Importting the necessary classes"""
from models.base_model import BaseModel


class User(BaseModel):
    """class that store User parameters"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Inheriting the BaseModel class"""
        
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Overwriting the to dict method"""

        user_dict = super().to_dict()
        user_dict["email"] = self.email
        user_dict["password"] = self.password
        user_dict["first_name"] = self.first_name
        user_dict["last_name"] = self.last_name
        return user_dict
