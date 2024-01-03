class Bill:
    '''Bill which is connected to the table in restaurant'''
    
    def __init__(self, table_num, product, waiter):
        self.table_num = table_num
        self.food_list = [product]
        self.waiter = waiter
    
    def add_food(self, product):
        self.food_list.append(product)

    def get_total_cost(self):
        price_list = [food.price for food in self.food_list]
        total_price = sum(price_list)
        return(total_price)
    
    def get_all_food(self):
        name_list = [food.name for food in self.food_list]
        return(name_list)
    
    def get_waiter_name(self):
        return self.waiter.name
    
