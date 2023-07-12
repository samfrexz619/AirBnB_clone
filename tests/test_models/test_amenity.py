#!/usr/bin/python3
''' '''
import unittest
from models.amenity import Amenity
import datetime

class TestAmenity(unittest.TestCase):
    ''' '''
    aty = Amenity()

    def test_class_exists(self):
        ''' '''
        result = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.aty)), result)

    def test_user_inheritance(self):
        ''' '''
        self.assertIsInstance(self.aty, Amenity)

    def test_has_attributes(self):
        ''' '''
        self.assertTrue(hasattr(self.aty, 'name'), True)

    def test_types(self):
        ''' '''
        self.assertIsInstance(self.aty.name, str)

if __name__ == '__main__':
    unittest.main()
