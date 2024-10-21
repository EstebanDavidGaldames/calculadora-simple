import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def menu():
    print('Opciones: \n')
    print('A: SUMA')
    print('B: RESTA')
    print('C: MULTIPLICACIÓN')
    print('D: DIVISIÓN')
    print('E: MOSTRAR HISTORIAL')
    print('F: SALIR')
