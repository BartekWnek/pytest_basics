import pytest
from restaurant import Restaurant
from waiter import Waiter
from bill import Bill
from manager import Manager
from product import Product
from setup_restaurant import setup_restaurant
from employee import no_such_table

def test_bill_get_waiter_name(setup_restaurant):
    restaurant, manager, waiter, soup, drink, main = setup_restaurant
    waiter.open_bill(table_num = 2, food = soup, waiter = waiter)
    assert waiter.my_bills[0].get_waiter_name() == 'Jon Snow'
