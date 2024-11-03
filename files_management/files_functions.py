FILE_NAME = 'calculos.txt'

def write_file(calculo_realizado : str = '') -> None:
    with open(FILE_NAME, 'a') as file:
        file.write(f'{calculo_realizado}\n')


def read_file() -> list[str]:
    try:
        with open(FILE_NAME, 'r') as file:
            lista_auxiliar = file.read().split('\n')
            return lista_auxiliar
    except FileNotFoundError:
        write_file()


def delete_content():
    with open(FILE_NAME, 'w') as file:
        file.write('')