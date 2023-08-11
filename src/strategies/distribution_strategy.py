from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from src.utils import rules as rules_methods


class Context():

    def __init__(self, strategy: DistributionStrategy = None) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> DistributionStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: DistributionStrategy) -> None:
        self._strategy = strategy

    def exec_distribution(self, motoboys, stores) -> None:
        self._strategy.distribute(motoboys, stores)


class DistributionStrategy(ABC):

    @abstractmethod
    def distribute(self, motoboys, stores):
        pass

    def distribute_remaining_orders_equally(self, motoboys, orders_queue, rule: str) -> List[Motoboy]:
        motoboy_index = 0
        while orders_queue:
            motoboy = motoboys[motoboy_index]
            if not getattr(rules_methods, rule)(motoboy):
                motoboy.add_order(orders_queue.popleft())
            motoboy_index = (motoboy_index + 1) % len(motoboys)
