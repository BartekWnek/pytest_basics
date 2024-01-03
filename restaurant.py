class Restaurant:
    '''Additional class that contain list representing tables at the restaurant, where each can contain one bill or None value'''
    def __init__(self, restaurant_name, num_of_tables):
        self.restaurant_name = restaurant_name
        self.tables = []
        for i in range(1, num_of_tables+1):
            self.tables.append(None)
            