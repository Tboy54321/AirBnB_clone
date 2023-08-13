#!/usr/bin/python3
"""Importing modules necessaty for the file storage"""
import json
import os
from models.base_model import BaseModel
from models import user
from models import amenity
from models import city
from models import place
from models import state
from models import review


class FileStorage:

    """Class for handling data"""
    __file_path = 'file.json'
    __objects = {}
    __class = {'BaseModel': BaseModel}

    def all(self):
        """method for storing all data"""
        return FileStorage.__objects

    def new(self, obj):
        """Method for creating new data"""
        key = "{}.{}".format(type(obj).__name__, obj.id)

        FileStorage.__objects[key] = obj

    def save(self):
        """Method for saving data"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        existing_data = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                existing_data = json.load(f)

        existing_data.update(obj_dict)

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=4)

    def all_classes(self):
        """method for storing all classes"""
        all_classes = {
            "User": user.User,
            "BaseModel": BaseModel,
            "Amenity": amenity.Amenity,
            "City": city.City,
            "Place": place.Place,
            "State": state.State,
            "Review": review.Review,
        }
        return all_classes

    # def reload(self):
    #     if os.path.exists(FileStorage.__file_path):
    #         with open(FileStorage.__file_path, encoding='utf-8') as f:
    #             data = json.load(f)
    #             for k, v in data.items():
    #                 class_name, obj_id = k.split('.')
    #                 class_obj = FileStorage.__class[class_name]
    #                 if class_obj:
    #                     FileStorage.__objects[k] = class_obj(**v)

    def reload(self):
        """Method for reloading"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding='utf-8') as f:
                data = json.load(f)
                class_mapping = self.all_classes()
                for k, v in data.items():
                    class_name, obj_id = k.split('.')
                    class_obj = class_mapping.get(class_name)
                    if class_obj:
                        FileStorage.__objects[k] = class_obj(**v)
