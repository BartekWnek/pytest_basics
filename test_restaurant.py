import pytest
from restaurant import Restaurant
from waiter import Waiter
from bill import Bill
from manager import Manager
from product import Product
from setup_restaurant import setup_restaurant
from employee import no_such_table

def test_restaurant(setup_restaurant):
    restaurant, manager, waiter, soup, drink, main = setup_restaurant
    assert restaurant.tables == [None,None,None,None,None]