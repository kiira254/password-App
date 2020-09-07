import unittest
from user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User('cephas', 'too', 'cephaske254', 'admin', 'admin')
