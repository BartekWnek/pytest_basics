import pytest
from restaurant import Restaurant
from waiter import Waiter
from bill import Bill
from manager import Manager
from product import Product
from setup_restaurant import setup_restaurant
from employee import no_such_table

def test_remove_from_bil(setup_restaurant):
    restaurant, manager, waiter, soup, drink, main = setup_restaurant
    waiter.open_bill(table_num = 1,food = main, waiter = waiter)
    waiter.open_bill(table_num = 1, food = drink, waiter = waiter)
    waiter.open_bill(table_num = 1, food = soup, waiter = waiter)
    manager.remove_from_bill(table = 1, food = main)
    assert restaurant.tables[0].food_list[0].name == "Drink" 
    assert restaurant.tables[0].food_list[1].name == "Soup"