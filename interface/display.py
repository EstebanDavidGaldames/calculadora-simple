import os

from files_management import read_file, delete_content


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


def get_answer():
    answer = input('\n ¿Desea conservar el historial de cálculos? (S --> Sí / N -- > No): ').upper()
    
    if answer == 'S':
        return
    elif answer == 'N':
        delete_content()
        return
    else:
        print('\n Ingrese S para Sí o N para No.')
        return get_answer()


def ask_delete():
    historial = (read_file())
    comparador = ['']

    if historial == comparador or historial == None:
        return
    else:
        get_answer()
        return
