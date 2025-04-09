class User:

    #For contacting the owner and establishing relationships
    system_email = "owner@system.com"

    def __init__(self, first_name: str, last_name: str, email: str, location: str):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email.title()
        self.location = location.title()
        self.login_attempts = 0

    
    def describe_user(self):
        """
        Displays user profile information

        Keyword arguments:
            None
        Return: 
            @string, display of user profile info.
        """
        info = f"User Profile Info. for {self.first_name} {self.last_name}:\n---------------------------------------\n First Name:\t {self.first_name}\n Last Name:\t {self.last_name}\n Email:\t {self.email}\n Location:\t {self.location}"
        return print(info)


    def greet_user(self):
        """
        Prints a greeting message
        Keyword arguments:
            None
        Return: 
            prints a string to the console
        """
        
        return print(f"Hello, {self.first_name}! Thank you for signing up. If you'd like to connect, reach out to {User.system_email}. Thanks and have a great day!")
    

    def increment_login_attempts(self):
        """
        Adds 1 login attempt to the instance attriute login_attempts
        
        Keyword arguments:
            None
        Return: 
            prints a message to the console telling the user how many login attempts have currently been used
        """
        self.login_attempts += 1
        return print(f"You have attempted a login.\n Total Login Attempts: {self.login_attempts}")
    

    def reset_login_attempts(self):
        """
        Resets the instance attribute login attempts back to 0
        
        Keyword arguments:
            None
        Return: 
            prints a message to the console describing that the login attempts have been reset to 0
        """

        self.login_attempts = 0
        return print(f"Login attempts have been reset.\n Total Login Attempts: {self.login_attempts}")
        

class Admin(User):
    
    
    available_privileges = {'r': "Allows read access to items", 'w': "Allows write access to items", '+': "Allows super user privileges, to both read and write items."}


    def __init__(self, first_name: str, last_name: str, email: str, location: str):
        super().__init__(first_name, last_name, email, location)
        self.privileges = []


    def show_options_for_privileges(self):
        """
        Prints a message to the console of availabale Admin privileges
        
        Keyword arguments:
            None
        Return: 
            prints a message to the console
        """
        
        msg = f"Here are your options:\n-------------------------------\n"
        i = 1
        for key,val in Admin.available_privileges.items():
            msg += f"{i}. '{key}' = {val}\n"
            i+=1
        return msg


    def add_privileges(self, *priveleges_to_add):
        """
        Allows the user to see the options available for privileges
        If the desired privilege does not exist, it will be excluded
        Adds the privileges that are avaialabe to the class Admin, to the instance privileges of the Admin
        
        Keyword arguments:
            *privileges -> @string
                desired privileges to add to the instance admin privileges attributs
        Return: 
            call to show_priviligest() method
        """
        print(Admin.show_options_for_privileges(self))
        
        while True:
            for item in [*priveleges_to_add]:
                if item in Admin.available_privileges.keys():
                    print(f"Adding privilege {item} which does the following: {Admin.available_privileges[item]}")
                    self.privileges.append({f"{item}": f"{Admin.available_privileges[item]}"})
                else:
                    print(f"{item} is not an avaliable privilege for administrators... not being added.")
            break
        return self.show_privileges()
    

    def show_privileges(self):
        msg = f"User {self.first_name} {self.last_name} has the following priviliges:\n--------------------------------------------------\n"

        for num,priv in enumerate(self.privileges):
            for key,val in priv.items():
                msg += f"{num+1}. {key} - {val}\n"
        return print(msg)


# u = User("Mally", "Grace", "m@email.com", "111 Location Drive")

# u.describe_user()
# u.greet_user()

# u.increment_login_attempts()
# u.increment_login_attempts()
# u.reset_login_attempts()
# u.increment_login_attempts()
# u.increment_login_attempts()

a = Admin("tater","tot","t@t.com","buzzville")
a.add_privileges("r", "test", "test2", "+")