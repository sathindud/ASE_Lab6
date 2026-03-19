from models.catalog import Catalog
from models.product import Product

class Cart:
    def __init__(self, catalog: Catalog, inventory_client=None):
        self.catalog = catalog
        self.inventory_client = inventory_client
        self.items = {}

    def add_item(self, sku: str, quantity: int):
        # ... previous quantity and catalog checks ...
        product = self.catalog.get(sku)
        if not product:
            raise ValueError("Product not found")
            
        if self.inventory_client and self.inventory_client.get_available(sku) < quantity:
            raise ValueError("Insufficient inventory")
            
        # ... append to self.items ...
        if sku in self.items:
            self.items[sku]['qty'] += quantity
        else:
            self.items[sku] = {'product': product, 'qty': quantity}


    def total(self) -> float:
        subtotal = 0.0
        for item in self.items.values():
            line_price = item['product'].price * item['qty']
            if item['qty'] >= 10:
                line_price *= 0.90 # 10% bulk discount
            subtotal += line_price
            
        if subtotal >= 1000.0:
            subtotal *= 0.95 # 5% order discount
            
        return subtotal