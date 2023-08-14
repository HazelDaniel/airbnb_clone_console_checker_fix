#!/usr/bin/env python3
"""a module that defines a FileStorage class"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import datetime
import json


def file_exists(file_str):
    """a procedure that checks if a file exists"""
    try:
        with open(file_str, mode="r", encoding="utf-8") as _:
            return True
    except FileNotFoundError:
        return False


class FileStorage:
    """
    FileStorage serializes instances to a JSON file and
    deserializes JSON file to instance

    __file_path - string path to the JSON file
    __objects - an empty dictionary that will store all objects

    new - A method that create a dictionary object
    save - A method that save the dict object to json file
    reload - A method that load a json file
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """a public instance method that returns all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """adds an instance to the FileStorage.__objects
            dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """a public instance field that writes the FileStorage.__objects
            to a file"""
        json_obj = {key: item.to_dict() for key,
                    item in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, mode="w",
                  encoding="utf-8") as file:
            json.dump(json_obj, file)

    def reload(self):
        """a public instance methods that deserializes a JSON file
            to FileStorage.__objects"""
        if not file_exists(FileStorage.__file_path):
            return {}
        with open(FileStorage.__file_path, mode="r",
                  encoding="utf-8") as f_ptr:
            res_objs = json.load(f_ptr)
            for key, value in res_objs.items():
                if not value:
                    continue
                class_str = key.split(".")[0]
                instance = globals()[class_str](**{key: val for key, val
                                                   in value.items()
                                                   if not key == "__class__"})
                self.new(instance)
        return FileStorage.__objects
