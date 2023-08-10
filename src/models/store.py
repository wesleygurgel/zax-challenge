from src.models.order import Order
from typing import List


class Store:
    def __init__(self, id: int, commission_fee: float):
        self.id = id
        self.commission_fee = commission_fee
        self.orders = []

    def add_order(self, order_value: float) -> None:
        self.orders.append(Order(self, order_value))

    def add_orders(self, order_values: List[float]) -> None:
        for order_value in order_values:
            self.add_order(order_value)
