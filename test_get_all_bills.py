import pytest

from restaurant import Restaurant
from waiter import Waiter
from bill import Bill
from manager import Manager
from product import Product
from setup_restaurant import setup_restaurant
from employee import no_such_table

def test_get_all_bills(setup_restaurant):
    restaurant, manager, waiter, soup, drink, main = setup_restaurant
    waiter2 = manager.add_waiter('Robb Stark',manager = manager)
    waiter.open_bill(table_num=4, food=main, waiter=waiter)
    waiter.open_bill(table_num=3, food=drink, waiter=waiter2)
    assert manager.get_all_bills()==[('Table: 4', 'Value: 30'), ('Table: 3', 'Value: 10')]