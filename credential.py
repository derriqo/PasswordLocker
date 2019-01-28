class Credential:   
    """
    Class that generates new instances of credentials.
    """

    credential_list = [] # Empty credential list

    def __init__(self,app_name,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.app_name = app_name
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email

    credential_list = [] # Empty credential list
 # Init method up here
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
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a credential that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Credential of person that matches the number.
        '''

        for credential in cls.credential_list:
            if credential.phone_number == number:
                return credential
    
    @classmethod
    def credential_exist(cls,number):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.phone_number == number:
                return True

        return False
    
    @classmethod
    def credential_exist(cls,number):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.phone_number == number:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list

#     @classmethod
#     def copy_email(cls,number):
#         credential_found = Credential.find_by_number(number)
#         pyperclip.copy(credential_found.email)