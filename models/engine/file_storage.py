#!/usr/bin/env python3
import json
from os import path
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """"
        Returns the dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets the dictionary with id
        """
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """
        Saves the instance to a file
        """
        with open(FileStorage.__file_path, "w") as f:
            serialized_obj = {}
            for key, value in FileStorage.__objects.items():
                serialized_obj[key] = value.to_dict()
            json.dump(serialized_obj, f)

    def reload(self):
        """
        Reloads the instances from a json file
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                deserialized_obj = json.load(f)
                for key, value in deserialized_obj.items():
                    class_name, obj_id = key.split(".")
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj
        else:
            return
