from src.models.motoboy import Motoboy

def exclusive(motoboy: Motoboy) -> bool:
    """
    Verifica se o motoboy tem uma loja exclusiva.

    :param motoboy: O objeto Motoboy a ser verificado.
    :return: True se o motoboy tem uma loja exclusiva, False caso contrário.
    """
    return motoboy.exclusive_store is not None
