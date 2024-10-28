from interface import * #from interface.display import clear_screen, menu, get_option
from core import * #from core.functions import sumar, restar, multiplicar, dividir, show_history

print('\n*** CALCULADORA SIMPLE. ***\n')


def main():
    while True:
        menu()
        choosed = input('¿Qué operación deseas realizar? ').upper()
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
                print('\n *** Calculadora apagada. ***\n')
                break
            case _ :
                clear_screen()
                print('No ingresó una opción válida.\nIngrese una opción válida.')
                continue

        option = get_option() #input('\n ¿Desea realizar otra operación? ')
        if option == 'S':
            clear_screen()
            continue
        elif option == 'N':
            clear_screen()
            print('\n *** Calculadora apagada. ***\n')
            break
        #else:
        #    clear_screen()
        #    print('No ingresó una opción válida.')


if __name__ == '__main__':
    main()
