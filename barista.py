import csv

class Barista:
    """A representation of the program login, or create a new user & password.
    Attributes: Username(string)
    Functions: verify_account(username), authenticate (password)
    """
        #initialize constructor for class Barista
    def __init__(self):

        self.user_log = {}
        while True:
            try:
                self.username = input("Enter your username: ") #takes in username attribute as input(0)
            except NameError:
                print('Please enter characters only')
                continue
            else:
                break
                
        self.verify_account(self.username)  # checks for username input against username entries in user_log.csv
        # checks for password input against password entries in user_log.csv
        self.authenticate()
        #verify that user_name is present in CSV file
        
        
    def verify_account(self, username):
        with open('user_log.csv', 'r') as csvfile: #open user_log.csv
            csv_reader = csv.DictReader(csvfile)
            #iterate over column [0] and column [1] in csvfile
            for row in csv_reader:
                self.user_log.update({row['username']:row['password']})   #update self.userlog with key values from csv_reader
                #defining username and password

        if username in self.user_log.keys():  #searches for username input in column[0]
            print("User found!")
        else:
            # use csvDictWrite to create a new user name and write it as a new row in user_log.csv
            print("User not found. Let's create one for you")
            headers = ['username', 'password']
            with open ('user_log.csv', 'a',newline='') as csvfile:
                csv_writer = csv.DictWriter(csvfile, fieldnames = headers) #define positional arguments
                username = input("Type a username you wish to use: ")
                password =  input("Type a password for this account: ")
                
                # Write to file
                csv_writer.writerow({'username': username, 'password': password})
                # update user log
                self.user_log.update({username: password})
            print("Please re-enter password to log in!")

    #checks password against the password in the user_log.csv file
    def authenticate(self):
        verify_password = False
        #user enters "y for another attept to enter password"
        option = 'y'
        while option == 'y' and verify_password is False:
            print("")
            password = input("Enter your password: ")
            print("")
            #Lets verify the password
            for key, val in self.user_log.items():
                print(key, val)
                if key == self.username:
                    if password == val:
                        print("")
                        print('       You are logged in! \n   Now lets make some coffee!')
                        print("")
                        verify_password = True
                    else:
                        print("Incorrect Password")
                        print("")
                        option = input("Enter 'y' to try again or hit any other key to exit: ")
