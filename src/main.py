from typing import List, Optional

from src.models.motoboy import Motoboy

from src.utils.arguments import get_args
from src.utils.initializers import initialize_motoboys, initialize_stores
from src.utils.decorators import execution_time

from strategies.distribution_strategy import Context, DistributionStrategy
from strategies.exclusive_first_strategy import ExclusiveFirstStrategy


def print_motoboys(motoboys: List[Motoboy], motoboy_id: Optional[int] = None):
    """
    Imprime informações sobre motoboys.

    :param motoboys: Lista de motoboys.
    :param motoboy_id: ID opcional do motoboy para filtrar.
    """
    if motoboy_id:
        selected_motoboy = next((m for m in motoboys if m.id == motoboy_id), None)
        if selected_motoboy:
            print(selected_motoboy)
            return
        print(f'Motoboy com ID {motoboy_id} não encontrado.')

    for motoboy in motoboys:
        print(motoboy)


@execution_time
def main() -> None:
    """
    Função principal que inicializa as lojas e motoboys, define a estratégia de distribuição, executa a distribuição e imprime os resultados.
    """
    args = get_args()

    stores = initialize_stores()
    motoboys = initialize_motoboys()

    context = Context()

    # Pensando em escalabilidade, poderiamos ter um Facotry que retornaria a estrategia adequada com base nos argumentos.
    # context.strategy = DistributionStrategyFactory.get_strategy(args.strategy)

    context.strategy = ExclusiveFirstStrategy()
    context.exec_distribution(motoboys=motoboys, stores=stores)
    print()

    print_motoboys(motoboys=motoboys, motoboy_id=args.motoboy_id)


if __name__ == "__main__":
    main()
