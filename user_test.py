import unittest # Importing the unittest module
from user import User # Importing the user class
import pyperclip

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_user = User("Derrick","moringa") # create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Derrick")
        self.assertEqual(self.new_user.password,"moringa")   

    def test_save_user(self):
        '''
        test_save_user to test if the user object is saved into the user list .
        '''

if __name__=='__main__':
    unittest.main()