class Cart:
    def __init__(self):
        self._items = []

    def add_item(self, product):
        self._items.append(product)

    def get_total(self):
        return sum(item.price for item in self._items)
