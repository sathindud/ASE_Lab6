# src/services/discount_engine.py
def apply_bulk_discount(items: dict) -> float:
    subtotal = 0.0
    for item in items.values():
        line_price = item['product'].price * item['qty']
        if item['qty'] >= 10:
            line_price *= 0.90
        subtotal += line_price
    return subtotal

def apply_order_discount(subtotal: float) -> float:
    if subtotal >= 1000.0:
        return subtotal * 0.95
    return subtotal

class DiscountEngine:
    def calculate_total(self, items: dict) -> float:
        subtotal = apply_bulk_discount(items)
        final_total = apply_order_discount(subtotal)
        return final_total

# src/models/cart.py
from services.discount_engine import DiscountEngine

class Cart:
    # ...
    def total(self) -> float:
        engine = DiscountEngine()
        return engine.calculate_total(self.items)