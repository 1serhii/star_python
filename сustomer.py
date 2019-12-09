from datetime import datetime
from products import Product

customer_types = {
    's': "Subscription",
    'a': "Account",
    'c': "Cash"
}


class Customer:
    """
    Class describe Customer properties and behaviour
    """
    def __init__(self, name: str, customer_type_suffix: str, longevity_years: int):
        self.customer_type = customer_types.get(customer_type_suffix.lower())
        self.customer_type_suffix = customer_type_suffix
        self.__check_customer_type()
        self.name = name
        self.longevity_years = longevity_years
        self.sales = {}

    def get_info(self, year_shift: int = 1) -> str:
        """
        Return Customer info as a string with it name, and all purchased products
        :param int year_shift: purchased products for last years
        """
        product_info = self.get_products_for_last_years(year_shift)
        last_year_purchase = []
        for i in set(product_info):
            last_year_purchase.append(f'{product_info.count(i)} x {i}')
        last_year_purchase = ", ".join(last_year_purchase)

        return f'Name: {self.name}[{self.customer_type_suffix.upper()}], ' \
               f'Duration: {self.longevity_years} years, ' \
               f'Purchases in the last year: {last_year_purchase}'

    def get_products_for_last_years(self, year_shift: int) -> list:
        """
        Get products for last years shift, f.e. for last 3 years
        """
        res = []
        for product, details in self.sales.items():
            p_name = f'{product}[{details.get("sale_type")[0]}]'
            for date in details.get('purchase_dates', []):
                if datetime.now().year - year_shift <= date.year:
                    res.append(p_name)
        return res

    def buy_product(self, product: Product):
        """
        Purchase given product and add it to sales history
        """
        if self.customer_type == customer_types['c'] and product.sale_type == "Subscription":
            print(f'{self.customer_type} customers cannot buy {product.sale_type} products. {product.name}')
            return
        if not self.sales.get(product.name):
            self.sales.update({product.name: {'purchase_dates': [datetime.now()],
                                              'sale_type': product.sale_type}})
        else:
            self.sales[product.name]['purchase_dates'].append(datetime.now())

    def __check_customer_type(self):
        """
        Check if customer has a correct type.
        """
        if not self.customer_type:
            raise ValueError(f'Unsupported customer type. Use one from following: {list(customer_types.keys())}')
