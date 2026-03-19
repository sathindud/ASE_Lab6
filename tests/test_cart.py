import pytest
from models.catalog import Catalog
from models.product import Product
from models.cart import Cart

@pytest.fixture
def catalog():
    cat = Catalog()
    cat.add(Product("P1", "Pen", 2.0))
    return cat

def test_add_item_not_in_catalog(catalog):
    cart = Cart(catalog)
    with pytest.raises(ValueError, match="Product not found"):
        cart.add_item("UNKNOWN", 1)

def test_add_item_invalid_quantity(catalog):
    cart = Cart(catalog)
    with pytest.raises(ValueError, match="Quantity must be > 0"):
        cart.add_item("P1", 0)

def test_cart_total_and_remove(catalog):
    cart = Cart(catalog)
    cart.add_item("P1", 3) # 3 * 2.0 = 6.0
    assert cart.total() == 6.0
    
    cart.remove_item("P1")
    assert cart.total() == 0.0