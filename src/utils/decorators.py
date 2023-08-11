import time
from functools import wraps
from typing import Callable, Any


def execution_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorador para calcular e imprimir o tempo de execução de uma função em milissegundos.

    :param func: A função cujo tempo de execução será medido.
    :return: Uma função wrapper que inclui a medição do tempo de execução.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000
        print(f"\nTempo de execução: {execution_time_ms:.2f} ms")
        return result
    return wrapper
