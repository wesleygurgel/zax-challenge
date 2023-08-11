from models.motoboy import Motoboy
from models.store import Store
from typing import List


def initialize_stores() -> List[Store]:
    """
    Inicializa e retorna uma lista de objetos Store.

    :return: Lista de objetos Store.
    """
    stores = [Store(id=1, commission_fee=0.05), Store(id=2, commission_fee=0.05), Store(id=3, commission_fee=0.15)]
    stores[0].add_order([50, 50, 50])
    stores[1].add_order([50, 50, 50, 50])
    stores[2].add_order([50, 50, 100])
    return stores


def initialize_motoboys() -> List[Motoboy]:
    """
    Inicializa e retorna uma lista de objetos Motoboy.

    :return: Lista de objetos Motoboy.
    """
    return [
        Motoboy(id=1, fee=2),
        Motoboy(id=2, fee=2),
        Motoboy(id=3, fee=2),
        Motoboy(id=4, fee=2, exclusive_store=1),
        Motoboy(id=5, fee=3)
    ]
