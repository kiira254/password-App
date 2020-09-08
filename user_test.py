import unittest
from user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        '''
        Set method to run before test classes
        '''
        self.new_user = User('Nelly', 'Kamotho', 'Nelly254', 'admin')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_info =[]

    def test_init(self):
        '''
        function to test for initialization of variables
        '''
        self.assertEqual(self.new_user.first_name, 'Nelly')
        self.assertEqual(self.new_user.last_name, 'Kamotho')
        self.assertEqual(self.new_user.username, 'Nelly254')
        self.assertEqual(self.new_user.password, 'admin')
    
    def test_save_user_info(self):
        '''
        Function that checks if user credentials are being saved
        '''
        User.save_user_info(self.new_user)
        self.assertEqual(len(User.user_info),1)
    def test_save_multiple_user(self):
        '''
        to check saving multiple users to our user_list is possible
        '''
        self.new_user.save_user_info()
        self.assertEqual(len(User.user_info),1)
    def test_user_exists(self):
        '''
        a test function that returns true or false to check if a certain user exists
        '''
        self.new_user.save_user_info()
        test_user = User("Test","user","6656","nyangoma.odera@gmail.com")
        test_user.save_user_info()

        user_exists = User.user_exists("6656")

        self.assertTrue(user_exists)

    def test_get_user_info(self):
        '''
        function that allows the user to view their account details
        '''
        User.save_user_info(self.new_user)
        self.assertEqual(User.get_user_info('Nellyke254'),self.new_user)

    def test_user_login(self):
        User.save_user_info(self.new_user)
        self.assertTrue(User.user_login('Nellyke254','admin'))

    def test_delete_user_info(self):
        '''
        to test if we can remove user from our list
        '''
        self.new_user.save_user_info()
        self.new_user.delete_user_info() # Delete user
        self.assertEqual(len(User.user_info),1)

if __name__ == '__main__':
    unittest.main()
