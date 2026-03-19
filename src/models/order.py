# src/models/order.py
from dataclasses import dataclass, field
import time

@dataclass
class Order:
    items: dict
    total: float
    timestamp: float = field(default_factory=time.time)