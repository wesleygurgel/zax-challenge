from __future__ import annotations


class Order:
    def __init__(self, store: "Store", value: float) -> None:
        """
        Inicializa um objeto da classe Order.

        :param store: Objeto da loja associada ao pedido
        :param value: Valor total do pedido
        """
        self.store = store
        self.value = value

    def commission(self) -> float:
        """
        Calcula a comissão para o pedido com base na taxa de comissão da loja e no valor do pedido.

        :return: Valor da comissão para o pedido
        """
        return self.store.commission_fee * self.value
