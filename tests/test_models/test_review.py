#!/usr/bin/python3
''' Unittest for review.py '''
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    ''' Tests instances and methods from Review class '''
    rev = Review()

    def test_class_exists(self):
        ''' tests if class exists '''
        result = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.rev)), result)

    def test_user_inheritance(self):
        ''' test if Review is a subclass of BaseModel '''
        self.assertIsInstance(self.rev, Review)

    def testHasAttributes(self):
        ''' verify if attributes exist '''
        self.assertTrue(hasattr(self.rev, 'place_id'))
        self.assertTrue(hasattr(self.rev, 'user_id'))
        self.assertTrue(hasattr(self.rev, 'text'))
        self.assertTrue(hasattr(self.rev, 'id'))
        self.assertTrue(hasattr(self.rev, 'created_at'))
        self.assertTrue(hasattr(self.rev, 'updated_at'))

    def test_types(self):
        ''' tests if the type of the attribute is the correct one '''
        self.assertIsInstance(self.rev.place_id, str)
        self.assertIsInstance(self.rev.user_id, str)
        self.assertIsInstance(self.rev.text, str)
        self.assertIsInstance(self.rev.id, str)
        self.assertIsInstance(self.rev.created_at, datetime.datetime)
        self.assertIsInstance(self.rev.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
