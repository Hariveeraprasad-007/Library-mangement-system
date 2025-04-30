class UserManager:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.users={}
    def register(self, username, password):
        if username in self.users:
            print("The username already exists.")
        else:
            self.users[username] = User(username, password)
            print("Registration successful!")
    def login(self, username, password):
        if username in self.users and self.users[username].password == password:
            print("You have logged in successfully.")
            return self.users[username]
        else:
            print("Invalid username or password. Check if you have registered.")
            return None