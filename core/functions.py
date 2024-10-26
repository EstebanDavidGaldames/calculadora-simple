
historial = []


def suma():
    number1 = float(input('Ingrese el primer sumando: '))
    number2 = float(input('Ingrese el segundo sumando: '))
    resultado = number1 + number2 #suma
    print(f'Su operación es: {number1} + {number2} = {resultado}')
    return historial.append(f'{number1} + {number2} = {resultado}')


def resta():
    number1 = float(input('Ingrese el minuendo: '))
    number2 = float(input('Ingrese el sustraendo: '))
    resultado = number1 - number2 #resto o diferencia
    print(f'Su operación es: {number1} - {number2} = {resultado}')
    return historial.append(f'{number1} - {number2} = {resultado}')


def multiplicacion():
    number1 = float(input('Ingrese el primer factor: '))
    number2 = float(input('Ingrese el segundo factor: '))
    resultado = number1 * number2
    print(f'Su operación es: {number1} x {number2} = {resultado}')
    return historial.append(f'{number1} x {number2} = {resultado}')


def division():
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
