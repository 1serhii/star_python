from dataclasses import dataclass


@dataclass
class ProductTypes:
    subscription: str = "Subscription"
    product: str = "Product"
    upgrade: str = "Upgrade"


class Product:
    def __init__(self, name: str, sale_type: str):
        self.name = name
        self.sale_type = sale_type


product_a = Product(name="ProductA", sale_type=ProductTypes.subscription)
product_b = Product(name="ProductB", sale_type=ProductTypes.product)
product_c = Product(name="ProductC", sale_type=ProductTypes.upgrade)
