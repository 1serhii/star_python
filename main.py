from products import product_a, product_b, product_c
from сustomer import Customer

subscription_cast = Customer(name='John', customer_type_suffix='s', longevity_years=3)
cash_cast = Customer(name='Dorian', customer_type_suffix='c', longevity_years=3)

subscription_cast.buy_product(product=product_a)
subscription_cast.buy_product(product=product_a)
subscription_cast.buy_product(product=product_b)
subscription_cast.buy_product(product=product_a)
cash_cast.buy_product(product=product_a)
cash_cast.buy_product(product=product_b)
cash_cast.buy_product(product=product_c)

print(subscription_cast.get_info())
print(cash_cast.get_info())
