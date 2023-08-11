from collections import deque
from typing import List, Deque

from src.constants import EXCLUSIVE_STRATEGY
from src.strategies.distribution_strategy import DistributionStrategy

from src.models.motoboy import Motoboy
from src.models.store import Store
from src.models.order import Order


class ExclusiveFirstStrategy(DistributionStrategy):
    def distribute(self, motoboys: List[Motoboy], stores: List[Store]) -> List[Motoboy]:
        """
        Distribui os pedidos, dando prioridade aos pedidos exclusivos.

        :param motoboys: Lista de motoboys
        :param stores: Lista de lojas
        :return: Lista de motoboys com pedidos distribuídos
        """
        orders_queue = deque(
            [order for store in stores for order in store.orders])

        # Distribute exclusive orders
        self.distribute_exclusive_orders(motoboys, stores, orders_queue)

        # Distribute remaining orders equally
        self.distribute_remaining_orders_equally(motoboys, orders_queue, rule=EXCLUSIVE_STRATEGY)

        return motoboys

    def distribute_exclusive_orders(self, motoboys: List[Motoboy], stores: List[Store], orders_queue: Deque[Order]) -> None:
        """
        Distribui os pedidos exclusivos entre os motoboys e lojas.

        :param motoboys: Lista de motoboys
        :param stores: Lista de lojas
        :param orders_queue: Fila de pedidos restantes (utilizando collections.deque)
        """
        for motoboy in motoboys:
            if motoboy.exclusive_store:
                for order in [order for store in stores if store.id == motoboy.exclusive_store for order in store.orders]:
                    motoboy.add_order(order)
                    orders_queue.remove(order)
