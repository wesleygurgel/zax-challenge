from typing import Optional
from .order import Order


class Motoboy:

    MAX_ORDERS = 5  # Capacidade máxima de pedidos que um motoboy pode carregar

    def __init__(self, id: int, fee: float, exclusive_store: Optional[int] = None) -> None:
        """
        Inicializa um objeto da classe Motoboy.

        :param id: Identificador único do motoboy
        :param fee: Taxa básica que o motoboy recebe por entrega
        :param exclusive_store: Identificador da loja com a qual o motoboy tem exclusividade (opcional)
        """
        self.id = id
        self.fee = fee
        self.exclusive_store = exclusive_store
        self.orders = []  # Lista para armazenar pedidos

    def add_order(self, order: Order) -> None:
        """
        Adiciona um pedido à lista de pedidos do motoboy.

        :param order: Objeto de pedido que será adicionado
        """
        self.orders.append(order)

    def total_earning(self) -> float:
        """
        Calcula o total de ganhos do motoboy com base na taxa e comissões dos pedidos.

        :return: Total de ganhos do motoboy
        """
        return sum([self.fee + order.commission() for order in self.orders])

    def remaining_capacity(self) -> int:
        """
        Retorna a capacidade restante de pedidos que o motoboy pode carregar.

        :return: Número de pedidos adicionais que o motoboy pode carregar
        """
        return self.MAX_ORDERS - len(self.orders)

    def add_order(self, order: Order) -> None:
        """
        Adiciona um pedido à lista de pedidos do motoboy.

        :param order: Pedido a ser adicionado
        """
        if self.remaining_capacity() > 0:
            self.orders.append(order)
        else:
            raise Exception(
                f'Motoboy com ID {self.id} já atingiu a capacidade máxima de pedidos.')

    def __str__(self) -> str:
        """
        Retorna uma representação em string do objeto Motoboy.

        :return: Representação em string do motoboy
        """
        retorno = f'(Motoboy {self.id}): Possui {len(self.orders)} pedido(s), totalizando ganhos de R$ {self.total_earning():,.2f}'

        if self.exclusive_store:
            retorno += f' (Exclusivo da loja {self.exclusive_store})'

        return retorno
