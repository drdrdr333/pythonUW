class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        """
        Initialize object of type Restaurant.
        
        Keyword arguments:
            restaurant_name -> @string
                - name of the instnace of Restaurant
            
            cuisine_type -> @string
                - cuisine speciality offered by the instance of Restaurant
        
        Return: 
            instance of Restaurant
        """

        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        #set to default
        self.number_served = 0
        

    def describe_restaurant(self):
        """
        Description of the restaurant
        
        Keyword arguments:
            None
        Return: 
            @string, a message describing the instance of Restaurant
        """

        return print(f"{self.restaurant_name.title()} has awesome {self.cuisine_type}(s).")
    

    def open_restaurant(self):
        """
        Tells if the restaurant is open
        
        Keyword arguments:
            None
        Return: 
            @string, a message saying the instance of the restaurant is open
        """
        return print(f"Welcome, {self.restaurant_name.title()} is open!!")


    def set_number_served(self, number_of_ppl_served: int):
        """
        Sets the instance attribute number_served to an argument supplied to the function
        
        Keyword arguments:
            number_of_ppl_served -> @int
                number informing the function of how many people were served
        Return: 
            None, simply updated the instance attribute
        """
        if not isinstance(number_of_ppl_served, int):
            raise TypeError("Please provide a number! You'll need to run this again with a number. Thank you!")
        else:
            self.number_served = number_of_ppl_served
            return None
        
    

    def increment_number_served(self, people_to_add: int):
        """
        Adds to the instance attribute number_served a specified amount
        
        Keyword arguments:
            people_to_add -> @int
                number of people to add to the current amount of people served
        Return: 
            calls the print_people_served() method to print the newly updated instances number_served attribute
        """
        if not isinstance(people_to_add, int):
            raise TypeError("Please provide a number! You'll need to run this again with a number. Thank you!")
        else:
            self.number_served += people_to_add
            return self.print_num_served()
        

    def print_num_served(self):
        """
        Prints the instance attribute number_served
        
        Keyword arguments:
            None
        Return: 
            prints a string to the console
        """
        return print(f"Current Number of people served by {self.restaurant_name}:\t {self.number_served}")

    
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name: str, cuisine_type="ice cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    
    def add_flavors(self, *flavors):
        """
        Adds flavors, as a @string type, to the instance attribute flavors
        
        Keyword arguments:
            *flavors -> @string
                flavors of ice cream specialized in for the ice cream shop, accepts as many flavors as desired
        Return: 
            prints a message describing the flavors of ice cream added
        """
        for i in flavors:
            print(f"Adding {i.title()} to your shop's flavor menu!")
            self.flavors.append(i.title())
        return None
    

    def show_flavors(self):
        """
        Prints all instance flavors
        
        Keyword arguments:
            None
        Return: 
            prints a string to the console containing the instances flavors
        """
        msg = f"The Flavor Menu - Take Your Pick!!:\n---------------------------------\n"

        for num,flavor in enumerate(self.flavors):
            msg += f"\t{num+1}. {flavor}\n"
        return print(msg)