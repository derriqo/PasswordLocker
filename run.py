#!/usr/bin/env python3.6
from credential import Credential
from user import User

def create_user(user_name,password):
	'''
	Function to create a new user account
	'''
	new_user = User(user_name,password)
	return new_user
def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)

def verify_user(user_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = User.check_user(user_name,password)
	return checking_user


def create_credential(username,appname,app_username,app_password):

        '''
        Function to create a new credential
        '''
        new_credential = Credential(username,appname,app_username,app_password)
        return new_credential

def save_credentials(credential):
        '''
        Function to save credential
        '''
        Credential.save_credential(credential)

def del_credential(credential):
        '''
        Function to delete a credential
        '''
        credential.delete_credential()

def find_credential(appname):
        '''
        Function that finds a credential by number and returns the credential
        '''
        return Credential.find_by_appname(appname)

def check_existing_credentials(appname):
        '''
        Function that check if a credential exists with that number and return a Boolean
        '''
        return Credential.credential_exist(appname)

def display_credentials():
        '''
        Function that returns all the saved credentials
        '''
        return Credential.display_credentials()
def generate_password():
        '''
        Function to generate password
        '''    
        return Credential.generate_password()    

def main():
        print('')
        print("Hello Welcome to your Password Locker.")

        while True:
                print(' ')
                print("-"*60)
                print('Use these short codes to navigate:\n ca-Create an Account \n li-Log In \n ex-Exit')
                print('\n')
                short_code = input('Enter a choice: ').lower().strip()
                if short_code == 'ex':
                        print("Don't forget to add new credentials")
                        print('\n')
                        break

                elif short_code == 'ca':
                        print("-"*60)
                        print(' ')
                        print('To create a new account:')
                        user_name = input('Enter your user name - ').strip()
                        password = input('Enter your password - ').strip()
                        save_user(create_user(user_name,password))
                        print(" ")
                        print(f'New Account Created for: {user_name} using password: {password}')
                elif short_code == 'li':
                        print("-"*60)
                        print(' ')
                        print('To login, enter your account details:')
                        user_name = input('Enter your user name - ').strip()
                        password = str(input('Enter your password - '))
                        print('\n')
                        user_exists = verify_user(user_name,password)
                        if user_exists == user_name:
                                print(" ")
                                print(f'Welcome {user_name}. Please choose an option to continue.')
                                print(' ')

                                while True:
                                        print("Use these short codes \n cc - create a new credential \n dc - display credentials \n fc -find a credential \n ex -exit the credential list ")

                                        short_code = input().lower()

                                        if short_code == 'cc':
                                                print("Application Name")
                                                app = input()

                                                print ("Enter username for this app ....")
                                                auname = input()

                                                print("Do you want to autogenerate password for this application? If yes, enter 'y' else enter 'n'")
                                                while True:
                                                        answer = input().lower().strip()
                                                        if answer == 'y':
                                                                appass = generate_password()
                                                                break   
                                                        elif answer== 'n':
                                                                print("Enter password for this app ...")
                                                                appass = input()
                                                                
                                                                break
                                                        else:
                                                                print("please choose again")        
                                               

                                                save_credentials(create_credential(user_name,app,auname,appass)) # create and save new credential.
                                                print ('\n')
                                                print(f"New Credential for {app} with username: {auname} and password:{appass} has been created")
                                                print ('\n')

                                        elif short_code == 'dc':

                                                if display_credentials():
                                                        print("Here is a list of all your credentials")
                                                        print('\n')
                                                        credential_list = display_credentials()
                                                        for credential in credential_list:
                                                                print(f"app name:{credential.app_name} username: {credential.app_username} password: {credential.app_password}")

                                                        print('\n')
                                                else:
                                                        print('\n')
                                                        print("You dont seem to have any credentials saved yet")
                                                        print('\n')

                                        elif short_code == 'fc':

                                                print("Enter the app name whose credentials you want to see")

                                                appname = input()
                                                if check_existing_credentials(appname):
                                                        credential = find_credential(appname)
                                                        print(f"Credentials for {appname} are:")
                                                        
                                                        print('\n')
                                                        print(f"USERNAME: {credential.app_username} PASSWORD: {credential.app_password}")
                                                        print('-' * 20)
                                                        print('\n')

                                                else:
                                                        print("The credential for this app does not exist")
                                        elif short_code == "ex":
                                                print("Bye .......")
                                                break
                                        else:
                                                print("I really didn't get that. Please use the short codes")
                        else:
                                print("This user doesnot exist. Please either create an account using 'ca' or exit using 'ex' ")     

                
                
                else:
                        print("I really didn't get that. Please use the short codes")                                        

if __name__ == '__main__':

    main()