from collections import deque
from strategies.distribution_strategy import DistributionStrategy


class ExclusiveFirstStrategy(DistributionStrategy):
    def distribute(self, motoboys, stores):
        orders_queue = deque(
            [order for store in stores for order in store.orders])

        # Distribute exclusive orders
        self.distribute_exclusive_orders(motoboys, stores, orders_queue)

        # Distribute remaining orders equally
        self.distribute_remaining_orders_equally(motoboys, orders_queue)

        return motoboys

    def distribute_exclusive_orders(self, motoboys, stores, orders_queue):
        for motoboy in motoboys:
            if motoboy.exclusive_store:
                for order in [order for store in stores if store.id == motoboy.exclusive_store for order in store.orders]:
                    motoboy.add_order(order)
                    orders_queue.remove(order)