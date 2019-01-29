#!/usr/bin/env python3.6
import os
os.system('setterm -background cyan -foreground black -store')
from credential import Credential

def create_credential(app,fname,lname,phone,email):

    '''
    Function to create a new credential
    '''
    new_credential = Credential(app,fname,lname,phone,email)
    return new_credential

def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def find_credential(number):
    '''
    Function that finds a credential by number and returns the credential
    '''
    return Credential.find_by_number(number)

def check_existing_credentials(number):
    '''
    Function that check if a credential exists with that number and return a Boolean
    '''
    return Credential.credential_exist(number)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()

def copy_email(email):
        '''
        Function that handles the behaviour of copy the email to the clipboard
        '''
        return Credential.copy_email(email)

def main():
        print("Hello Welcome to your Password Locker. What is your name?")
        user_name = input()

        print(f"Hello {user_name}. what would you like to do?")
        print('\n')

        while True:
                print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, ex -exit the credential list ")

                short_code = input().lower()

                if short_code == 'cc':
                        print("New Application")
                        app = input()

                        print ("First name ....")
                        f_name = input()

                        print("Last name ...")
                        l_name = input()

                        print("Phone number ...")
                        p_number = input()

                        print("Email address ...")
                        e_address = input()


                        save_credentials(create_credential(app,f_name,l_name,p_number,e_address)) # create and save new credential.
                        print ('\n')
                        print(f"New Credential {app} {f_name} {l_name} created")
                        print ('\n')

                elif short_code == 'dc':

                        if display_credentials():
                                print("Here is a list of all your credentials")
                                print('\n')

                                for credential in display_credentials():
                                        print(f"{credential.first_name} {credential.last_name} .....{credential.phone_number}")

                                print('\n')
                        else:
                                print('\n')
                                print("You dont seem to have any credentials saved yet")
                                print('\n')

                elif short_code == 'fc':

                        print("Enter the number you want to search for")

                        search_number = input()
                        if check_existing_credentials(search_number):
                                search_credential = find_credential(search_number)
                                print(f"{search_credential.first_name} {search_credential.last_name}")
                                print('-' * 20)

                                print(f"Phone number.......{search_credential.phone_number}")
                                print(f"Email address.......{search_credential.email}")
                        else:
                                print("That credential does not exist")

                # elif short_code == 'del':
                        
                #         print("Enter the number you want to delete")
                        
                #         search_number = input()
                #         if delete_credential(search_number):
                #                 search_credential = find_credential(search)
                #                 print("Are you sure you want to delete this number")
                #                 print('\n')

                #                 for credential in delete_credential():
                #                         delete_credential(display_credential(f_name,l_name,p_number,e_address))

                #                 print('\n')
                #         else:
                #                 print('\n')
                #                 print("You dont seem to have that credential")
                #                 print('\n')

                elif short_code == "ex":
                        print("Bye .......")
                        break
                else:
                        print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()