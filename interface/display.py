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
    print('F: SALIR\n')


def get_option():
    option = input('\n ¿Desea realizar otra operación? (S --> Sí / N -- > No): ').upper()
    if option == 'S' or option == 'N':
        return option
    else:
        print('\n Ingrese S para Sí o N para No.')
        return get_option()
