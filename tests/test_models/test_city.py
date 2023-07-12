#!/usr/bin/python3
''' '''
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    ''' '''
    cty = City()

    def test_class_exists(self):
        ''' '''
        self.assertEqual(str(type(self.cty)), "<class 'models.city.City'>")

    def test_user_inheritance(self):
        ''' '''
        self.assertTrue(self.cty, City)

    def testHasAttributes(self):
        ''' '''
        self.assertTrue(hasattr(self.cty, 'state_id'))
        self.assertTrue(hasattr(self.cty, 'name'))
        self.assertTrue(hasattr(self.cty, 'id'))
        self.assertTrue(hasattr(self.cty, 'created_at'))
        self.assertTrue(hasattr(self.cty, 'updated_at'))

    def test_types(self):
        ''' '''
        self.assertIsInstance(self.cty.state_id, str)
        self.assertIsInstance(self.cty.name, str)
        self.assertIsInstance(self.cty.id, str)
        self.assertIsInstance(self.cty.created_at, datetime.datetime)
        self.assertIsInstance(self.cty.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
