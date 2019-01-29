class User:

  """ 
  Class that generates new instances of users.
  """

user_list = [] # Empty user list

def __init__(self,user_name,password):

      # docstring removed for simplicity

        self.user_name = user_name
        self.password = password

  user_list = [] # Empty contact list
 # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

    
        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)
    
    
