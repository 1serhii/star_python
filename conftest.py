import pytest

from products import Product, ProductTypes
from сustomer import Customer


@pytest.fixture()
def subscription_customer():
    return Customer(name='John', customer_type_suffix='s', longevity_years=4)


@pytest.fixture()
def cash_customer():
    return Customer(name='Dorian', customer_type_suffix='c', longevity_years=3)


@pytest.fixture()
def account_customer():
    return Customer(name='Ted', customer_type_suffix='a', longevity_years=2)


@pytest.fixture(params=["subscription_customer", "cash_customer", "account_customer"])
def all_customers(request):
    yield request.getfixturevalue(request.param)
    # yield request.param


@pytest.fixture(scope="session")
def subscription_type_product():
    return Product(name="ProductA", sale_type=ProductTypes.subscription)


@pytest.fixture(scope="session")
def product_type_product():
    return Product(name="ProductB", sale_type=ProductTypes.product)


@pytest.fixture(scope="session")
def upgrade_type_product():
    return Product(name="ProductC", sale_type=ProductTypes.upgrade)
