from dataclasses import dataclass


@dataclass
class ProductTypes:
    """ Data class to store available product types """
    subscription: str = "Subscription"
    product: str = "Product"
    upgrade: str = "Upgrade"


class Product:
    """ Class represents behaviour and properties of product """
    def __init__(self, name: str, sale_type: str):
        self.name = name
        self.sale_type = sale_type

    @property
    def name_with_prefix(self) -> str:
        """ Get product name with prefix """
        return f'{self.name}[{self.sale_type[0].upper()}]'
