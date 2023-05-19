class User:
    def __init__(self, user_type, username, password,email):
        self.user_type = user_type
        self.username = username
        self.password=password
        self.email = email
    
    def register(self):
        self.user_type = input("Enter user type (seller or customer): ")
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        self.email = input("Enter email: ")

        new_user = User(self.user_type,self.username, self.password, self.email)
        return new_user
    
    def login(self):
        username_input = input("Enter username: ")
        password_input = input("Enter password: ")
        
        if username_input == self.username and password_input == self.password:
            print("Login was successful!")
        else:
            print("Invalid username or password.")