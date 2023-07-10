#!/usr/bin/python3
''' '''
import unittest
import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    ''' '''
    aty = Amenity()

    def test_class_exists(self):
        ''' '''
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.aty)), res)

    def test_user_inheritance(self):
        ''' '''
        self.assertIsInstance(self.aty, Amenity)

    def test_has_attributes(self):
        ''' '''
        self.assertTrue(hasattr(self.aty, 'name'))
        self.assertTrue(hasattr(self.aty, 'id'))
        self.assertTrue(hasattr(self.aty, 'created_at'))
        self.assertTrue(hasattr(self.aty, 'updated_at'))

    def test_types(self):
        ''' '''
        self.assertIsInstance(self.aty.name, str)
        self.assertIsInstance(self.aty.id, str)
        self.assertIsInstance(self.aty.created_at, datetime.datetime)
        self.assertIsInstance(self.aty.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
