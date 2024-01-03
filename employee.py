class no_such_table(Exception):
    pass # if an Employee wants to create a bill on a table that doesn't exist

class Employee:
    
    def __init__(self, name, my_restaurant):
        self.name = name
        self.my_restaurant = my_restaurant
