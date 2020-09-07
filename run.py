from user import User
import pyperclip
from user_accounts import userAccounts

def new_user_account():
    print('Create New user account')
    usr_firstname = input('Enter First Name: ')
    usr_lastname = input('Enter Last Name: ')
    usr_username = input('Enter Username: ')
    if(User.user_exists(usr_username)):
        print('User already exists')
        new_user_account()
    else:
        usr_password = input('Type your login password: ')
        usr_password1 = input('Confirm your login password: ')
        if usr_password == usr_password1:
            new_User = User(usr_firstname, usr_lastname,usr_username, usr_password)
            User.save_user_info(new_User)
            print(f'{usr_firstname} added as user\n---------')
            login_account()
def login_account():
    print("-------Login-------")
    exists = User.user_login(input('Enter Username: '),input('Enter Password: '))
    if(exists !=True):
        print('Check your password!')
    else:
        acc_short_code = input('Hello, if you want to add an existing platform acccount, type EX. If you want to generate new account details, type NW').lower()
        if(acc_short_code == 'nw'):
            reg_new_platform()
        elif acc_short_code =='ex':
            reg_existing_platform()
        else:
            print('Invalid Option')
            login_account()