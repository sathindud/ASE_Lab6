import pytest
from unittest.mock import Mock
from models.cart import Cart
from models.catalog import Catalog
from models.product import Product

def test_add_item_fails_when_inventory_insufficient():
    catalog = Catalog()
    catalog.add(Product("P1", "Pen", 2.0))
    
    mock_inventory = Mock()
    mock_inventory.get_available.return_value = 2 # Only 2 left in stock
    
    cart = Cart(catalog, inventory_client=mock_inventory)
    
    with pytest.raises(ValueError, match="Insufficient inventory"):
        cart.add_item("P1", 3)