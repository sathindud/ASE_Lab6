from dataclasses import dataclass

@dataclass
class Product:
    sku: str
    name: str
    price: float
    
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")