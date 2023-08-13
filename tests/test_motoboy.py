import pytest
from src.models.motoboy import Motoboy
from src.models.store import Store
from src.models.order import Order


@pytest.fixture
def store():
    return Store(id=1, commission_fee=0.05)


@pytest.fixture
def order(store):
    return Order(store, value=100)


@pytest.fixture
def motoboy():
    return Motoboy(id=1, fee=10, exclusive_store=2)


def test_motoboy_initialization(motoboy):
    assert motoboy.id == 1
    assert motoboy.fee == 10
    assert motoboy.exclusive_store == 2
    assert motoboy.orders == []


def test_add_order(motoboy, order):
    motoboy.add_order(order)
    assert len(motoboy.orders) == 1
    assert motoboy.orders[0] == order


def test_total_earning(motoboy, order):
    motoboy.add_order(order)
    assert motoboy.total_earning() == 15
