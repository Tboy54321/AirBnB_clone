import datetime
import uuid
# from models.engine.file_storage import FileStorage
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
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
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        dict_data = self.__dict__.copy()
        # if "created_at" in dict_data:
        dict_data["created_at"] = self.created_at.isoformat()
        # if "updated_at" in dict_data:
        dict_data["updated_at"] = self.updated_at.isoformat()
        dict_data["__class__"] = self.__class__.__name__
        return dict_data

    def __str__(self):
        return (f'[{type(self).__name__}] ({self.id}) {self.__dict__}')

    # def to_dict(self):
    #     data = {
    #         'users': [user.__dict__ for user in users],
    #         'cities': [city.__dict__ for city in cities],
    #         'places': [place.__dict__ for place in places]
    #     }
    #     with open("../database.json", "w") as file:
    #         json.dump(data, file, indent=2)
    # @property
    # def user(self):
    #     return self.__user__
    #
    # @user.setter
    # def user(self, user_content):
    #     return self.__user = user_content
    # def save_to_file(self):
    #     content = {key: }
    #     with open('../storage/database.json', 'w') as file:
    #         content = json.dumps(self.user)
    #         file.write(content)
