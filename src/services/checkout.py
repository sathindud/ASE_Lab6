from models.cart import Cart
from gateways.payment import PaymentGateway
from models.order import Order

class PaymentDeclinedError(Exception):
    pass

class CheckoutService:
    def __init__(self, payment_gateway: PaymentGateway, order_repository=None):
        self.payment_gateway = payment_gateway
        self.order_repository = order_repository

    def checkout(self, cart: Cart, token: str) -> bool:
        if not cart.items:
            raise ValueError("Cart is empty")
            
        amount = cart.total()
        
        # 1. Charge the payment
        if not self.payment_gateway.charge(amount, token):
            raise PaymentDeclinedError("Payment declined by gateway")
            
        # 2. If successful and we have a repo, save the order
        if self.order_repository:
            order = Order(items=cart.items.copy(), total=amount)
            self.order_repository.save(order)
            
        return True