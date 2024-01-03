import pytest
from restaurant import Restaurant
from waiter import Waiter
from bill import Bill
from manager import Manager
from product import Product
from setup_restaurant import setup_restaurant
from employee import no_such_table

def test_get_waiters(setup_restaurant):
    restaurant, manager, waiter, soup, drink, main=setup_restaurant
    waiter2=manager.add_waiter('Robb Stark', manager)
    assert waiter2.name == 'Robb Stark'
    assert manager.get_waiters() == ['Jon Snow', 'Robb Stark']
    