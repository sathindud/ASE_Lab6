from unittest.mock import Mock
from models.cart import Cart
from models.catalog import Catalog
from models.product import Product
from services.checkout import CheckoutService

def test_checkout_creates_and_saves_order():
    catalog = Catalog()
    catalog.add(Product("P1", "Pen", 2.0))
    cart = Cart(catalog)
    cart.add_item("P1", 2)
    
    mock_payment = Mock()
    mock_payment.charge.return_value = True
    
    mock_repo = Mock()
    
    service = CheckoutService(mock_payment, order_repository=mock_repo)
    service.checkout(cart, "token_123")
    
    assert mock_repo.save.called
    saved_order = mock_repo.save.call_args[0][0]
    assert saved_order.total == 4.0