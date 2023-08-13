#!/usr/bin/python3
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
    __file_path = 'file.json'
    __objects = {}
    __class = {'BaseModel': BaseModel}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)

        FileStorage.__objects[key] = obj

        '''
    def save(self):
        serialized = {}

        with open(self.__file_path, 'w') as content:
            data = {key:obj.to_dict() for (key, obj) in self.__objects.items()}
            json.dump(data, content)
        for key, obj in FileStorage.__objects.items():
            serialized[key] = obj.to_dict()

        with open(self.__file_path, "a") as f:
            json.dump(serialized, f, indent=4)
        '''

    def save(self):
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
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding='utf-8') as f:
                data = json.load(f)
                class_mapping = self.all_classes()
                for k, v in data.items():
                    class_name, obj_id = k.split('.')
                    class_obj = class_mapping.get(class_name)
                    if class_obj:
                        FileStorage.__objects[k] = class_obj(**v)
