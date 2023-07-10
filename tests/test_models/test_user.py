#!/usr/bin/python3
''' '''
import unittest
from models.user import User
import datetime


class UserCase(unittest.TestCase):
    ''' '''
    my_user = User()

    def test_class_exists(self):
        ''' '''
        self.assertEqual(str(type(self.my_user)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        ''' '''
        self.assertIsInstance(self.my_user, User)

    def test_has_attributes(self):
        ''' '''
        self.assertTrue(hasattr(self.my_user, 'email'))
        self.assertTrue(hasattr(self.my_user, 'password'))
        self.assertTrue(hasattr(self.my_user, 'first_name'))
        self.assertTrue(hasattr(self.my_user, 'last_name'))
        self.assertTrue(hasattr(self.my_user, 'id'))
        self.assertTrue(hasattr(self.my_user, 'created_at'))
        self.assertTrue(hasattr(self.my_user, 'updated_at'))

    def test_types(self):
        ''' '''
        self.assertIsInstance(self.my_user.first_name, str)
        self.assertIsInstance(self.my_user.last_name, str)
        self.assertIsInstance(self.my_user.email, str)
        self.assertIsInstance(self.my_user.password, str)
        self.assertIsInstance(self.my_user.id, str)
        self.assertIsInstance(self.my_user.created_at, datetime.datetime)
        self.assertIsInstance(self.my_user.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
