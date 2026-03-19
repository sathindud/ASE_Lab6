import pytest
from models.cart import Cart
from models.catalog import Catalog
from models.product import Product

@pytest.fixture
def catalog():
    cat = Catalog()
    cat.add(Product("P1", "Pen", 2.0))
    cat.add(Product("P2", "Laptop", 1000.0))
    return cat

def test_bulk_discount(catalog):
    # >= 10 items of single SKU = 10% off that line
    cart = Cart(catalog)
    cart.add_item("P1", 10) # 10 * 2.0 = 20.0. 10% off = 18.0
    assert cart.total() == 18.0

def test_order_discount(catalog):
    # Total >= 1000 = 5% off entire subtotal
    cart = Cart(catalog)
    cart.add_item("P2", 1) # 1000. 5% off = 950.0
    assert cart.total() == 950.0