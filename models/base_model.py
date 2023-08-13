#!/usr/bin/python3
"""Importing the necessary classes"""

import datetime
import uuid
# from models.engine.file_storage import FileStorage
import models


class BaseModel:
    
    """BaseModel Method"""
    
    def __init__(self, *args, **kwargs):
        """Initializing the BaseModel class"""
        
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """Method for saving the data"""
        
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Method for converting it to dict"""
        
        dict_data = self.__dict__.copy()
        # if "created_at" in dict_data:
        dict_data["created_at"] = self.created_at.isoformat()
        # if "updated_at" in dict_data:
        dict_data["updated_at"] = self.updated_at.isoformat()
        dict_data["__class__"] = self.__class__.__name__
        return dict_data

    def __str__(self):
        """returns official string representation"""
        
        return (f'[{type(self).__name__}] ({self.id}) {self.__dict__}')
