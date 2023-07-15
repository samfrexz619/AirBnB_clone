#!/usr/bin/python3
'''Test Class User'''

from models.user import User
import datetime
import unittest
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    '''Tes class User'''
    my_usr = User()
    my_usr.name = "Betty"

    def test_checking_for_docstring_User(self):
        '''Test for docstring'''
        self.assertIsNotNone(User.__doc__)

    def test_subclass_instance_User(self):
        '''Test my_model 1 and 2 are subclasses of BaseModel'''
        self.assertTrue(isinstance(self.my_usr, User))

    def test_attribute_email(self):
        '''Tests email'''
        self.assertTrue(hasattr(self.my_usr, 'email'))

    def test_attribute_password(self):
        '''Test password'''
        self.assertTrue(hasattr(self.my_usr, 'password'))

    def test_attribute_first_name(self):
        '''check first name'''
        self.assertTrue(hasattr(self.my_usr, 'first_name'))

    def test_attribute_last_name(self):
        '''check last'''
        self.assertTrue(hasattr(self.my_usr, 'last_name'))

    def test_hasattr(self):
        '''attrs inherited of BaseModel'''
        self.assertTrue(hasattr(self.my_usr, 'name'))
        self.assertTrue(hasattr(self.my_usr, 'id'))
        self.assertTrue(hasattr(self.my_usr, 'created_at'))
        self.assertTrue(hasattr(self.my_usr, 'updated_at'))

    def test_attributes_types(self):
        '''Test types'''
        self.assertEqual(type(self.my_usr.email), str)
        self.assertEqual(type(self.my_usr.last_name), str)
        self.assertEqual(type(self.my_usr.first_name), str)
        self.assertEqual(type(self.my_usr.password), str)
        self.assertIsInstance(self.my_usr.created_at, datetime.datetime)
        self.assertIsInstance(self.my_usr.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
