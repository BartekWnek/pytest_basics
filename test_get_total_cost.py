import pytest
from restaurant import Restaurant
from waiter import Waiter
from bill import Bill
from manager import Manager
from product import Product
from setup_restaurant import setup_restaurant
from employee import no_such_table

def test_get_total_cost(setup_restaurant):
    restaurant, manager, waiter, soup, drink, main = setup_restaurant
    waiter.open_bill(table_num=2,food=soup,waiter = waiter)
    waiter.open_bill(table_num=2,food=soup,waiter = waiter)
    assert waiter.my_bills[0].get_total_cost() == 40
