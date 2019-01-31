import random
class Credential:   
    """
    Class that generates new instances of credentials.
    """

    credential_list = [] # Empty credential list
    
    def __init__(self,user_name,app_name,app_username,app_password):
        '''
        Test init test case to test if the object is instantiated correctly
        '''
      
        self.user_name = user_name
        self.app_name = app_name
        self.app_username = app_username
        self.app_password = app_password
       

        credential_list = [] # Empty credential list


    def save_credential(self):

        '''
        save_credential method saves credential objects into credential_list
        '''

    
        Credential.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)
    
    @classmethod
    def find_by_appname(cls,appname):
        '''
        Method that takes in a appname and returns a credential that matches that appname.

        Args:
            appname: Phone appname to search for
        Returns :
            Credential of person that matches the appname.
        '''

        for credential in cls.credential_list:
            if credential.app_name == appname:
                return credential
    
    @classmethod
    def credential_exist(cls,appname):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            appname: Phone appname to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.app_name == appname:
                return True

        return False

    def generate_password(self):
        char="ABCDEFGHIJKLMNOPQRSTUVWXYXabcdefghijklmnopqrstuvwxyx1234567890"
        password =""
        for i in range(8):
            password+=random.choice(char)
        return password    


    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list


    