from models.product import Product

class Catalog:
    def __init__(self):
        self.products = {}
        
    def add(self, product: Product):
        self.products[product.sku] = product
        
    def get(self, sku: str):
        return self.products.get(sku, None)