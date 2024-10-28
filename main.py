from interface import * #from interface.display import clear_screen, menu
from core import * #from core.functions import sumar, restar, multiplicar, dividir, show_history

print('\n CALCULADORA SIMPLE. \n')


def main():
    while True:
        menu()
        choosed = input('¿Qué operación deseas realizar? ')
        match choosed:
            case 'A':
                clear_screen()
                sumar()
            case 'B':
                clear_screen()
                restar()
            case 'C':
                clear_screen()
                multiplicar()
            case 'D':
                clear_screen()
                dividir()
            case 'E':
                clear_screen()
                show_history()
            case 'F':
                clear_screen()
                print('Calculadora apagada. \n')
                break
            case _ :
                clear_screen()
                print('No ingresó una opción válida.\nIngrese una opción válida.')
                continue

        option = input('\n ¿Desea realizar otra operación? ')
        if option == 'Y':
            print('\n')
            continue
        elif option == 'N':
            clear_screen()
            print('Calculadora apagada. \n')
            break
        else:
            clear_screen()
            print('No ingresó una opción válida.')


if __name__ == '__main__':
    main()
