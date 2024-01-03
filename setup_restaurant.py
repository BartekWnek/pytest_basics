import pytest
from restaurant import Restaurant
from manager import Manager
from product import Product

@pytest.fixture
def setup_restaurant():
    restaurant = Restaurant(restaurant_name='Winterfell', num_of_tables=5)
    manager = Manager(name='Eddard Stark', my_restaurant=restaurant)
    waiter = manager.add_waiter(name='Jon Snow', manager=manager)
    soup = Product(name='Soup', price=20)
    drink = Product(name='Drink', price=10)
    main = Product(name='Main', price=30)
    return restaurant, manager, waiter, soup, drink, main
    