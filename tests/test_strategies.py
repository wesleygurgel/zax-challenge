import random
from collections import deque

from src.constants import EXCLUSIVE_STRATEGY
from src.models.motoboy import Motoboy
from src.models.store import Store
from src.strategies.distribution_strategy import Context, DistributionStrategy
from src.strategies.exclusive_first_strategy import ExclusiveFirstStrategy


def generate_data() -> tuple:
    """Função para criar motoboys e lojas para teste."""
    # Criando três motoboys sem exclusividade
    motoboys = [Motoboy(i, 10 + i) for i in range(1, 4)]

    # Criando três lojas e adicionando pedidos
    stores = [Store(i, 0.1 * i) for i in range(1, 4)]
    for i, store in enumerate(stores):
        store.add_order([random.randint(20, 100) for _ in range(i + 1)])

    # Encontrando a loja com mais pedidos (neste caso, é a última loja)
    store_with_most_orders = stores[-1].id

    # Atribuindo exclusividade ao primeiro motoboy com a loja que tem mais pedidos
    motoboys[0].exclusive_store = store_with_most_orders

    return motoboys, stores


class TestContext:
    """Testes para a classe Context."""

    def test_context_initialization(self):
        """Testar a inicialização do contexto com uma estratégia."""
        strategy = ExclusiveFirstStrategy()
        context = Context(strategy)
        assert context.strategy == strategy

    def test_exec_distribution_with_exclusive_first_strategy(self):
        """Testar a execução da distribuição com a estratégia 'ExclusiveFirstStrategy'."""
        motoboys, stores = generate_data()
        strategy = ExclusiveFirstStrategy()
        context = Context(strategy)
        context.exec_distribution(motoboys=motoboys, stores=stores)
        assert len(motoboys[0].orders) == 3
        assert motoboys[0].orders[0].store.id == 3


class TestExclusiveFirstStrategy:
    """Testes para a classe ExclusiveFirstStrategy."""

    def test_distribute_exclusive_orders(self):
        """Testar a distribuição de ordens exclusivas."""
        motoboys, stores = generate_data()
        strategy = ExclusiveFirstStrategy()
        orders_queue = deque(
            [order for store in stores for order in store.orders])
        strategy.distribute_exclusive_orders(motoboys, stores, orders_queue)
        assert motoboys[0].orders[0].store.id == 3

    def test_distribute_remaining_orders_equally(self):
        """Testar a distribuição igualitária das ordens restantes."""
        motoboys, stores = generate_data()
        strategy = ExclusiveFirstStrategy()  # Poderia ser qualquer outra estratégia

        orders_queue = deque(
            [order for store in stores for order in store.orders])

        strategy.distribute_remaining_orders_equally(
            motoboys, orders_queue, rule=EXCLUSIVE_STRATEGY)

        # Primeiro motoboy não recebeu nenhuma ordem, pois é exclusivo.
        assert len(motoboys[0].orders) == 0
        assert len(motoboys[1].orders) == 3

    def test_distribute(self):
        """Testar o método de distribuição."""
        motoboys, stores = generate_data()
        strategy = ExclusiveFirstStrategy()
        result = strategy.distribute(motoboys, stores)
        assert len(result[0].orders) == 3
        assert result[0].orders[0].store.id == 3
