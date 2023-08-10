class Motoboy:
    def __init__(self, id, fee, exclusive_store=None):
        self.id = id
        self.fee = fee
        self.exclusive_store = exclusive_store
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def total_earning(self):
        return sum([self.fee + order.commission() for order in self.orders])

    def __str__(self):
        retorno = f'(Motoboy {self.id}): Possui {len(self.orders)} pedido(s), totalizando ganhos de R$ {self.total_earning():,.2f}'

        if self.exclusive_store:
            retorno += f' (Exclusivo da loja {self.exclusive_store})'

        return retorno
