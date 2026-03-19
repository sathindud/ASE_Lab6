# src/gateways/payment.py
from typing import Protocol

class PaymentGateway(Protocol):
    def charge(self, amount: float, token: str) -> bool:
        ...

# src/services/checkout.py
from models.cart import Cart
from gateways.payment import PaymentGateway

class PaymentDeclinedError(Exception):
    pass

class CheckoutService:
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway

    def checkout(self, cart: Cart, token: str) -> bool:
        if not cart.items:
            raise ValueError("Cart is empty")
            
        amount = cart.total()
        if not self.payment_gateway.charge(amount, token):
            raise PaymentDeclinedError("Payment declined by gateway")
            
        return True