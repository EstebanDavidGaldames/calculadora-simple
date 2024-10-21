from display import clear_screen, menu
from functions import suma, resta, multiplicacion, division, show_history


print('\n CALCULADORA SIMPLE. \n')


def main():
    while True:
        menu()
        choosed = input('¿Qué operación deseas realizar? ')
        match choosed:
            case 'A':
                clear_screen()
                suma()
            case 'B':
                clear_screen()
                resta()
            case 'C':
                clear_screen()
                multiplicacion()
            case 'D':
                clear_screen()
                division()
            case 'E':
                clear_screen()
                show_history()
            case 'F':
                clear_screen()
                print('Calculadora apagada. \n')
                break

        option = input('\n ¿Desea realizar otra operación? ')
        if option == 'Y':
            print('\n')
            continue
        elif option == 'N':
            clear_screen()
            print('Calculadora apagada. \n')
            break


if __name__ == '__main__':
    main()
