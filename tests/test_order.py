import pytest
from src.models.store import Store
from src.models.order import Order


@pytest.fixture
def store():
    return Store(id=1, commission_fee=0.05)


@pytest.fixture
def order(store):
    return Order(store, value=100)


def test_order_initialization(order, store):
    assert order.store == store
    assert order.value == 100


def test_order_commission(order):
    assert order.commission() == 5
