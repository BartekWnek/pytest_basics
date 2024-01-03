from employee import Employee
from waiter import Waiter

class Manager(Employee):
    
    def __init__(self, name, my_restaurant):
        super().__init__(name, my_restaurant)
        self.all_bills = [] #Manager has access to all_bills in the restaurant
        self.all_waiters = [] #Manager has access to all waiters working in restaurant
        self.total_earnings = 0 #Manager can chesk total earnings (from closed bills)

    def add_waiter(self, name, manager):
        new_waiter = Waiter(name, self.my_restaurant, manager)
        self.all_waiters.append(new_waiter)
        return new_waiter

    def get_waiters(self):
        waiters_names = [waiter.name for waiter in self.all_waiters]
        return waiters_names
    
    def get_all_bills(self):
        raport = [(f'Table: {bill.table_num}', f'Value: {bill.get_total_cost()}') for bill in self.all_bills]
        return raport

    def get_total_earnings(self):
        for waiter in self.all_waiters:
            self.total_earnings = self.total_earnings+waiter.days_earnings
        return self.total_earnings

    def remove_from_bill(self, table, food):
        self.my_restaurant.tables[table-1].food_list.remove(food)
    