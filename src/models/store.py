from src.models.order import Order
from typing import List, Union, overload


class Store:
    """
    Representa uma loja que mantém uma lista de pedidos. Cada loja tem um ID único e uma taxa de comissão
    associada a ela.

    :param id: ID único da loja
    :param commission_fee: Taxa de comissão aplicada aos pedidos
    """

    def __init__(self, id: int, commission_fee: float) -> None:
        """
        Inicializa a loja com o ID e a taxa de comissão fornecidos.

        :param id: ID único da loja
        :param commission_fee: Taxa de comissão aplicada aos pedidos
        """
        self.id = id
        self.commission_fee = commission_fee
        self.orders = []

    @overload
    def add_order(self, order_value: float) -> None:
        """
        Adiciona um pedido à lista de pedidos da loja.

        :param order_value: Valor do pedido a ser adicionado
        """
        ...

    @overload
    def add_order(self, order_values: List[float]) -> None:
        """
        Adiciona vários pedidos à lista de pedidos da loja.

        :param order_values: Lista de valores de pedidos a serem adicionados
        """
        ...

    def add_order(self, order_values: Union[float, List[float]]) -> None:
        if isinstance(order_values, list):
            for order_value in order_values:
                self.orders.append(Order(self, order_value))
        else:
            self.orders.append(Order(self, order_values))
