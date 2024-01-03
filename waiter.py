from employee import Employee
from employee import no_such_table
from bill import Bill
from restaurant import Restaurant
from product import Product

class Waiter(Employee):
    def __init__(self, name, my_restaurant, manager):
        super().__init__(name, my_restaurant)
        self.num_of_bills = 0 
        self.days_earnings = 0 
        self.my_bills = [] 
        self.manager = manager
    #Only waiter can open or close new bills (manager does not serve tables)
    def open_bill(self, table_num, food, waiter):
        if table_num in range(1,len(self.my_restaurant.tables)+1):
            if self.my_restaurant.tables[table_num-1] == None: #checking if there is already bill at the table if no: creating new
                new_bill = Bill(table_num,food,waiter)
                self.my_restaurant.tables[table_num-1] = new_bill
                self.my_bills.append(new_bill)
                self.manager.all_bills.append(new_bill)
            else: # if there is a bill at such table, you can add more food 
                self.my_restaurant.tables[table_num-1].add_food(food)
        else:
            raise(no_such_table) 

    def close_bill(self, table_num): 
        table_num = table_num
        if table_num in range(1,len(self.my_restaurant.tables)):
            if self.my_restaurant.tables[table_num-1] != None:
                self.days_earnings = self.days_earnings+self.my_restaurant.tables[table_num-1].get_total_cost()
                self.my_restaurant.tables[table_num-1] = None
            else:
                print('There is no bill at this table')
        else:
            raise(no_such_table)
    
    def get_bills(self): #only open bills
        for bill in self.my_bills:
            print(f'Table number: {bill.table_num}, value of order: {bill.get_total_cost()}')
        

