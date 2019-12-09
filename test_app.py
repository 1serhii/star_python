from products import Product
from сustomer import Customer


def buy_product_for_cust(cust: Customer, product: Product, quantity: int):
    for _ in range(quantity):
        cust.buy_product(product)


def test_buy_products(all_customers, product_type_product):
    all_customers.buy_product(product=product_type_product)
    assert all_customers.get_products_for_last_years(year_shift=3) == [product_type_product.name_with_prefix]


def test_cash_customer_cannot_buy_subscription_product(cash_customer, subscription_type_product):
    cash_customer.buy_product(subscription_type_product)
    assert cash_customer.sales == {}


def test_get_products_by_year_shift(account_customer, upgrade_type_product, subscription_type_product):
    account_customer.buy_product(upgrade_type_product)
    account_customer.buy_product(subscription_type_product)
    subs_sales = account_customer.sales.get(subscription_type_product.name)
    assert subs_sales  # no reason to continue if product is missing
    real_date = subs_sales['purchase_dates'][0]
    new_date = real_date.replace(year=2012)
    subs_sales['purchase_dates'][0] = new_date
    assert account_customer.get_products_for_last_years(1) == [upgrade_type_product.name_with_prefix]


def test_buy_product_several_times(account_customer, upgrade_type_product):
    test_quantity = 3
    buy_product_for_cust(account_customer, upgrade_type_product, test_quantity)
    sales = account_customer.sales.get(upgrade_type_product.name, {}).get('purchase_dates')
    assert len(sales) == test_quantity, f'ar: {len(sales)}, er: {test_quantity}'


def test_show_full_info(account_customer, subscription_type_product):
    test_quantity = 3
    buy_product_for_cust(account_customer, subscription_type_product, test_quantity)
    assert account_customer.get_info() == 'Name: Ted[A], Duration: 2 years, Purchases in the last year: 3 x ProductA[S]'
