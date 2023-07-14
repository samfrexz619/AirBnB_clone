#!/usr/bin/python3
"""
Parent class
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    '''
    Defines the common attrs
    '''
    def __init__(self, *args, **kwargs):
        '''
        init class
        '''
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        '''rets data'''
        clsName = "[" + self.__class__.__name__ + "] "
        clsId = "(" + self.id + ") "
        clsDict = str(self.__dict__)
        return clsName + clsId + clsDict

    def save(self):
        '''saves items'''
        val = datetime.now()
        setattr(self, 'updated_at', val)
        models.storage.save()

    def to_dict(self):
        '''gets the dict and key class'''
        new_dict = {}
        var = self.__dict__
        for elem in var:
            if elem == 'created_at' or elem == 'updated_at':
                new_dict[elem] = var[elem].isoformat()
            else:
                new_dict[elem] = var[elem]
        new_dict['__class__'] = self.__class__.__name__
        return (new_dict)
