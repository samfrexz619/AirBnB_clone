#!/usr/bin/python3
'''

'''
import json
import os

class FileStorage:
    ''' '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' '''
        return FileStorage.__objects

    def new(self, obj):
        ''' '''
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        ''' '''
        dic = {}

        for key, val in FileStorage.__objects.items():
            dic[key] = val.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dumps(dic, f)

    def reload(self):
        ''' '''
        from models.base_model import BaseModel

        dic = {"BaseModel": BaseModel,}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, val in json.load(f).items():
                    self.new(dic[val['__class__']](**val))
