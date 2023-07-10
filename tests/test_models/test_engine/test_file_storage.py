#!/usr/bin/python3
''' '''
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage



class FileStorageTests(unittest.TestCase):
    ''' '''

    my_model = BaseModel()

    def test_class_instance(self):
        ''' '''
        self.assertIsInstance(storage, FileStorage)

    def test_store_base_model(self):
        ''' '''
        self.my_model.f_name = 'BaseModel Instance'
        self.my_model.save()
        m_dict = self.my_model.to_dict()
        all_ob = storage.all()

        key = m_dict['__class__'] + "." + m_dict['id']
        self.assertEqual(key in all_ob, True)

    def test_store_base_model1(self):
        ''' '''
        self.my_model.me_name = 'First name'
        self.my_model.save()
        m_dict = self.my_model.to_dict()
        all_ob = storage.all()

        key = m_dict['__class__'] + "." + m_dict['id']

        self.assertEqual(key in all_ob, True)
        self.assertEqual(m_dict['me_name'], "First name")

        crt = m_dict['created_at']
        upd = m_dict['updated_at']

        self.my_model.me_name = 'Second Name'
        self.my_model.save()
        m_dict = self.my_model.to_dict()
        all_ob = storage.all()

        self.assertEqual(key, in all_ob, True)

        crt1 = m_dict['created_at']
        upd1 = m_dict['updated_at']

        self.assertEqual(crt, crt1)
        self.assertNotEqual(upd, upd1)
        self.assertEqual(m_dict['me_name'], "Second Name")

    def test_has_attributes(self):
        pass

    def test_save(self):
        ''' '''

        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        ''' '''
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        tob = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dobj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, val in storage.all().items():
            self.assertEqual(tob[key].to_dict(), val.to_dict())


if __name__ = '__main__':
    unittest.main()
