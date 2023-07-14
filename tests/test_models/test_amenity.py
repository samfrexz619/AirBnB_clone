#!/usr/bin/python3
''' Unittest for amenity.py '''

import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    ''' Tests instances and methods from amenity class '''
    aty = Amenity()

    def test_class_exists(self):
        ''' tests if class exists '''
        result = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.aty)), result)

    def test_user_inheritance(self):
        ''' test if Amenity is a subclass of BaseModel '''
        self.assertIsInstance(self.aty, Amenity)

    def test_has_attributes(self):
        ''' verify if attributes exist '''
        self.assertTrue(hasattr(self.aty, 'name'), True)

    def test_types(self):
        ''' tests if the type of the attribute is the correct one '''
        self.assertIsInstance(self.aty.name, str)


if __name__ == '__main__':
    unittest.main()
