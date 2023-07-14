#!/usr/bin/python3
''' Unittest for user.py '''

import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    ''' Tests instances and methods from city class '''
    cty = City()

    def test_class_exists(self):
        ''' tests if class exists '''
        self.assertEqual(str(type(self.cty)), "<class 'models.city.City'>")

    def test_user_inheritance(self):
        ''' test if city is a subclass of BaseModel '''
        self.assertTrue(self.cty, City)

    def testHasAttributes(self):
        ''' verify if attributes exist '''
        self.assertTrue(hasattr(self.cty, 'state_id'))
        self.assertTrue(hasattr(self.cty, 'name'))
        self.assertTrue(hasattr(self.cty, 'id'))
        self.assertTrue(hasattr(self.cty, 'created_at'))
        self.assertTrue(hasattr(self.cty, 'updated_at'))

    def test_types(self):
        ''' tests if the type of the attribute is the correct one '''
        self.assertIsInstance(self.cty.state_id, str)
        self.assertIsInstance(self.cty.name, str)
        self.assertIsInstance(self.cty.id, str)
        self.assertIsInstance(self.cty.created_at, datetime.datetime)
        self.assertIsInstance(self.cty.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
