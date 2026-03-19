class Product:
    def __init__(self, sku: str, name: str, price: float):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.sku = sku
        self.name = name
        self.price = price