import pytest
from src.models.store import Store


@pytest.fixture
def store():
    return Store(id=1, commission_fee=0.05)


def test_store_initialization(store):
    assert store.id == 1
    assert store.commission_fee == 0.05
    assert store.orders == []


def test_add_order(store):
    store.add_order(100)
    assert len(store.orders) == 1
    assert store.orders[0].value == 100
