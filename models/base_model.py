#!/usr/bin/python3
'''parent class that will inherit'''

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    '''Defines all common attributes/methods '''
    def __init__(self, *args, **kwargs):
        '''initializes all attributes '''
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            fmt = '%Y-%m-%dT%H:%M:%S.%f'
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.strptime(kwards[key], fmt)
                    if key != '__class__':
                        setattr(self, key, val)


    def __str__(self):
        '''returns class name, id and attribute dictionary '''
        class_name = '[" + self.__class__.__name__ + "]'
        dic = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + ' (" + self.id + ") ' + str(dic)

    def save(self):
        '''updates last update time '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''creates a new dictionary, adding a key and returning
        datemtimes converted to strings '''
        n_dict = {}

        for key, vals in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                n_dict[key] = vals.strftime('%Y-%m-%dT%H:%M:%S.%f')
            else:
                if not vals:
                    pass
                else:
                    n_dict[key] = vals
        n_dict['__class__'] = self.__class__.__name__

        return n_dict

