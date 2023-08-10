import argparse
import sys


def get_args():
    parser = argparse.ArgumentParser(description='Process motoboy ID.')
    parser.add_argument('--motoboy_id', type=int, default=None)

    args, unknown_args = parser.parse_known_args()

    if len(sys.argv) > 1:
        if args.motoboy_id is not None:
            print(f"Filtro por Motoboy com ID {args.motoboy_id}.")
        else:
            unknown_args_str = ' '.join(unknown_args)
            print(f"Nenhum argumento válido encontrado. Argumento(s) recebido(s): '{unknown_args_str}' | Sugestão: 'python main.py --motoboy_id 1'")


    return args
