import argparse
import sys
from argparse import Namespace


def get_args() -> Namespace:
    """
    Configura e analisa os argumentos de linha de comando para o processamento do ID do motoboy.

    :return: Um objeto Namespace contendo os argumentos fornecidos na linha de comando.
    """
    parser = argparse.ArgumentParser(description='Process motoboy ID.')
    parser.add_argument('--motoboy_id', type=int, default=None)

    args, unknown_args = parser.parse_known_args()

    if len(sys.argv) > 1:
        if args.motoboy_id is not None:
            print(f"Filtro por Motoboy com ID {args.motoboy_id}.")
        else:
            unknown_args_str = ' '.join(unknown_args)
            print(
                f"Nenhum argumento válido encontrado. Argumento(s) recebido(s): '{unknown_args_str}' | Sugestão: 'python main.py --motoboy_id 1'")

    return args
