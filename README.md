# PASSWORD LOCKER


# Table of contents
***
* [General Info](#General-Info)
* [Technologies](#Technologies)
* [Setup](#Setup)
* [Behaviour Driven Technologies](#Behaviour-Driven-Technologies)
* [Support](#Support)
* [Bugs](#Bugs)
* [Creator](#Creator)
* [License](#License)

## General info
---
PasswordLocker as the name suggests is an application that enables users to manage their individual passwords and furthermore generates new passwords for them.

The application allows the user to:

* Create a password locker account with their details, a login username and a password.

* Store already existing account credentials in the application .

* Create new account credentials in the application .

* Have the option of putting in a password that they want to use for the new credential account.

* Auto generate their password using the application.

* To view various account credentials and their password in the application.

* Delete a credentials account that they no longer need.


## Technologies
---
Project is created with:
* Python 3.6
* Prerequisites:   *Pip ,Pyperclip*


## Setup
---
To run this project, please follow the following instructions.
-   Get access to the internet
-   Sign into your github pages. Set up would require access to github pages; the webpage uses an index file linked on github pages. This would require membership and access to the **derriqo** repository.
-   Search for derriqo on the github pages and select the Password-Locker repository.
-   Clone the repository.

### Cloning
---
* In your terminal:
        
        $ git clone https://github.com/derriqo/Password-Locker/
        $ cd Password-Locker

## Running the Application
---
* To run the application, in your terminal:

        $ chmod +x run.py
        $ ./run.py
        
## Testing the Application
---
* To run the tests for the class file:

        $ python3.6 credentials_test.py
        

## Behaviour Driven Development
---

**User Story**
As a user i want to be able to store my account credentials and their various passwords and also  be able to delete them.

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Welcomes user to the applicatin | **In terminal: $./run.py** | Hello, Welcome to Password Locker. What is your name? |
| Display codes for navigation | **In terminal: User enters Name** | Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, ex -exit the credential list  |
| Display prompt for creating account | **Enter: cc** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
| Display prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Exit application | **Enter: ex** | Exit the current navigation stage |


## Support and contact details
---
For any inquiries, please reach out to derrick.william24@yahoo.com

## Bugs
---
None at the moment, but would love to hear your feedback!

## Creator
---

Created by Derrick William. 
