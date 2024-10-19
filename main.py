import os


print('\n CALCULADORA SIMPLE. \n')

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


historial = []


def suma(): #number1:float, number2:float) -> float:
    number1 = float(input('Ingrese el primer sumando: '))
    number2 = float(input('Ingrese el segundo sumando: '))
    resultado = number1 + number2 #suma
    print(f'Su operación es: {number1} + {number2} = {resultado}')
    return historial.append(f'{number1} + {number2} = {resultado}')


def resta(): #number1:float, number2:float) -> float:
    number1 = float(input('Ingrese el minuendo: '))
    number2 = float(input('Ingrese el sustraendo: '))
    resultado = number1 - number2 #resto o diferencia
    print(f'Su operación es: {number1} - {number2} = {resultado}')
    return historial.append(f'{number1} - {number2} = {resultado}')


def multiplicacion(): #number1:float, number2:float) -> float:
    number1 = float(input('Ingrese el primer factor: '))
    number2 = float(input('Ingrese el segundo factor: '))
    resultado = number1 * number2
    print(f'Su operación es: {number1} x {number2} = {resultado}')
    return historial.append(f'{number1} x {number2} = {resultado}')


def division(): #number1:float, number2:float) -> float:
    number1 = float(input('Ingrese el dividendo: '))
    number2 = float(input('Ingrese el divisor: '))
    resultado = number1 / number2
    print(f'Su operación es: {number1} / {number2} = {resultado}')
    return historial.append(f'{number1} / {number2} = {resultado}')


def show_history():
    if not historial:
        print('No se realizaron cálculos.')
    else:
        print('\n Cálculos realizados: \n')
        for element in historial:
            print(element)


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
