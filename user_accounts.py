import random
import string
import pyperclip

class userAccounts:
    '''
    Class that stores user accounts and credentials
    '''
    accounts = []

    def __init__(self, platform, username, password):
        '''
        this function allows users to store their various account details
            Args: platform,username,password
        '''
        self.platform = platform
        self.username = username
        self.password = password

    def add_account(self):
        '''
        this function adds accounts to the accounts list
        '''
        self.accounts.append(self)

    def random_password(length, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(length))
