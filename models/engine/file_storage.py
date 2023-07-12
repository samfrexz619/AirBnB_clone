#!/usr/bin/python3
'''file storage'''

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

dict_cls = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review}


class FileStorage:
    '''file storage class'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
        return the dict of objects
        Args:
            None
        Returns:
            the dict of objs
        '''
        return self.__objects

    def new(self, obj):
        '''
        save in each object created

        Args:
            obj
        Returns:
            None

        '''
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        '''
        Save the result in file.json
        Args:
            None

        Returns:
            None
        '''
        new = {}
        for elem in self.__objects:
            new[elem] = self.__objects[elem].to_dict()
        with open(self.__file_path, 'w') as fd:
            json.dump(new, fd)

    def reload(self):
        '''
        reload file
        Args:
            None

        Returns:
            None
        '''
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r') as fd:
                var = json.load(fd)
                for elem in var:
                    aux = dict_cls[var[elem]['__class__']]
			self.__objects[elem] = aux(**(var[elem]))
