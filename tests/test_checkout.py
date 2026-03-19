import pytest
from unittest.mock import Mock
from models.cart import Cart
from models.catalog import Catalog
from models.product import Product
from services.checkout import CheckoutService

def test_successful_checkout():
    catalog = Catalog()
    catalog.add(Product("P1", "Pen", 2.0))
    cart = Cart(catalog)
    cart.add_item("P1", 2)
    
    mock_payment = Mock()
    mock_payment.charge.return_value = True
    
    service = CheckoutService(mock_payment)
    result = service.checkout(cart, "token_123")
    
    assert result is True
    mock_payment.charge.assert_called_with(4.0, "token_123")

def test_failed_checkout_payment_declined():
    catalog = Catalog()
    catalog.add(Product("P1", "Pen", 2.0))
    cart = Cart(catalog)
    cart.add_item("P1", 2)
    
    mock_payment = Mock()
    mock_payment.charge.return_value = False
    
    service = CheckoutService(mock_payment)
    with pytest.raises(Exception, match="Payment declined"):
        service.checkout(cart, "token_bad")