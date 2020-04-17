import unittest
import os

class UnitTests(unittest.TestCase):

    def test_getUser_from_env(self):
        user_login =  os.getenv('GOOGLE_USERNAME')
        assert user_login is not None

    def test_getPass_from_env(self):
        user_password =  os.getenv('PASSWORD')
        assert user_password is not None

    def test_getUrl_from_env(self):
        link =  os.getenv('URL')
        assert link is not None

if __name__ == '__main__':
    unittest.main()
