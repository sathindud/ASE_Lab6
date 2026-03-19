# src/gateways/inventory.py
from typing import Protocol

class InventoryClient(Protocol):
    def get_available(self, sku: str) -> int:
        """Returns the available quantity for a given SKU."""
        ...

# In src/models/cart.py, update the import and type hint:
from gateways.inventory import InventoryClient

class Cart:
    def __init__(self, catalog: Catalog, inventory_client: InventoryClient = None):
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
