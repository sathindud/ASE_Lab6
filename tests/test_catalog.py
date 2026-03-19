import pytest
from models.product import Product
from models.catalog import Catalog

def test_create_product_valid():
    p = Product(sku="APPLE-01", name="Apple", price=1.5)
    assert p.sku == "APPLE-01"
    assert p.name == "Apple"
    assert p.price == 1.5

def test_create_product_negative_price():
    with pytest.raises(ValueError, match="Price cannot be negative"):
        Product(sku="APPLE-01", name="Apple", price=-1.5)

# Red Tests

def test_catalog_add_and_search():
    catalog = Catalog()
    p = Product(sku="APPLE-01", name="Apple", price=1.5)
    catalog.add(p)
    assert catalog.get("APPLE-01") == p

def test_catalog_search_missing_returns_none():
    catalog = Catalog()
    assert catalog.get("MISSING-99") is None