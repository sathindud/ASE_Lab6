import pytest
from src.models.product import Product
from src.models.cart import Cart

def test_cart_initial_total_is_zero():
    cart = Cart()
    assert cart.get_total() == 0.0

def test_add_product_to_cart_updates_total():
    cart = Cart()
    product1 = Product("P1", "Widget", 10.0)
    product2 = Product("P2", "Gizmo", 20.0)
    
    cart.add_item(product1)
    cart.add_item(product2)
    
    assert cart.get_total() == 30.0

# Red Tests

def test_create_product_negative_price():
    with pytest.raises(ValueError):
        Product(sku="APPLE-01", name="Apple", price=-1.5)

def test_catalog_add_and_search():
    catalog = Cart()
    p = Product(sku="APPLE-01", name="Apple", price=1.5)
    catalog.add_item(p)
    assert catalog.get_total() == p

def test_catalog_search_missing_returns_none():
    catalog = Cart()
    assert catalog.get_total() is None
