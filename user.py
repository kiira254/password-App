class User:
    '''
    Class that allows the users to create their login details
    '''
    user_info = []
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def save_user_info(self):
        '''
        function that appends user login info
        '''
        self.user_info.append(self)

    