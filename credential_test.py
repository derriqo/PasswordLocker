import unittest # Importing the unittest module
from credential import Credential # Importing the credential class
# from user import User #Importing the user class
import pyperclip

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
        # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("Facebook","James","Muriuki","0712345678","james@ms.com") # create credential object
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.app_name,"Facebook")
        self.assertEqual(self.new_credential.first_name,"James")
        self.assertEqual(self.new_credential.last_name,"Muriuki")
        self.assertEqual(self.new_credential.phone_number,"0712345678")
        self.assertEqual(self.new_credential.email,"james@ms.com")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)

    # setup and class creation up here

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []
    
    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("App","Test","user","0712345678","test@user.com") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credential from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("App","Test","user","0712345678","test@user.com") # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a credential object
            self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential_by_number(self):
        '''
        test to check if we can find a credential by phone number and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("App","Test","user","0711223344","test@user.com") # new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_number("0711223344")

        self.assertEqual(found_credential.email,test_credential.email)
    
    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("App","Test","user","0711223344","test@user.com") # new credential
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("0711223344")

        self.assertTrue(credential_exists)
    
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)

        
if __name__== '__main__':
    unittest.main()