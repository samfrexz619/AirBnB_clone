#!/usr/bin/python3
''' Unittest for amenity.py '''

import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    ''' Tests instances and methods from amenity class '''

    plc = Place()

    def test_class_exists(self):
        ''' tests if class exists '''
        self.assertEqual(str(type(self.plc)), "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        ''' test if Place is a subclass of BaseModel '''
        self.assertIsInstance(self.plc, Place)

    def testHasAttributes(self):
        ''' verify if attributes exist '''
        self.assertTrue(hasattr(self.plc, 'city_id'))
        self.assertTrue(hasattr(self.plc, 'user_id'))
        self.assertTrue(hasattr(self.plc, 'name'))
        self.assertTrue(hasattr(self.plc, 'description'))
        self.assertTrue(hasattr(self.plc, 'number_rooms'))
        self.assertTrue(hasattr(self.plc, 'number_bathrooms'))
        self.assertTrue(hasattr(self.plc, 'max_guest'))
        self.assertTrue(hasattr(self.plc, 'price_by_night'))
        self.assertTrue(hasattr(self.plc, 'latitude'))
        self.assertTrue(hasattr(self.plc, 'longitude'))
        self.assertTrue(hasattr(self.plc, 'amenity_ids'))
        self.assertTrue(hasattr(self.plc, 'id'))
        self.assertTrue(hasattr(self.plc, 'created_at'))
        self.assertTrue(hasattr(self.plc, 'updated_at'))

    def test_types(self):
        ''' tests if the type of the attribute is the correct one '''
        self.assertIsInstance(self.plc.city_id, str)
        self.assertIsInstance(self.plc.user_id, str)
        self.assertIsInstance(self.plc.name, str)
        self.assertIsInstance(self.plc.description, str)
        self.assertIsInstance(self.plc.number_rooms, int)
        self.assertIsInstance(self.plc.number_bathrooms, int)
        self.assertIsInstance(self.plc.max_guest, int)
        self.assertIsInstance(self.plc.price_by_night, int)
        self.assertIsInstance(self.plc.latitude, float)
        self.assertIsInstance(self.plc.longitude, float)
        self.assertIsInstance(self.plc.amenity_ids, list)
        self.assertIsInstance(self.plc.id, str)
        self.assertIsInstance(self.plc.created_at, datetime.datetime)
        self.assertIsInstance(self.plc.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
