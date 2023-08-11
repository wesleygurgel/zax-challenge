from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Deque
from collections import deque

from src.models.motoboy import Motoboy
from src.models.store import Store
from src.models.order import Order

from src.utils import rules as rules_methods


class Context:
    """
    Define a interface de execução da estratégia de distribuição.
    """

    def __init__(self, strategy: DistributionStrategy = None) -> None:
        """
        Inicializa o contexto com uma estratégia de distribuição opcional.

        :param strategy: Estratégia de distribuição (opcional)
        """
        self._strategy = strategy

    @property
    def strategy(self) -> DistributionStrategy:
        """
        :return: Retorna a estratégia de distribuição atual
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: DistributionStrategy) -> None:
        """
        Define uma nova estratégia de distribuição.

        :param strategy: Nova estratégia de distribuição
        """
        self._strategy = strategy

    def exec_distribution(self, motoboys: List[Motoboy], stores: List[Store]) -> None:
        """
        Executa a distribuição de pedidos usando a estratégia definida.

        :param motoboys: Lista de motoboys
        :param stores: Lista de lojas
        """
        self._strategy.distribute(motoboys, stores)


class DistributionStrategy(ABC):
    """
    Interface base para estratégias de distribuição.
    """

    @abstractmethod
    def distribute(self, motoboys: List[Motoboy], stores: List[Store]) -> None:
        """
        Método abstrato para distribuir pedidos.

        :param motoboys: Lista de motoboys
        :param stores: Lista de lojas
        """
        pass

    def distribute_remaining_orders_equally(self, motoboys: List[Motoboy], orders_queue: Deque[Order], rule: str) -> List[Motoboy]:
        """
        Distribui os pedidos restantes igualmente entre os motoboys.

        Por se tratar de uma função auxiliar, se faz necessário passar a regra de distribuição como parâmetro: "rule".

        Assim podemos remover o Motoboy que foi contemplado com a Estratégia de Distribuição prioritária.

        :param motoboys: Lista de motoboys
        :param orders_queue: Fila de pedidos restantes (utilizando collections.deque)
        :param rule: Nome do método dentro do módulo src/utils/rules.py
        :return: Lista de motoboys com pedidos distribuídos
        """
        motoboy_index = 0
        while orders_queue:
            motoboy = motoboys[motoboy_index]
            if not getattr(rules_methods, rule)(motoboy):
                motoboy.add_order(orders_queue.popleft())
            motoboy_index = (motoboy_index + 1) % len(motoboys)
        return motoboys
